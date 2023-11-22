from flask import Flask, render_template, request, send_file
from PIL import Image



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'image' in request.files:
        image = request.files['image']
        #  Traitement de l'image (conversion en PDF)
        img = Image.open(image)
        pdf_path = 'output.pdf'
        img.save(pdf_path, 'PDF')
        # Envoi du PDF en téléchargement
        return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
