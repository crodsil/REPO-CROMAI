# Esteganografia API

Esta é uma aplicação em Python com Flask para fazer esteganografia em imagens. A aplicação é capaz de esconder uma mensagem em uma imagem e também de revelar a mensagem que foi escondida. 

## Instalação

Para instalar a aplicação, é necessário ter o Python 3.x e o pip instalados. Então, execute o seguinte comando para instalar as dependências:

1. Flask: `pip install Flask`
2. PIL (Python Imaging Library): `pip install Pillow`
3. NumPy: `pip install numpy`

## Como executar a aplicação

Para executar a aplicação, basta rodar o seguinte comando onde se encontra o arquivo `app.py`:

`python3 app.py`


## Documentação

A aplicação possui os seguintes endpoints:

### /upload (POST)

Esse endpoint permite que uma imagem com uma mensagem seja enviada para a aplicação. É necessário enviar um arquivo de imagem e uma mensagem no formato de texto.

### /image (GET)

Esse endpoint retorna a última imagem enviada com uma mensagem escondida.

### /reveal (POST)

Esse endpoint permite que a mensagem escondida em uma imagem seja revelada. É necessário enviar o arquivo da imagem.

### / (GET)

Esse endpoint retorna os endpoints disponíveis na aplicação.

## Por que Flask?

O Flask é uma das melhores opções para construir APIs em Python por ser simples e escalável. Ele não impõe uma estruturação rígida no código e é fácil de entender e utilizar. Além disso, a comunidade do Flask é grande e há uma vasta documentação disponível.

## Cases
### Javascript

``` // Exemplo de upload de imagem com mensagem escondida
const imagem = document.querySelector('input[type="file"]').files[0];
const mensagem = 'Mensagem secreta';
const formData = new FormData();
formData.append('imagem', imagem);
formData.append('mensagem', mensagem);
fetch('/upload', { method: 'POST', body: formData })
  .then(response => response.blob())
  .then(imagemComMensagem => {
    const url = URL.createObjectURL(imagemComMensagem);
    document.querySelector('#imagem').src = url;
  });
  
// Exemplo de revelação de mensagem de imagem
const imagem = document.querySelector('input[type="file"]').files[0];
const formData = new FormData();
formData.append('imagem', imagem);
fetch('/reveal', { method: 'POST', body: formData })
  .then(response => response.json())
  .then(data => {
    const mensagem = data.mensagem;
    alert(mensagem);
  });
```

### Python

```
import requests

# Exemplo de upload de imagem com mensagem escondida
url = 'http://localhost:5000/upload'
imagem = open('imagem.png', 'rb')
mensagem = 'Mensagem secreta'
response = requests.post(url, files={'imagem': imagem}, data={'mensagem': mensagem})
imagem_com_mensagem = response.content
with open('imagem_com_mensagem.png', 'wb') as f:
    f.write(imagem_com_mensagem)
    
# Exemplo de revelação de mensagem de imagem
url = 'http://localhost:5000/reveal'
imagem = open('imagem_com_mensagem.png', 'rb')
response = requests.post(url, files={'imagem': imagem})
mensagem = response.json()['mensagem']
print(mensagem)
```

### Curl
```
# Exemplo de upload de imagem com mensagem escondida
curl -X POST -F 'imagem=@imagem.png' -F 'mensagem=Mensagem secreta' http://localhost:5000/upload > imagem_com_mensagem.png

# Exemplo de revelação de mensagem de imagem
curl -X POST -F 'imagem=@imagem_com_mensagem.png' http://localhost:5000/reveal
```







