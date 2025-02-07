import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import { Task } from '../models/task.model';

@Injectable({
  providedIn: 'root'
})
export class TaskService {
  private taskListUpdated = new Subject<void>();
  private apiUrl = 'http://127.0.0.1:8000/tasks';  // FastAPI backend URL

  constructor(private http: HttpClient) {}

  // Fetch a specific task by ID
  getTaskById(taskId: number): Observable<Task> {
    return this.http.get<Task>(`${this.apiUrl}/${taskId}`);
  }
  
  // GET request to fetch tasks from the backend
  getTasks(): Observable<Task[]> {
    return this.http.get<Task[]>(this.apiUrl);
  }

  // PUT request to update the task in the backend (memory cache)
  updateTask(task: Task): Observable<Task> {
    console.log(task);
    return this.http.put<Task>(`${this.apiUrl}/${task.id}`, task);
  }

  // Notify components that the task list has been updated (same as before)
  notifyTaskListUpdated(): void {
    this.taskListUpdated.next();
  }

  // Observable to let components know when to refresh the task list
  onTaskListUpdated(): Observable<void> {
    return this.taskListUpdated.asObservable();
  }
}
