class Functions:
    def getfft( filepath):
      img = cv2.imread(filepath, 0)
      img_fft = np.fft.fftshift(np.fft.fft2(img))
      return img_fft


    def getmag(filename,img_fft):
        img_amplitude = np.sqrt(np.real(img_fft)** 2 + np.imag(img_fft) ** 2)
        magpath = (f"static/images/{filename}_mag.jpg")
        plt.imsave(magpath ,
                   np.log(img_amplitude+1e-10), cmap='gray')
        return magpath

    def getphase(filename,img_fft):
        img_phase = np.arctan2(np.imag(img_fft), np.real(img_fft))
        phasepath = (f"static/images/{filename}_phase.jpg")
        plt.imsave(phasepath, img_phase, cmap='gray')
        return phasepath





    # def extract_info(filename,filepath):
    # img = cv2.imread(filepath,0)
    # img_fft = np.fft.fftshift(np.fft.fft2(img))
    # img_amplitude = np.sqrt(np.real(img_fft) ** 2 + np.imag(img_fft) ** 2)
    # img_phase = np.arctan2(np.imag(img_fft), np.real(img_fft))
    # plt.imsave(f"static/images/{filename}_mag.jpg",np.log(img_amplitude+1e-10), cmap='gray') 
    # plt.imsave(f"static/images/{filename}_phase.jpg",img_phase, cmap='gray')
    # magpath=(f"static/images/{filename}_mag.jpg")
    # phasepath=(f"static/images/{filename}_phase.jpg")
    # return magpath,phasepath