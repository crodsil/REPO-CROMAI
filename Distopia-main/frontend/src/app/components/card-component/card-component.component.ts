import { Component, OnInit } from '@angular/core';
import Swiper, { SwiperOptions } from 'swiper';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-card-component',
  templateUrl: './card-component.component.html',
  styleUrls: ['./card-component.component.css']
})
export class CardComponentComponent implements OnInit {
  capturando = '';
  swiperContainer: any;
  public textareaValue!: string;
  i: number = 0;

  constructor(private http: HttpClient) {  
  }
  
  ngOnInit(): void {
    const swiperOptions: SwiperOptions = {
      slidesPerView: 3,
      spaceBetween: 30,
      slidesPerGroup: 3,
      loop: true,
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
    };
    const swiper = new Swiper(".mySwiper", swiperOptions);
  }

  capturar(event: Event) {
    this.capturando = (event.target as HTMLTextAreaElement).value;
  }

  enviar(event: any): void {
    event.preventDefault();

    const url = 'http://127.0.0.1:5000/upload';
    const formData = new FormData(document.getElementById(`card-${this.i}`) as HTMLFormElement);
    
    // Adicionar a imagem ao formulário
    const imageUrl = 'assets/Timyn.jpg' ;
    
    fetch(imageUrl)
      .then(response => response.blob())
      .then(blob => {
        const file = new File([blob], 'Timyn.jpg',  { type: 'image/jpeg' });
        formData.append('imagem', file);
        
        // Adicionar o texto ao formulário
        formData.append('mensagem', this.capturando);
        
        // Enviar a requisição POST
        this.http.post(url, formData).subscribe(response => {
          console.log(response);       
        }); 
      })
      .catch(error => {
        console.error(error);
      });

      this.textareaValue = '';
  }

}
