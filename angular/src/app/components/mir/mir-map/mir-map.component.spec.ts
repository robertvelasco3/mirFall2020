import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MirMapComponent } from './mir-map.component';

describe('MirMapComponent', () => {
  let component: MirMapComponent;
  let fixture: ComponentFixture<MirMapComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MirMapComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MirMapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
