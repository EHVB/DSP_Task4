from flask import Flask, render_template, request
from PIL import Image
from flask import send_file
import numpy as np
import matplotlib.pyplot as plt
app = Flask(__name__)
from werkzeug.utils import secure_filename
import os
import cv2

def extract_info(filename,filepath):
    img = cv2.imread(filepath,0)
    img_fft = np.fft.fftshift(np.fft.fft2(img))
    img_amplitude = np.sqrt(np.real(img_fft) ** 2 + np.imag(img_fft) ** 2)
    img_phase = np.arctan2(np.imag(img_fft), np.real(img_fft))
    plt.imsave(f"static/images/{filename}_mag.jpg",np.log(img_amplitude+1e-10), cmap='gray') 
    plt.imsave(f"static/images/{filename}_phase.jpg",img_phase, cmap='gray')
    magpath=(f"static/images/{filename}_mag.jpg")
    phasepath=(f"static/images/{filename}_phase.jpg")
    return magpath,phasepath


@app.route('/', methods=['GET','POST'])
def home():
    if request.method=='POST' and request.form['requestinfo']== 'image1':
        image1 = request.files['image1']
        filename = secure_filename(image1.filename) # save file 
        filepath = os.path.join('static/images', filename);
        image1.save(filepath)
        mag_path,phase_path = extract_info(filename,filepath)
        return (mag_path)
    elif request.method=='POST' and request.form['requestinfo']== 'image2':
        image2 = request.files['image2']
        filename = secure_filename(image2.filename) # save file 
        filepath = os.path.join('static/images', filename);
        image2.save(filepath)
        mag_path,phase_path = extract_info(filename,filepath)
        return (phase_path)
    elif request.method=='POST' and request.form['requestinfo']== 'crop1pos': 
        x=request.form['x'] 
        y=request.form['y']
        w=request.form['w']
        h=request.form['h']
        print(int(float(x)),int(float(y)),int(float(w)),int(float(h)))
        return("crop pos recieved")

    else:
        return (render_template('index.html'))

if __name__ == "__main__":
    app.run(debug=True)
