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
    
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Adiciona os dados ao QRCode
    qr.add_data(texto_do_usuario)
    qr.make(fit=True)

    # Cria uma imagem QRCode
    img_qrcode = qr.make_image(fill_color=f"#000000", back_color="#ffffff")
    img_qrcode = img_qrcode.convert('RGB')
    img_qrcode = np.array(img_qrcode)
    img_qrcode = cv.cvtColor(img_qrcode,cv.COLOR_RGB2BGR)
    
    retval, buffer = cv.imencode('.png', img_qrcode)
    buffer64 = base64.b64encode(buffer)  
    string64 = buffer64.decode('utf-8')
    
    return render_template('imagem.html',imagem_base64=string64,nome_arq=nome_arquivo)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
