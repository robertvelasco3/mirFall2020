import { Component, OnInit } from '@angular/core';
import  { MissionService } from './mission.service';
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

  ngOnInit() {
  }

  deliver() {
    this.message = "Parts delivering!";
    this.ms.getStart().subscribe(null, null);
    //((data : any) => this.message = data.toString(), (data : any) => this.message = data.toString());
  }

  pauseProgram() {
    this.message = "Pausing program..."
    this.ms.getStop().subscribe(null, null);
  } 


}
