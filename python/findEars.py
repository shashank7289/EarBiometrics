'''
Created on Jan 6, 2017

@author: shash
'''
from cv2 import rectangle,putText,FONT_HERSHEY_SIMPLEX
from numpy import size
def findEars(img,leftEarCascade,rightEarCascade):
#     gray = cvtColor(img, COLOR_BGR2GRAY)
    
    rightEar = leftEarCascade.detectMultiScale(img, 1.3, 5) 
    leftEar = rightEarCascade.detectMultiScale(img, 1.3, 5) 
    
    if size(leftEar,0) !=0:
        for (x,y,w,h) in leftEar: 
            rectangle(img, (x,y), (x+w,y+h),(255,0 ,0), 3)
            putText(img, 'Left Ear', (10, 30),FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    elif size(rightEar,0) !=0:
        for (x,y,w,h) in rightEar: 
            rectangle(img, (x,y), (x+w,y+h),(255,0 ,0), 3)
            putText(img, 'Right Ear', (10, 30),FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    else:
        putText(img, 'No ear found', (10, 30),FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    return img