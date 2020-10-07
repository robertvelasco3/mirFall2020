import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MirDataDisplayComponent } from './mir-data-display.component';

describe('MirDataDisplayComponent', () => {
  let component: MirDataDisplayComponent;
  let fixture: ComponentFixture<MirDataDisplayComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MirDataDisplayComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MirDataDisplayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
