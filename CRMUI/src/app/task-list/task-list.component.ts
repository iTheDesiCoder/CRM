import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BsModalService } from 'ngx-bootstrap/modal';
import { TaskDetailsModalComponent } from '../task-details-modal/task-details-modal.component';
import { PolicyDetailsModalComponent } from '../policy-details-modal/policy-details-modal.component';
import { TaskService } from '../services/task.service';
import { Task } from '../models/task.model';

@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.scss'],
  standalone:false
})
export class TaskListComponent implements OnInit {
  tasks: any[] = [];
  currentPageTasks: Task[] = [];  // For pagination
  filteredTasks: any[] = [];
  totalRecords = 0;

  // Filter variables
  startDate: string = '';
  endDate: string = '';
  selectedStatus: string = '';
  accountFilter: string = '';

  statuses = ["New", "In-Progress", "Completed"];

  constructor(private http: HttpClient, private taskService: TaskService, private modalService: BsModalService) {}

  ngOnInit() {
    this.fetchTasks();
    // Subscribe to task list update notifications
    this.taskService.onTaskListUpdated().subscribe(() => {
      this.fetchTasks();  // Refresh the tasks when notified
    })
  }

  fetchTasks() {
   /* this.http.get<any[]>('assets/tasks.json').subscribe((data) => {
      this.tasks = data;
      this.filteredTasks = [...this.tasks];  // Initialize filtered tasks
      this.totalRecords = this.tasks.length;
    });*/

    this.taskService.getTasks().subscribe(
      (data) => {
        this.tasks = data;  // Assign fetched data to tasks array
        console.log("We got data",this.tasks);
        this.filteredTasks = [...this.tasks];
        this.setPageData(1);  // Initialize pagination
      },
      (error) => {
        console.error('Error fetching tasks:', error);
      }
    );
  }



  applyFilters() {
    this.filteredTasks = this.tasks.filter(task => {
      // Filter by date range
      const taskDate = new Date(task.publishDate);
      const start = this.startDate ? new Date(this.startDate) : null;
      const end = this.endDate ? new Date(this.endDate) : null;

      if (start && taskDate < start) return false;
      if (end && taskDate > end) return false;

      // Filter by status
      if (this.selectedStatus && task.status !== this.selectedStatus) return false;

      // Filter by account number
      if (this.accountFilter && !task.accountNumber.includes(this.accountFilter)) return false;

      return true;  // Include task if all conditions pass
    });

    this.setPageData(1);
  }

  // Pagination logic (as before)
  setPageData(pageNumber: number): void {
    const pageSize = 10;
    const startIndex = (pageNumber - 1) * pageSize;
    this.currentPageTasks = this.filteredTasks.slice(startIndex, startIndex + pageSize);
  }
  openTaskDetailsModal(task: any) {
    const initialState = { task };
    this.modalService.show(TaskDetailsModalComponent, { initialState });
  }

  openPolicyDetailsModal(policy: any) {
    const initialState = { policy };
    this.modalService.show(PolicyDetailsModalComponent, { initialState });
  }

  getStatusClass(status: string): string {
    switch (status) {
      case 'New': return 'badge bg-primary';
      case 'In-Progress': return 'badge bg-warning';
      case 'Completed': return 'badge bg-success';
      default: return 'badge bg-secondary';
    }
  }

  getPriorityClass(priority: string): string {
    switch (priority) {
      case 'High': return 'text-danger fw-bold';
      case 'Medium': return 'text-warning fw-bold';
      case 'Low': return 'text-success fw-bold';
      default: return 'text-muted';
    }
  }
}
