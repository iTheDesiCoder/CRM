import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { provideHttpClient  } from '@angular/common/http';
import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { TaskListComponent } from './task-list/task-list.component';
import { TaskDetailsModalComponent } from './task-details-modal/task-details-modal.component';
import { PolicyDetailsModalComponent } from './policy-details-modal/policy-details-modal.component';
import { NgxDatatableModule } from '@swimlane/ngx-datatable';
import { ModalModule,BsModalService } from 'ngx-bootstrap/modal';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';


@NgModule({
  declarations: [
    AppComponent,
    TaskListComponent,
    TaskDetailsModalComponent,
    PolicyDetailsModalComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgxDatatableModule,
    ModalModule.forRoot(),
    FormsModule,
    CommonModule  
  ],
  providers: [provideHttpClient() ,BsModalService],
  bootstrap: [AppComponent]  // Bootstrap the app using AppComponent
})
export class AppModule {}
