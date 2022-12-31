from flask import Flask, render_template, request , session
from PIL import Image
from flask import send_file
import numpy as np
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename
import os
import cv2
from ImageClass import Image

app = Flask(__name__)
app.secret_key = 'Highly secure key // random'

# def extract_info(filename,filepath):
#     img = cv2.imread(filepath,0)
#     img_fft = np.fft.fftshift(np.fft.fft2(img))
#     img_amplitude = np.sqrt(np.real(img_fft) ** 2 + np.imag(img_fft) ** 2)
#     img_phase = np.arctan2(np.imag(img_fft), np.real(img_fft))
#     plt.imsave(f"static/images/{filename}_mag.jpg",np.log(img_amplitude+1e-10), cmap='gray') 
#     plt.imsave(f"static/images/{filename}_phase.jpg",img_phase, cmap='gray')
#     magpath=(f"static/images/{filename}_mag.jpg")
#     phasepath=(f"static/images/{filename}_phase.jpg")
#     return magpath,phasepath

def merge(img1mode,img2mode):
    img1_mag = cv2.imread(session['mag_path1'])
    img1_phase = cv2.imread(session['phase_path1'])
    img2_mag = cv2.imread(session['mag_path2'])
    img2_phase = cv2.imread(session['phase_path1'])
    
   
    for x in range (0,img1_mag.shape[0]):
        for y in range(0,img1_mag.shape[1]):
            if (x>=session['x1'] and x<=session['x1']+session['h1'])and(
                y>=session['y1'] and y<=session['y1']+session['w1']):
                pass
            else:
                if img1mode == 'mag':
                    img1_mag[x][y] = 1
                elif img1mode == 'phase':
                    img1_phase[x][y] = 0
    
    for i in range(0,img2_mag.shape[0]):
        for j in range(0,img2_mag.shape[1]):
            if (i>=session['x2'] and i<=session['x2']+session['h2'])and(
                j>=session['y2'] and j<=session['y2']+session['w2']):
                pass 
            else:
                if img2mode == 'mag':
                    img2_mag[i][j] = 1
                elif img2mode == 'phase':
                    img2_phase[i][j] = 0
    
    if img1mode == 'mag' and img2mode == 'phase':
        img = np.multiply(img1_mag, np.exp(1j * img2_phase))
    elif img2mode == 'mag' and img1mode == 'phase':
        img = np.multiply(img2_mag, np.exp(1j * img1_phase))
    
    result = np.real(np.fft.ifft2(np.fft.ifftshift(img)))
    resultPath = 'static/images/result.jpg'
    plt.imsave(resultPath,result,cmap='gray')
    return resultPath


@app.route('/', methods=['GET','POST'])
def home():
    if request.method=='POST' and request.form['requestinfo']== 'image1':
        image1 = request.files['image1']
        session['image1name'] = secure_filename(image1.filename) # save file 
        session['image1path'] = os.path.join('static/images', session['image1name'] )
        print(session['image1path'] )
        image1.save(session['image1path'])
        # mag_path1,phase_path1 = extract_info(session['image1name'],session['image1path'])
        img1 = Image(session['image1name'],session['image1path'])
        img1_fft = img1.getfft()
        mag_path1 = img1.getmag(img1_fft)
        session['mag_path1'] = mag_path1
        phase_path1 = img1.getphase(img1_fft)
        session['phase_path1'] = phase_path1
        
        return (mag_path1) +"|" + phase_path1
    
    
    elif request.method=='POST' and request.form['requestinfo']== 'image2':
        image2 = request.files['image2']
        session['image2name'] = secure_filename(image2.filename)       
        print(session['image1path'] )
        session['image2path'] = os.path.join('static/images', session['image2name'])
        print(session['image2path'] ) 
        image2.save(session['image2path'])
        # mag_path2,phase_path2 = extract_info(session['image2name'],session['image2path'])
        img2 = Image(session['image2name'],session['image2path'])
        img2_fft = img2.getfft()
        mag_path2 = img2.getmag(img2_fft)
        session['mag_path2'] = mag_path2
        phase_path2 = img2.getphase(img2_fft)
        session['phase_path2'] = phase_path2
        
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
            
            resultnewpath= merge(img1mode,img2mode)

       
            return(resultnewpath)



    else:
        return (render_template('index.html'))

if __name__ == "__main__":
    app.run(debug=True)
