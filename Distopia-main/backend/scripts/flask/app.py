from flask import Flask, request, jsonify, send_file,url_for
from msn_reveal import revelar_mensagem
from msn_send import esconder_mensagem
from home import init
import uuid
from PIL import Image
import numpy as np
import io
import os

app = Flask(__name__)
app.config['STATIC_FOLDER'] = os.path.abspath("static")
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'downloadImages')


@app.route('/upload', methods=['POST'])
def upload():
    imagem = Image.open(request.files['imagem'])
    mensagem = request.form['mensagem']
    nome_imagem = str(uuid.uuid4())[:3] + ".png" 
    imagem_com_mensagem = esconder_mensagem(imagem, mensagem)
    imagem_com_mensagem.save(os.path.join(app.config['UPLOAD_FOLDER'], nome_imagem))
    return send_file(imagem_com_mensagem, mimetype='image/png')


@app.route('/image', methods=['GET'])
def image():
    filenames = os.listdir(app.config['UPLOAD_FOLDER'])
    if not filenames:
        return jsonify({'error': 'Au au! Nenhuma imagem encontrada.'}), 404

    images_html = ""
    for filename in filenames:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        images_html += f"<li><img src='{url_for('static', filename=filename)}'></li>"
    
    return f"<ul>{images_html}</ul>"



@app.route('/reveal', methods=['POST'])
def reveal():
    imagem = Image.open(request.files['imagem'])
    mensagem = revelar_mensagem(imagem)
    if mensagem == '':
        return jsonify({'error': 'Au au! Nenhuma mensagem encontrada.'}), 404
    return jsonify({'mensagem': mensagem})



@app.route('/')
def menu():
    return init()

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)




if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
