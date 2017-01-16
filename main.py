'''
Created on Jan 6, 2017

@author: shash
'''
from os.path import dirname,realpath
from cv2 import imread,CascadeClassifier,VideoCapture,imshow,waitKey
from python import findEars.findEars
from bananaWavelets.bananaParameters import bananaParameters

dirPath = dirname(realpath(__file__))    
leftEarCascade = CascadeClassifier(dirPath + '/resources/haarcascade_mcs_leftear.xml') 
rightEarCascade = CascadeClassifier(dirPath + '/resources/haarcascade_mcs_rightear.xml')

if leftEarCascade.empty(): 
    raise IOError('Unable to load the left ear cascade classifier xml file') 
if rightEarCascade.empty(): 
    raise IOError('Unable to load the right ear cascade classifier xml file') 
 
# img = imread('D:/Academics/Projects/MATLAB/Ear Biometrics/Databases/XM2VTS/000_1_l1.jpg')
# cap = VideoCapture(0)
# while True:
#     ret,img = cap.read()
# 
#     img = findEars(img,leftEarCascade,rightEarCascade)
#     imshow('output',img)
#     waitKey(1)
    
bananaParameters()
    