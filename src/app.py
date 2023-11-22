from flask import Flask, render_template, request, send_file
from PIL import Image
# from flask_mail import Mail, Message



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

# @app.route('/send_email', methods=['POST'])
# def send_email():
#     msg = Message('Sujet de l\'e-mail', sender='ablodiallo1521@gmail.com', recipients=['ablodiallo1521@gmail.com'])
#     msg.body = 'Corps de l\'e-mail'
#     with app.open_resource('output.pdf') as pdf_attachment:
#         msg.attach('output.pdf', 'application/pdf', pdf_attachment.read())
#     mail.send(msg)  
# mail = Mail(app)
if __name__ == '__main__':
    app.run(debug=True)
