import { Component, OnInit } from '@angular/core';
import { Panel } from '../../models/Panel'
import { AppComponent } from '../../app.component';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {
  panels:Panel[];
  constructor() { }

  homeOn:boolean = true;
  projectOn:boolean = false;
  missionOn:boolean = false;
  teamOn:boolean = false;

  ngOnInit() {
    this.panels = [
      {
        name:"Home",
        isOpen:false
      },
      {
        name:"Project",
        isOpen:false
      },
      {
        name:"Mission",
        isOpen:true
      },
      {
        name:"Team",
        isOpen:false
      }
    ]
  }

  selectPanel(panelName:string) {
    for(var pan of this.panels)
    {
      if(pan.name == panelName)
      {
        pan.isOpen = true;
      }
      else
      {
        pan.isOpen = false;
      }
      if(pan.name == "Home")
      {
        this.homeOn = pan.isOpen;
      }
      else if(pan.name == "Project")
      {
        this.projectOn = pan.isOpen;
      }
      else if(pan.name == "Mission")
      {
        this.missionOn = pan.isOpen;
      }
      else if(pan.name == "Team")
      {
        this.teamOn = pan.isOpen;
      }
    }

  }

}
