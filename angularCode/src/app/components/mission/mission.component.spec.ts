import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MissionComponent } from './mission.component';
//import { MissionService } from './mission.service';

describe('MissionComponent', () => {
  let component: MissionComponent;
  //let service: MissionService;
  let fixture: ComponentFixture<MissionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MissionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MissionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
