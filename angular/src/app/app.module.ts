import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { EquipmentPageComponent } from './components/equipment-page/equipment-page.component';
import { HeaderComponent } from './components/header/header.component';
import { ProjectPageComponent } from './components/project-page/project-page.component';
import { DataPageComponent } from './components/data-page/data-page.component';
import { ContactInfoPageComponent } from './components/contact-info-page/contact-info-page.component';
import { TeamPageComponent } from './components/team-page/team-page.component';
import { HomePageComponent } from './components/home-page/home-page.component';
import { MirDataComponent } from './components/mir-data/mir-data.component';
import { MirSidebarComponent } from './components/mir/mir-sidebar/mir-sidebar.component';
import { MirMapComponent } from './components/mir/mir-map/mir-map.component';
import { MirDataDisplayComponent } from './components/mir/mir-data-display/mir-data-display.component';

@NgModule({
  declarations: [
    AppComponent,
    SidebarComponent,
    EquipmentPageComponent,
    HeaderComponent,
    ProjectPageComponent,
    DataPageComponent,
    ContactInfoPageComponent,
    TeamPageComponent,
    HomePageComponent,
    MirDataComponent,
    MirSidebarComponent,
    MirMapComponent,
    MirDataDisplayComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
