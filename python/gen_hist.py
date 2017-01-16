'''conv_gen_hist - convolve banana wavelets with the ear image

Usage:
  gen_hist()
-------------------------------------------------------------------------'''

from numpy import zeros,size,convolve
from scipy.io import loadmat,savemat
from cv2 import imwrite, calcHist
from glob import glob

def genHist(img):

    #Preallocation
    img = zeros((120, 80, 252))#ear images
    bw = zeros((30, 30, 80))#banana wavelet
    convImg = zeros((90, 50))#convolution result
    hist = zeros((256, 1))#histogram
        
        #reading banana wavelets from the folder
    bwDatabase = 'D:/Codes/Python/Ear Biometrics/Wavelet Images/Wavelet Images (Recognition)/*jpg'
    bwName = glob(bwDatabase)
    for fn in bwName:
        bw = loadmat(fn)

        #performing convolution of banana wavelets with ear image
        convImg = convolve(img, bw, 'valid')

        #saving the convolved image
        outputFileName = 'ConvImg_' + bwName + '.jpg'
        imwrite(convImg, outputFileName)

        #calculating histogram of convolved image
        hist = calcHist(convImg,[0],None,[256],[0,256])
        
        #saving the histogram
        savemat('hist_'+bwName, hist, True)