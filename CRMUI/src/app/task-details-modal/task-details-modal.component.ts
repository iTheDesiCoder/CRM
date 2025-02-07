import { Component, Input } from '@angular/core';
import { BsModalRef } from 'ngx-bootstrap/modal';
import { Task } from '../models/task.model';
import { TaskService } from '../services/task.service';

@Component({
  selector: 'app-task-details-modal',
  templateUrl: './task-details-modal.component.html',
  styleUrls: ['./task-details-modal.component.scss'],
  standalone:false
})
export class TaskDetailsModalComponent {
  @Input() task: any;
  editableTask!: Task;
  taskNotes: string[] = [];  // Store notes for the current task
  newNote: string = '';  // For new note input

  // Status options for the dropdown
  statusOptions: string[] = ['New', 'In-Progress', 'Completed'];

  constructor(public modalRef: BsModalRef, private taskService: TaskService) {}

  ngOnInit(): void {
    // Make a copy of the task for editing
    this.editableTask = { ...this.task };
  }

  addNote() {
    if (this.newNote.trim()) {
      this.taskNotes.push(this.newNote);
      this.newNote = '';  // Clear the input
    }
  }

  saveTask(): void {
    if (this.newNote.trim()) {
      this.editableTask.description += `\nNote: ${this.newNote}`;
    }

    this.taskService.updateTask(this.editableTask).subscribe(() => {
      this.modalRef.hide();  // Close modal after save
      this.taskService.notifyTaskListUpdated();  // Refresh task list
    });
  }
  
  getFormattedDescription(): string {
    return this.task.description.replace(/\n/g, '<br>');
  }
  closeModal() {
    this.modalRef.hide();
  }
}
