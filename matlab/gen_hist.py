function gen_hist()

%conv_gen_hist - function that convolves banana wavelets with the ear image
%
%Usage:
%  gen_hist()
%-------------------------------------------------------------------------

close all;
clear all;
clc;

%Preallocation

ear_img = zeros(120,80,252);    %ear images
bw = zeros(30,30,80);           %banana wavelet
conv_img = zeros(91,51);        %convolution result
hist = zeros(256,1);            %histogram


%reading ear images from the folder
ear_folder = 'H:\MATLAB\Ear Biometrics\Databases\XM2VTS (Recognition)';
ear_filePattern = fullfile(ear_folder, '*.jpg');
ear_jpegFiles = dir(ear_filePattern);
for ear_counter = 1:20%length(ear_jpegFiles)    
    ear_baseFileName = ear_jpegFiles(ear_counter).name;
    ear_fullFileName = fullfile(ear_folder, ear_baseFileName);
    ear_img(:,:,ear_counter) = rgb2gray(im2double(imread(ear_fullFileName)));
    
    %subplot(2,2,1), imshow(ear_img(:,:,ear_counter));
    
    %reading banana wavelets from the folder
    bw_folder = 'H:\MATLAB\Ear Biometrics\Wavelet Images\Wavelet Images (Recognition)';
    bw_filePattern = fullfile(bw_folder, '*.jpg');
    bw_jpegFiles = dir(bw_filePattern);
    for bw_counter = 81:length(bw_jpegFiles)    
        bw_baseFileName = bw_jpegFiles(bw_counter).name;
        bw_fullFileName = fullfile(bw_folder, bw_baseFileName);
        bw(:,:,bw_counter) = rgb2gray(im2double(imread(bw_fullFileName)));        
        %subplot(2,2,2), imshow(bw(:,:,bw_counter));
        
        %performing convolution of banana wavelets with ear image
        conv_img(:,:) = mat2gray(conv2(double(ear_img(:,:,ear_counter)), double(bw(:,:,bw_counter)),'valid'));
        
        %saving the convolved image
        outputFileName = sprintf('ConvImg_%d_%d.jpg',ear_counter,bw_counter);
        imwrite(conv_img, outputFileName);
        
        %calculating histogram for convolved ear image
        %hist(:,:) = imhist((conv_img(:,:)), 256);
        %subplot(2,2,4), imhist((conv_img(:,:)), 256);
        %drawnow;
        
        %saving the histogram
%         eval(sprintf('save(''hist_%d_0%d.mat'',''hist'');',ear_counter,bw_counter));
    end
end
end