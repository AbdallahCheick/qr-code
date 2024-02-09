from flask import Flask, request, jsonify, send_file
import segno

app = Flask(__name__)

@app.route('/generate_qrcode', methods=['POST'])
def generate_qr_code():
    data = request.get_json()

    if 'link' not in data:
        return jsonify({'error': 'No link provided'}), 400

    link = data['link']

    # Générer le code QR avec l'image insérée
    qrcode = segno.make(link, error='h')
    qrcode.to_artistic(background='nanawax.png', target='output.png', scale=5)  
    # Enregistrer l'image dans un buffer mémoire
    img_buffer = open('output.png', 'rb')

    return send_file(img_buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
