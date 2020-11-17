import { Component, OnInit } from '@angular/core';
import  { MissionService } from './mission.service';
import {interval} from "rxjs/internal/observable/interval";
import {startWith, switchMap} from "rxjs/operators";
import { HttpResponse } from '@angular/common/http';

@Component({
  selector: 'app-mission',
  templateUrl: './mission.component.html',
  providers: [ MissionService ],
  styleUrls: ['./mission.component.css']
})
export class MissionComponent implements OnInit {

  constructor(private ms : MissionService) { }

  message:string = "";
  status:string = "";

  ngOnInit() {
    this.message = "Welcome to mission control! Click Deliver to start.";
    interval(5000)
      .pipe(
        startWith(0),
        switchMap(() => this.ms.getStatus())
      )
      .subscribe(res => {this.status = res})
    ;
  }

  deliver() {
    this.message = "Parts delivering!";
    this.ms.getStart().subscribe(results => {this.message = results;}, null);
  }

  pauseProgram() {
    this.message = "Pausing program..."
    this.ms.getStop().subscribe(results => {this.message = results;}, null);
    this.message
  } 

  
  resumeSafety() {
    this.message = "Resuming from safety..."
    this.ms.getSafe().subscribe(results => {this.message = results;}, null);
    this.message
  } 

}
