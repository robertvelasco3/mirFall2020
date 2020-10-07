import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MirDataComponent } from './mir-data.component';

describe('MirDataComponent', () => {
  let component: MirDataComponent;
  let fixture: ComponentFixture<MirDataComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MirDataComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MirDataComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
