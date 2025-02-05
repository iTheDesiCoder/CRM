import { Component, Input } from '@angular/core';
import { BsModalRef } from 'ngx-bootstrap/modal';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-policy-details-modal',
  templateUrl: './policy-details-modal.component.html',
  styleUrls: ['./policy-details-modal.component.scss'],
  standalone:false
})
export class PolicyDetailsModalComponent {
  @Input() policy: any;

  constructor(public modalRef: BsModalRef) {}

  closeModal() {
    this.modalRef.hide();
  }
}
