//import { NgModule } from '@angular/core';
//import { BrowserModule } from '@angular/platform-browser';

//import { AppComponent } from './app.component';
//import { CardComponentComponent } from './components/card-component/card-component.component';

//@NgModule({
//  declarations: [AppComponent, CardComponentComponent],
//  imports: [BrowserModule],
//  providers: [],
//  bootstrap: [AppComponent],
//})
//export class AppModule {}

import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { CardComponentComponent } from './components/card-component/card-component.component';

import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    CardComponentComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }





