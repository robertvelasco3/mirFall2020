import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpErrorResponse, HttpResponse } from '@angular/common/http';

import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

@Injectable()
export class MissionService {
    constructor(private http: HttpClient) { }
    getStart() {
        return this.http.get("http://192.168.1.8:1234/resume", {responseType: "text"});//,{
        //    responseType:'text'});
        
    }
    getStop() {
        return this.http.get("http://192.168.1.8:1234/pause", {responseType: "text"});//,{
        //    responseType:'text'});
    }
}