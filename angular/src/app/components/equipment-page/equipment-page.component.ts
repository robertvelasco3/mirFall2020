import { Component, OnInit } from '@angular/core';
import {Equipment } from "../../models/Equipment"
import { hasMagic } from 'glob';

@Component({
  selector: 'app-equipment-page',
  templateUrl: './equipment-page.component.html',
  styleUrls: ['./equipment-page.component.css']
})
export class EquipmentPageComponent implements OnInit {
  sampleEquipment:Equipment[];
  constructor() { }

  ngOnInit() {
    this.sampleEquipment = [
      {
        id: 1,
        name: "Haas",
        isRunning: false
      },
      {
        id: 2,
        name: "MiR",
        isRunning: false
      },
      {
        id: 3,
        name: "Rize",
        isRunning: false
      }
    ]
  }

}
