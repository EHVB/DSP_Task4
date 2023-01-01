import numpy as np
import cv2
import matplotlib.pyplot as plt


class Image:
    def __init__(self, filename, filepath, x=0, y=0, w=430, h=287):
        self.filename = filename
        self.filepath = filepath
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def getfft(self):
        img = cv2.imread(self.filepath, 0)
        img_fft = np.fft.fftshift(np.fft.fft2(img))
        return img_fft

    def getmag(self, img_fft):
        img_mag = np.sqrt(np.real(img_fft) ** 2 + np.imag(img_fft) ** 2)
        magpath = (f"static/images/{self.filename}_mag.jpg")
        plt.imsave(magpath,
                   np.log(img_mag+1e-10), cmap='gray')
        return magpath, img_mag

    def getphase(self, img_fft):
        img_phase = np.arctan2(np.imag(img_fft), np.real(img_fft))
        phasepath = (f"static/images/{self.filename}_phase.jpg")
        plt.imsave(phasepath, img_phase, cmap='gray')
        return phasepath, img_phase

    def crop_pos(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def crop_low(self, mode, img_mag, img_phase):
        h_ratio = 61/41
        w_ratio = 64/43
        mag_mask = np.ones((img_mag.shape[0], img_mag.shape[1]))
        phase_mask = np.zeros((img_mag.shape[0], img_mag.shape[1]))
        print('entered low')

        if mode == 'mag':
            for i in range(int(self.y*h_ratio), (int((self.y+self.h)*h_ratio))):
                for j in range(int(self.x*w_ratio), (int((self.x+self.w)*w_ratio))):
                    # print(i,j)
                    mag_mask[i][j] = img_mag[i][j]
        elif mode == 'phase':
            for i in range(int(self.y*h_ratio), (int((self.y+self.h)*h_ratio))):
                for j in range(int(self.x*w_ratio), (int((self.x+self.w)*w_ratio))):
                    # print(i,j)
                    phase_mask[i][j] = img_phase[i][j]
        

        if mode == 'mag':
            return mag_mask
        elif mode == 'phase':
            return phase_mask

    def crop_high(self, mode, img_mag, img_phase):
        h_ratio = 61/41
        w_ratio = 64/43
        mag_mask = np.ones((img_mag.shape[0], img_mag.shape[1]))
        phase_mask = np.zeros((img_mag.shape[0], img_mag.shape[1]))

        print('entered HIGH')

        # if mode == 'mag':
        #     for i in range(int(self.y*h_ratio), (int((self.y+self.h)*h_ratio))):
        #         for j in range(int(self.x*w_ratio), (int((self.x+self.w)*w_ratio))):
        #             img_mag[i][j] = mag_mask[i][j]
        # elif mode == 'phase':
        #     for i in range(int(self.y*h_ratio), (int((self.y+self.h)*h_ratio))):
        #         for j in range(int(self.x*w_ratio), (int((self.x+self.w)*w_ratio))):
        #             img_phase[i][j] = phase_mask[i][j]

        if mode == 'mag':
            for i in range(193, 233):
                for j in range(300, 340):
                    img_mag[i][j] = mag_mask[i][j]
        elif mode == 'phase':
            for i in range(193, 233):
                for j in range(300, 340):
                    img_phase[i][j] = phase_mask[i][j]

        if mode == 'mag':
            return img_mag
        elif mode == 'phase':
            return img_phase
