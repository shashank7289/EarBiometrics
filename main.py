'''
Created on Jan 6, 2017

@author: shash
'''
from os.path import dirname,realpath
from cv2 import imread,CascadeClassifier
import numpy as np 
from detection.findEars import findEars
from cv2 import cvtColor,COLOR_BGR2GRAY,rectangle, imshow, waitKey


dirPath = dirname(realpath(__file__))    
leftEarCascade = CascadeClassifier(dirPath + '/resources/haarcascade_mcs_leftear.xml') 
rightEarCascade = CascadeClassifier(dirPath + '/resources/haarcascade_mcs_rightear.xml')

if leftEarCascade.empty(): 
    raise IOError('Unable to load the left ear cascade classifier xml file') 
if rightEarCascade.empty(): 
    raise IOError('Unable to load the right ear cascade classifier xml file') 

img = imread('D:/Academics/Projects/MATLAB/Ear Biometrics/Databases/XM2VTS/000_1_l1.jpg')
# img = imread('C:\Users\shash\Desktop\1.jpg')
# gray = cvtColor(img, COLOR_BGR2GRAY)

leftEar = leftEarCascade.detectMultiScale(img, 1.3, 5) 
rightEar = rightEarCascade.detectMultiScale(img, 1.3, 5) 

for (x,y,w,h) in leftEar: 
    rectangle(img, (x,y), (x+w,y+h),(255,0 ,0), 2)
    print leftEar
    
imshow('right ear',img)
waitKey(0)
# findEars(img,leftEarCascade,rightEarCascade)