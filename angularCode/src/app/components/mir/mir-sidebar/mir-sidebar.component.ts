import { Component, OnInit } from '@angular/core';
import { Panel } from '../../../models/Panel'

@Component({
  selector: 'app-mir-sidebar',
  templateUrl: './mir-sidebar.component.html',
  styleUrls: ['./mir-sidebar.component.css']
})
export class MirSidebarComponent implements OnInit {

  panels:Panel[];
  constructor() { }

  LiveMapOn:boolean = true;
  dataOn:boolean = false;

  ngOnInit() {
    this.panels = [
      {
        name:"Live Map",
        isOpen:true
      },
      {
        name:"MiR100 Data",
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
      if(pan.name == "Live Map")
      {
        this.LiveMapOn = pan.isOpen;
      }
      else if(pan.name == "MiR100 Data")
      {
        this.dataOn = pan.isOpen;
      }
    }
  }

}

