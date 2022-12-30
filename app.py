from flask import Flask, render_template, request
from PIL import Image
from flask import send_file
app = Flask(__name__)
from werkzeug.utils import secure_filename
import os
import cv2


@app.route('/', methods=['GET','POST'])
def home():
    if request.method=='POST' and request.form['requestinfo']== 'image1':
        image1 = request.files['image1']
        filename = secure_filename(image1.filename) # save file 
        filepath = os.path.join('static/images', filename);
        image1.save(filepath)
        cv2.imread(filepath)
        # do processing here 
        # /////
        magpath=r"static\images\img2.jpg"  # should be replaced by your path for mag
        return (magpath)
    else:
        return (render_template('index.html'))

if __name__ == "__main__":
    app.run(debug=True)
