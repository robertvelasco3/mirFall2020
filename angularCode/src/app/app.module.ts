import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { HeaderComponent } from './components/header/header.component';
import { ProjectPageComponent } from './components/project-page/project-page.component';
import { TeamPageComponent } from './components/team-page/team-page.component';
import { HomePageComponent } from './components/home-page/home-page.component';
import { MissionComponent } from './components/mission/mission.component';

@NgModule({
  declarations: [
    AppComponent,
    SidebarComponent,
    HeaderComponent,
    ProjectPageComponent,
    TeamPageComponent,
    HomePageComponent,
    MissionComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
