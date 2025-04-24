from flask import Flask, render_template, send_file, request, jsonify
import os
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('webcam.html')

@app.route('/capture', methods=['POST'])
def capture_image():
    try:
        data_url = request.json['image']
        img_data = base64.b64decode(data_url.split(',')[1])
        img_io = BytesIO(img_data)
        img_io.seek(0)
        return send_file(
            img_io,
            mimetype='image/png',
            as_attachment=True,
            download_name=f'captured_image_{request.json["timestamp"]}.png'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
