from flask import Flask, render_template, request
import qrcode
import base64
import cv2 as cv
import numpy as np
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar_formulario', methods=['POST'])
def processar_formulario():
    # Obtém o texto do formulário enviado pelo usuário
    texto_do_usuario = request.form['texto_usuario']
    nome_arquivo = request.form['arquivo']

    qr = qrcode.QRCode()

    # Adiciona os dados ao QRCode
    qr.add_data(texto_do_usuario)
    # qr.make(fit=True)

    # Cria uma imagem QRCode
    img_qrcode = qr.make_image(fill_color="green", back_color="white")

    img_qrcode = np.array(img_qrcode)
    
    retval, buffer = cv.imencode('.png', img_qrcode)
    buffer64 = base64.b64encode(buffer)
    
    
    string64 = buffer64.decode('ascii')
    
    
    
    
    # buffer = base64.b64decode(string64.replace('data:image/png;base64,', ''))

    
    # imgArray = np.frombuffer(buffer, np.int8)
    # img = cv.imdecode(imgArray, cv.IMREAD_UNCHANGED)
    
    return render_template('imagem.html',imagem_base64=string64,nome_arq=nome_arquivo)
