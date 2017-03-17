from flask import Flask, request
from ctocr import extract_pdf
app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def index():
    if 'file' in request.files:
        file = request.files['file']
        extract_pdf(file)
    return file.filename

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5342)
