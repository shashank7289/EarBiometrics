function recognition()
%recognition - function that compares a query image with a database image to give
%the recognition result
%
%Usage:
%  recognition()
%--------------------------------------------------------------------------

close all;
clear all;
clc;

%preallocation-------------------------------------------------------------
bw = zeros(30,30,80);       %banana wavelet
hist_index = zeros(20092);  %histogram index
conv_img = zeros(91,51);    %convolution result
q_hist = zeros(256,1);      %histogram of a query image
d_hist = zeros(256,1);      %histogram of a database image
dist_pix = zeros(256,1);    %histogram distance at a pixel
sum_dist = zeros;           %summation of histogram distances
summ_dist = zeros;
min_value = zeros;          %value of histogram with minimum distance in a banana wavelet
min_index = zeros;          %position of histogram with minimum distance in a banana wavelet

%reading ear image from the folder-----------------------------------------
[ear_file,ear_path] = uigetfile('H:\MATLAB\Ear Biometrics\Databases\XM2VTS (Recognition subset 20 imgs-1)\*.jpg','Select an image');
ear_img = rgb2gray(im2double(imread(strcat(ear_path,ear_file))));

ear_folder = 'H:\MATLAB\Ear Biometrics\Databases\XM2VTS (Recognition subset 20 imgs-1)';
ear_filePattern = fullfile(ear_folder, '*.jpg');
ear_jpegFiles = dir(ear_filePattern);
for ear_img_counter = 1:length(ear_jpegFiles)
    bw_counter = 1;
    
    %loading existing histograms from database-----------------------------
    files = dir('H:\MATLAB\Ear Biometrics\Histograms\Banana - Histograms (Recognition subset 20 imgs)\*.mat');
    mainDir = pwd;
    hist_counter_x = hist_index + 1;    %histogram index counter
    hist_counter_y = hist_index + 80;   %histogram index counter
    for hist_index = hist_counter_x : hist_counter_y
        eval(sprintf('d_histPath=fullfile(mainDir,''Histograms'',''Banana - Histograms (Recognition subset 20 imgs)'',files(%d,1).name);',hist_index));
        eval(sprintf('d_histStruct_%d=load(d_histPath);',hist_index));
        eval(sprintf('d_hist_%d=d_histStruct_%d.hist;',hist_index,hist_index));
        eval(sprintf('d_hist = d_hist_%d;',hist_index));
        eval(sprintf('clear d_histStruct_%d;',hist_index));
        
        %reading banana wavelets from the folder---------------------------
        bw_folder = 'H:\MATLAB\Ear Biometrics\Wavelet Images\Wavelet Images (Recognition)';
        bw_filePattern = fullfile(bw_folder, '*.jpg');
        bw_jpegFiles = dir(bw_filePattern);
        for bw_index = bw_counter
            bw_baseFileName = bw_jpegFiles(bw_index).name;
            bw_fullFileName = fullfile(bw_folder, bw_baseFileName);
            bw(:,:,bw_index) = rgb2gray(im2double(imread(bw_fullFileName)));
            %             subplot(2,2,1), imshow(bw(:,:,bw_counter));
            %             subplot(2,2,2), imshow(ear_img);
            
            %performing convolution of banana wavelets with query ear image
            conv_img(:,:) = mat2gray(convolve2(double(ear_img), double(bw(:,:,bw_index)),'valid', 0));
            %             subplot(2,2,3), imshow(conv_img(:,:,bw_counter));
            
            %calculating histograms for windows in convolved query ear image
            q_hist(:,:) = imhist(conv_img(:,:), 256);
            %             subplot(2,2,4), imhist(conv_img, 256);
            %             drawnow;
            dist_pix(:,:) = (abs(q_hist(:,:) - d_hist(:,:)));
            sum_dist(bw_index) = sum(dist_pix(:,:),1);
            eval(sprintf('clear d_hist_%d;',hist_index));
        end
        bw_counter = bw_index + 1;    %banana wavelet index limit
        clear bw conv_img row_index col_index q_hist d_hist;
    end
    summ_dist(ear_img_counter) = sum(sum_dist(:),1);
    [min_value,min_index] = min(summ_dist(:));
    clear bw_counter; 
end
end