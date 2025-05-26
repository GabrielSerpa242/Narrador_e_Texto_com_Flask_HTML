from flask import Flask, request, send_file
from gtts import gTTS
from flask_cors import CORS
import io

app = Flask(__name__)
CORS(app)
@app.route('/gerar-audio', methods=['POST'])
def gerar_audio():
    data = request.json
    texto = data.get('texto', '')
    if not texto:
        return {"error": "Texto não fornecido"}, 400
    
    tts = gTTS(text=texto, lang='pt-br')
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    
    return send_file(mp3_fp, mimetype="audio/mpeg", as_attachment=True, download_name="narracao.mp3")

if __name__ == '__main__':
    app.run(debug=True)