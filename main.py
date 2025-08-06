
from flask import Flask, render_template, request, send_file, make_response, jsonify
from flask_cors import CORS
import base64
import json
import io
import os

PORT = 5002

from morse import Morse

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdfsdafdsafdas'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/foo": {"origins": f"http://localhost:{PORT}"}})

CORS(app)
morse = Morse()


@app.route("/")
def index():
    return render_template("home.html")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    json_data = json.loads(request.get_data().decode("utf-8"))
    plaintext = json_data["plaintext"]
    ciphertext = morse.convert_text_to_morse(plaintext)
    return {"ciphertext":ciphertext}

@app.route("/decrypt", methods=["POST"])
def decrypt():
    json_data = json.loads(request.get_data().decode("utf-8"))
    ciphertext = json_data["ciphertext"]
    plaintext = morse.convert_morse_to_text(ciphertext)
    return {"plaintext":plaintext}

@app.route("/sound", methods=["POST"])
def sound():
    json_data = json.loads(request.get_data().decode("utf-8"))
    ciphertext = json_data["ciphertext"]
    sound = morse.convert_morse_to_sound(ciphertext)
    
    buffer = io.BytesIO()
    sound.export(buffer, format="mp3")
    buffer.seek(0)

    return send_file(buffer, mimetype="audio/mp3", as_attachment=False, download_name="sound.mp3") 



if __name__ == "__main__":
    app.run(debug=True, port=PORT, host=os.environ.get('HOST_URL'))
