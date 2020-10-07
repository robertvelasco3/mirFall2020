import { Component, OnInit } from '@angular/core';
import { Project } from '../../models/Project'

@Component({
  selector: 'app-project-page',
  templateUrl: './project-page.component.html',
  styleUrls: ['./project-page.component.css']
})
export class ProjectPageComponent implements OnInit {
  projects:Project[];
  constructor() { }

  ngOnInit() {
    this.projects = [
      {
        id: "LF19-01",
        name: ""
      },
      {
        id: "LF19-02",
        name: "Mobile Robotics Solutions in Mfg"
      },
      {
        id: "LF19-03",
        name: ""
      },
      {
        id: "LF19-04",
        name: ""
      },
      {
        id: "LF19-05",
        name: ""
      },
      {
        id: "LF19-06",
        name: ""
      },
      {
        id: "LF19-07",
        name: ""
      },
      {
        id: "LF19-08",
        name: ""
      },
      {
        id: "LF19-09",
        name: ""
      },
      {
        id: "LF19-10",
        name: ""
      }

    ];
  }

}
