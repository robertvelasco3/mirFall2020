import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-mission',
  templateUrl: './mission.component.html',
  styleUrls: ['./mission.component.css']
})
export class MissionComponent implements OnInit {

  constructor() { }

  message:string = "";

  ngOnInit() {
  }

  deliver() {
    this.message = "Parts delivering!";
  }

  stopProgram() {
    this.message = "Stopping program..."
  }

}
