import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PolicyDetailsModalComponent } from './policy-details-modal.component';

describe('PolicyDetailsModalComponent', () => {
  let component: PolicyDetailsModalComponent;
  let fixture: ComponentFixture<PolicyDetailsModalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PolicyDetailsModalComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PolicyDetailsModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
