from flask import Flask, request, jsonify, send_file
import qrcode
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate_qr', methods=['POST'])
def generate_qr_code():
    data = request.get_json()

    if 'link' not in data:
        return jsonify({'error': 'No link provided'}), 400

    link = data['link']

    # Créer un objet QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    # Créer une image QR code
    img = qr.make_image(fill_color="blue", back_color="yellow")

    # Enregistrer l'image dans un buffer mémoire
    img_buffer = io.BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)

    return send_file(img_buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
