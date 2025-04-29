from flask import Flask, request, jsonify
import base64, io
from PIL import Image
import pytesseract

app = Flask(__name__)

@app.route('/image', methods=['POST'])
def solve_image():
    data = request.get_json()
    base64_str = data['base64_string']
    image_data = base64.b64decode(base64_str)
    image = Image.open(io.BytesIO(image_data))
    text = pytesseract.image_to_string(image, config='--psm 7 digits')
    try:
        result = str(eval(text.strip()))
    except:
        result = "?"
    return jsonify({"solves": list(result)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
