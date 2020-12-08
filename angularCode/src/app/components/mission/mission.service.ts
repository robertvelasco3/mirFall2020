import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpErrorResponse, HttpResponse } from '@angular/common/http';

import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { map } from "rxjs/operators";


@Injectable()
export class MissionService {
    constructor(private http: HttpClient) { }
    ip = "127.0.0.1";
    ip2 = "192.168.1.10";
    getStart() {
        return this.http.get("http://"+this.ip2+":1234/resume", {responseType: "text"});
    }
    getStop() {
        return this.http.get("http://"+this.ip2+":1234/pause", {responseType: "text"});
    }
    getSafe() {
        return this.http.get("http://"+this.ip2+":1234/safe", {responseType: "text"});
    }
    getStatus() {
        return this.http.get("http://"+this.ip2+":1234/status", {responseType: "text"})
        .pipe(
            map(res => res)
          );
    }
}
