import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm # kjižnica barvnih lestvic
from PIL import Image
import scipy.signal as sig

#%% funkcije


def showImage(iImage,iTitle=''):
    #plt.figure()
    plt.imshow(iImage, cmap = cm.Greys_r) # brez cmap vrne v osnovi sivinsko sliko s RGB barvami
    plt.suptitle(iTitle)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axes().set_aspect('equal','datalim') # x in y sta enakovredni, x in y imata isto merilo
    plt.show()


def loadImage(iPath):
    img = Image.open(iPath)
    a = np.array(img)
    #plt.imshow(a)
    #plt.show()
    return a


    # shranjujemo različne formate
def saveImage( iPath, iImage, iFormat ):
    xImage = Image.fromarray(iImage)
    xImage.save(iPath+'.'+iFormat)
    
def colorToGrey(iImage):
    iImageType = iImage.dtype
    rgb = np.array(iImage,dtype= 'float')
    return (rgb[:,:,0]*0.299 + rgb[:,:,1]*0.587 + rgb[:,:,2]*0.114).astype(iImageType)


#%%
def meraChetkosti(g):
    ft = np.fft.fft2(g)
    cft = np.fft.fftshift(ft)
    aft = np.abs(cft)
    M = aft.max()
    Th = np.sum(aft > M/1000)
    FM = Th/np.prod(ft.shape)
    return FM

#%%
def main():
    a = loadImage('/home/mary/Documents/coding/slika.jpg')
    g = colorToGrey(a)
    plt.imshow(g, cmap = cm.Greys_r)
    blur = sig.convolve2d(g, np.ones((5,5))/25)
    meraChetkosti(blur)

if __name__=='__main__':
    main()

#https://www.sciencedirect.com/science/article/pii/S1877705813016007
