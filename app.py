from flask import Flask, render_template, request , session
from PIL import Image
from flask import send_file
import numpy as np
import matplotlib.pyplot as plt
app = Flask(__name__)
app.secret_key = 'Highly secure key // random'
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
        session['image1name'] = secure_filename(image1.filename) # save file 
        session['image1path'] = os.path.join('static/images', session['image1name'] )
        print(session['image1path'] )
        image1.save(session['image1path'])
        mag_path1,phase_path1 = extract_info(session['image1name'],session['image1path'] )
        return (mag_path1) +"|" + phase_path1
    elif request.method=='POST' and request.form['requestinfo']== 'image2':
        image2 = request.files['image2']
        session['image2name'] = secure_filename(image2.filename)       
        print(session['image1path'] )
        session['image2path'] = os.path.join('static/images', session['image2name'])
        print(session['image2path'] ) 
        image2.save(session['image2path'])
        mag_path2,phase_path2 = extract_info(session['image2name'],session['image2path'])
        return (phase_path2) + "|" + mag_path2
    elif request.method=='POST' and request.form['requestinfo']== 'crop1pos': 
        session['x1']=int(float(request.form['x'] ))
        session['y1']=int(float(request.form['y'] ))
        session['w1']=int(float(request.form['w'] ))
        session['h1']=int(float(request.form['h'] ))
        #print(int(float(x)),int(float(y)),int(float(w)),int(float(h)))
        print(session['x1'],session['y1'],session['w1'],session['h1'])
        return("crop pos recieved")
    elif request.method=='POST' and request.form['requestinfo']== 'crop2pos': 
       session['x2']=int(float(request.form['x'] ))
       session['y2']=int(float(request.form['y'] ))
       session['w2']=int(float(request.form['w'] ))
       session['h2']=int(float(request.form['h'] ))
       print(session['x2'],session['y2'],session['w2'],session['h2'])
       # print(int(float(x)),int(float(y)),int(float(w)),int(float(h)))
       return("crop pos2 recieved")
    
    elif request.method=='POST' and request.form['requestinfo']== 'merge': 
        # all session variables are updated to the latest post request 
            print(session['image1name'],session['image2path'],session['x1'],session['y2'])
            img1mode=request.form['img1mode']
            img2mode=request.form['img2mode']
            #mode is either mag'' or 'phase' __ case sensitive 
            # call merge here 
            resultnewpath='static\images\wabefrom.png'

       
            return(resultnewpath)



    else:
        return (render_template('index.html'))

if __name__ == "__main__":
    app.run(debug=True)
