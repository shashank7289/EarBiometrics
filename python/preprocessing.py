'''
Created on Jan 16, 2017

@author: uid38420
'''
#preprocessing - function that does the skin detection & edge enhancement
#
# Usage:
#   preprocessing(img)
# -------------------------------------------------------------------------
    
from numpy import array,arange
from cv2 import imshow,waitKey,filter2D,equalizeHist,createCLAHE,LUT,Laplacian,CV_64F
from cv2 import cvtColor,COLOR_BGR2YUV,COLOR_YUV2BGR

def histogramEqualization(img):
    imgYUV = cvtColor(img, COLOR_BGR2YUV)
    imgYUV[:,:,0] = equalizeHist(imgYUV[:,:,0])
    adjusted = cvtColor(imgYUV, COLOR_YUV2BGR)
    return adjusted
 
def clahe(img):
    imgYUV = cvtColor(img, COLOR_BGR2YUV)
    clahe = createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    imgYUV[:,:,0] = clahe.apply(imgYUV[:,:,0])
    adjusted = cvtColor(imgYUV, COLOR_YUV2BGR)
    return adjusted
 
def gammaCorrection(img, gamma):
    # build a lookup table mapping pixel values [0, 255] to their adjusted gamma values
    invGamma = 1.0 / gamma
    table = array([((i / 255.0) ** invGamma) * 255
        for i in arange(0, 256)]).astype("uint8")
    
    # apply gamma correction using the lookup table
    imgYUV = cvtColor(img, COLOR_BGR2YUV)
    imgYUV[:,:,0] = LUT(imgYUV[:,:,0],table)
    adjusted = cvtColor(imgYUV, COLOR_YUV2BGR)
    return adjusted

def gicClahe(img,gamma):
    cl = clahe(img)
    adjusted = gammaCorrection(cl, gamma)
    return adjusted

def blurDetect(img):
    # compute the Laplacian and return focus measure (variance of Laplacian)
    blur = Laplacian(img, CV_64F).var()
    return blur

def blurRemove(img):
    blur = blurDetect(img)
    if blur > 100:
        pass
    elif blur < 100 and blur >= 20:
        #Sharpening
        kernelSharpen = array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        adjusted = filter2D(img, -1, kernelSharpen)
    elif blur < 20 and blur >= 0:
        #Edge Enhancement
        kernelSharpen = array([[-1,-1,-1,-1,-1],
                               [-1, 2, 2, 2,-1],
                               [-1, 2, 8, 2,-1],
                               [-1, 2, 2, 2,-1],
                               [-1,-1,-1,-1,-1]])/8.0
        adjusted = filter2D(img, -1, kernelSharpen)
#     imshow("res", adjusted)
#     waitKey(0)
    return adjusted