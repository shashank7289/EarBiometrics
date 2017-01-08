'''
Created on Jan 6, 2017

@author: shash
'''
from cv2 import cvtColor,COLOR_BGR2GRAY,rectangle, imshow, waitKey

def findEars(img,leftEarCascade,rightEarCascade):
    gray = cvtColor(img, COLOR_BGR2GRAY)
    
    leftEar = leftEarCascade.detectMultiScale(gray, 1.3, 5) 
    rightEar = rightEarCascade.detectMultiScale(gray, 1.3, 5) 
    
    for (x,y,w,h) in rightEar: 
        rectangle(img, (x,y), (x+w,y+h),(255,0 ,0), 3)
        
    imshow('right ear',gray)
    waitKey(0)