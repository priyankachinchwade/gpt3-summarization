import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Injectable } from '@angular/core';
import {HttpClient, HttpParams, HttpRequest, HttpEvent,HttpEventType} from '@angular/common/http';
import {MatIconModule} from '@angular/material/icon';


@Component({
  selector: 'summarization',
  templateUrl: './app.summarization.html',
  styleUrls: ['./app.component.css']
})
export class AppSummarizationComponent {
  
  fileName = '';

  constructor(private http: HttpClient) {}

  onFileSelected(event: any) {

      const file:File = event.target.files[0];

      if (file) {

          this.fileName = file.name;
          
          const formData = new FormData();

          formData.append("file", file);
          //var option = {'Content-Length' : msg.length, 'Content-Type': 'plain/text', 'body' : msg};

          const upload$ = this.http.post("http://127.0.0.1:5000/upload", formData);

          upload$.subscribe();
      }

  
}

}