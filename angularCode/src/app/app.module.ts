import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { HeaderComponent } from './components/header/header.component';
import { ProjectPageComponent } from './components/project-page/project-page.component';
import { ContactInfoPageComponent } from './components/contact-info-page/contact-info-page.component';
import { TeamPageComponent } from './components/team-page/team-page.component';
import { HomePageComponent } from './components/home-page/home-page.component';
import { MirDataComponent } from './components/mir-data/mir-data.component';
import { MissionComponent } from './components/mission/mission.component';

@NgModule({
  declarations: [
    AppComponent,
    SidebarComponent,
    HeaderComponent,
    ProjectPageComponent,
    ContactInfoPageComponent,
    TeamPageComponent,
    HomePageComponent,
    MirDataComponent,
    MissionComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
