import numpy as np
import cv2
import matplotlib.pyplot as plt

class Image:
    def __init__(self, filename, filepath):
        self.filename=filename
        self.filepath=filepath

    def getfft( self):
      img = cv2.imread(self.filepath, 0)
      img_fft = np.fft.fftshift(np.fft.fft2(img))
      return img_fft


    def getmag(self,img_fft):
        img_amplitude = np.sqrt(np.real(img_fft)** 2 + np.imag(img_fft) ** 2)
        magpath = (f"static/images/{self.filename}_mag.jpg")
        plt.imsave(magpath ,
                   np.log(img_amplitude+1e-10), cmap='gray')
        return magpath,img_amplitude

    def getphase(self,img_fft):
        img_phase = np.arctan2(np.imag(img_fft), np.real(img_fft))
        phasepath = (f"static/images/{self.filename}_phase.jpg")
        plt.imsave(phasepath, img_phase, cmap='gray')
        return phasepath,img_phase

