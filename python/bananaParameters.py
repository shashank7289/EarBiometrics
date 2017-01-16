'''
banana_parameters - function where parameters of banana wavelets are specified

 Usage:
   banana_parameters()
 -------------------------------------------------------------------------'''
from numpy import pi,real
from cv2 import imshow,waitKey
from python import bananaWavelet

def bananaParameters():

    # Parameter Setting
    x = 30; #rows
    y = 30; #columns
    f = 0.28;   #frequency
    a = 16*(pi/8);   #orientation
    c = 0.06;    #curvature
    s = 1.0;    #size
    sigma_x = 0.75;  #scale of Gaussian filter in x direction
    sigma_y = 3;  #scale of Gaussian filter in y direction
    
    #B_bank = cell(1,100);
    
    # Show the Banana Wavelets
    for v in range(0,1):
        for u in range(0,1):
    
            # Create the Banana wavelets
            B_b = bananaWavelet(x, y, f, a, c, s, sigma_x, sigma_y, u, v)
            
            # Show the real part of Banana wavelets
    #         imshow(real(B_b), [])
            
            imshow('bw',real(B_b), [])
            waitKey(1)
    
            #B_bank((v + 1) * u).lvalue = B_b