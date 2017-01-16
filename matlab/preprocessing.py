%preprocessing - function that does the skin detection & edge enhancement
%
% Usage:
%   preprocessing()
%
% -------------------------------------------------------------------------
function preprocessing( )

close all;
clear all;
clc;

img = imread('E:\Academics\Projects\MATLAB\Ear Biometrics\Databases\XM2VTS - Sample\001_1_l1.jpg');

%skin colour...............................................................

%Convert image from RGB to YCBCR colour space
img_ycbcr = rgb2ycbcr(img);
%figure,imshow(img_ycbcr);  %   Display image

%skin texture..............................................................

%Convert from RGB to Gray scale
img_gray = rgb2gray(img);   
figure,subplot(2,2,1), subimage(img_gray);
title('Grayscale Image');

%Enhance the contrast of the grayscale image by using CLAHE
img_clahe = adapthisteq(img_gray);  
subplot(2,2,2), subimage(img_clahe);
title('CLAHE Image');

%Calculate Co-occurrence matrix
glcm = graycomatrix(img_clahe,'NumLevels',255,'GrayLimits',[]); 
%glcm = graycomatrix(img_clahe,'NumLevels',255,'GrayLimits',[],'Offset', [0 1; 0 -1;   -1 1; 1 -1;   -1 0; 1 0;   -1 -1; 1 1]); %
subplot(2,2,3), imshow(glcm);
title('Co-Occurrence Matrix');

%Calculate Inertia of Co-occurrence matrix
inertia = graycoprops(glcm, 'contrast');

%Calculate Energy of Co-occurrence matrix
energy = graycoprops(glcm, 'energy');

end


