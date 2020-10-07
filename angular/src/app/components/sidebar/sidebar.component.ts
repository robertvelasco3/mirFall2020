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
  dataOn:boolean = false;
  equipOn:boolean = false;
  projectOn:boolean = false;
  teamOn:boolean = false;
  contactOn:boolean = false;
  mirOn:boolean = false;

  ngOnInit() {
    this.panels = [
      {
        name:"Home",
        isOpen:false
      },
      {
        name:"Data",
        isOpen:false
      },
      {
        name:"Equipment",
        isOpen:true
      },
      {
        name:"Projects",
        isOpen:false
      },
      {
        name:"Team",
        isOpen:false
      },
      {
        name:"Contact Info",
        isOpen:false
      },
      {
        name:"MiR100",
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
      else if(pan.name == "Data")
      {
        this.dataOn = pan.isOpen;
      }
      else if(pan.name == "Equipment")
      {
        this.equipOn = pan.isOpen;
      }
      else if(pan.name == "Projects")
      {
        this.projectOn = pan.isOpen;
      }
      else if(pan.name == "Team")
      {
        this.teamOn = pan.isOpen;
      }
      else if(pan.name == "Contact Info")
      {
        this.contactOn = pan.isOpen;
      }
      else if(pan.name == "MiR100")
      {
        this.mirOn = pan.isOpen;
      }
    }

  }

}
