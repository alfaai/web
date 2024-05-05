from flask import Flask, render_template, request, send_file
from inference import sticker, pulid
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOADS_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "uploads")
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'webp'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/sticker', methods=['GET', 'POST'])
def sticker_endpoint():
    if request.method == 'POST':
        prompt = request.form['prompt']
        img_link = sticker(prompt)
        return render_template('sticker.html', img=img_link)
    return render_template('sticker.html')


@app.route('/pulid', methods=['GET', 'POST'])
def pulid_endpoint():
    if request.method == 'POST':
        prompt = request.form['prompt']
        file = request.files['img']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOADS_PATH, filename))

            img_link = pulid(open(os.path.join(UPLOADS_PATH, filename), "rb"), prompt)
            os.remove(os.path.join(UPLOADS_PATH, filename))
            return render_template('pulid.html', img=img_link)
    else:
        return render_template('pulid.html')
