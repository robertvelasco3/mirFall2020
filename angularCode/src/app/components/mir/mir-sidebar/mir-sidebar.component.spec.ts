import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MirSidebarComponent } from './mir-sidebar.component';

describe('MirSidebarComponent', () => {
  let component: MirSidebarComponent;
  let fixture: ComponentFixture<MirSidebarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MirSidebarComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MirSidebarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
