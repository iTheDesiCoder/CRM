import { Component, Input } from '@angular/core';
import { BsModalRef } from 'ngx-bootstrap/modal';

@Component({
  selector: 'app-task-details-modal',
  templateUrl: './task-details-modal.component.html',
  styleUrls: ['./task-details-modal.component.scss'],
  standalone:false
})
export class TaskDetailsModalComponent {
  @Input() task: any;
  taskNotes: string[] = [];  // Store notes for the current task
  newNote: string = '';  // For new note input

  constructor(public modalRef: BsModalRef) {}

  addNote() {
    if (this.newNote.trim()) {
      this.taskNotes.push(this.newNote);
      this.newNote = '';  // Clear the input
    }
  }

  closeModal() {
    this.modalRef.hide();
  }
}
