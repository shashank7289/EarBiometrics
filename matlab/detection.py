function [centre_pixel_x, centre_pixel_y] = detection(img)
%detection - function that detects the pixel aaround which the ear is 
%located in an ear image
%Usage:
%  detection()
%--------------------------------------------------------------------------

%preallocation-------------------------------------------------------------
bw = zeros(30,30,88);       %banana wavelet
hist_counter = 1;           %histogram index counter
conv_img = zeros(547,691);  %convolution result
q_hist = zeros(256,1);      %histogram of a query image
d_hist = zeros(256,1);      %histogram of a database image
dist_pix = zeros(256,1);    %histogram distance at a pixel
sum_dist = zeros(452,544);  %summation of histogram distances
min_value = zeros;          %value of histogram with minimum distance in a banana wavelet
min_index = zeros;          %position of histogram with minimum distance in a banana wavelet

%reading ear image from the folder-----------------------------------------
[ear_file,ear_path] = uigetfile('H:\MATLAB\Ear Biometrics\Databases\XM2VTS\*.jpg','Select an image');
ear_img = rgb2gray(im2double(imread(strcat(ear_path,ear_file))));

%reading banana wavelets from the folder-----------------------------------
bw_folder = 'H:\MATLAB\Ear Biometrics\Wavelet Images\Wavelet Images (Detection)';
bw_filePattern = fullfile(bw_folder, '*.jpg');
bw_jpegFiles = dir(bw_filePattern);
for bw_counter = 1:length(bw_jpegFiles)
    bw_baseFileName = bw_jpegFiles(bw_counter).name;
    bw_fullFileName = fullfile(bw_folder, bw_baseFileName);
    bw(:,:,bw_counter) = rgb2gray(im2double(imread(bw_fullFileName)));
    subplot(2,2,1), imshow(bw(:,:,bw_counter));
    subplot(2,2,2), imshow(ear_img);
    
    %performing convolution of banana wavelets with query ear image--------
    conv_img(:,:) = mat2gray(convolve2(double(ear_img), double(bw(:,:,bw_counter)),'valid', 0));
    subplot(2,2,3), imshow(conv_img(:,:,bw_counter));
    
    %loading existing histograms from database-----------------------------
    files = dir('H:\MATLAB\Ear Biometrics\Histograms\Banana - Histograms (Detection)\*.mat');
    mainDir = pwd;    
    for hist_index = hist_counter
        eval(sprintf('d_histPath=fullfile(mainDir,''Histograms'',''Banana - Histograms (Detection)'',files(%d,1).name);',hist_index));
        eval(sprintf('d_histStruct_%d=load(d_histPath);',hist_index));
        eval(sprintf('d_hist_%d=d_histStruct_%d.hist;',hist_index,hist_index));
        eval(sprintf('d_hist = d_hist_%d;',hist_index));
        eval(sprintf('clear d_histStruct_%d;',hist_index));
        
        %calculating histograms for windows in convolved query ear image---
        for row_index = 1:(547-95)
            for col_index = 1:(691-147)
                window = conv_img((row_index : row_index + 94), (col_index : col_index + 146));
                q_hist(:,:) = imhist(window, 256);
                subplot(2,2,4), imhist(window, 256);
                drawnow;
                dist_pix(:,:,row_index,col_index) = (abs(q_hist(:,:) - d_hist(:,:)));
                sum_dist(row_index, col_index) = sum(dist_pix(:,:,row_index,col_index) ,1);
            end
        end
        [min_value(bw_counter),min_index(bw_counter)] = min(sum_dist(:));
        [i,j] = ind2sub(size(sum_dist), min_index);
        
        mesh(sum_dist);
        eval(sprintf('clear d_hist_%d;',hist_index));
        hist_counter = hist_index + 1;    %histogram index limit
    end
    clear bw conv_img row_index col_index q_hist d_hist;    
end
[~,min_bw_index] = min(min_value(:));
[x,~] = ind2sub(size(sum_dist), min_bw_index);
centre_pixel_x = i(x);
centre_pixel_y = j(x);
end