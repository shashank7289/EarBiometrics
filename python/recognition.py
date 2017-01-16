'''
Created on Jan 16, 2017

@author: uid38420
'''
#recognition - function that compares a query image with a database image to give
#the recognition result
#
#Usage:
#  recognition()
#--------------------------------------------------------------------------

#preallocation-------------------------------------------------------------
bw = zeros(30, 30, 80)#banana wavelet
hist_index = zeros(20092)#histogram index
convImg = zeros(91, 51)#convolution result
q_hist = zeros(256, 1)#histogram of a query image
d_hist = zeros(256, 1)#histogram of a database image
dist_pix = zeros(256, 1)#histogram distance at a pixel
sum_dist = zeros#summation of histogram distances
summ_dist = zeros
min_value = zeros#value of histogram with minimum distance in a banana wavelet
min_index = zeros#position of histogram with minimum distance in a banana wavelet

#reading ear image from the folder-----------------------------------------
[ear_file, ear_path] = uigetfile(mstring('H:\\MATLAB\\Ear Biometrics\\Databases\\XM2VTS (Recognition subset 20 imgs-1)\\*.jpg'), mstring('Select an image'))
img = rgb2gray(im2double(imread(strcat(ear_path, ear_file))))

ear_folder = mstring('H:\\MATLAB\\Ear Biometrics\\Databases\\XM2VTS (Recognition subset 20 imgs-1)')
ear_filePattern = fullfile(ear_folder, mstring('*.jpg'))
ear_jpegFiles = dir(ear_filePattern)
for ear_img_counter in mslice[1:length(ear_jpegFiles)]:
    bw_counter = 1

    #loading existing histograms from database-----------------------------
    files = dir(mstring('H:\\MATLAB\\Ear Biometrics\\Histograms\\Banana - Histograms (Recognition subset 20 imgs)\\*.mat'))
    mainDir = pwd
    hist_counter_x = hist_index + 1#histogram index counter
    hist_counter_y = hist_index + 80#histogram index counter
    for hist_index in mslice[hist_counter_x:hist_counter_y]:
        eval(sprintf(mstring('d_histPath=fullfile(mainDir,\'Histograms\',\'Banana - Histograms (Recognition subset 20 imgs)\',files(%d,1).name);'), hist_index))
        eval(sprintf(mstring('d_histStruct_%d=load(d_histPath);'), hist_index))
        eval(sprintf(mstring('d_hist_%d=d_histStruct_%d.hist;'), hist_index, hist_index))
        eval(sprintf(mstring('d_hist = d_hist_%d;'), hist_index))
        eval(sprintf(mstring('clear d_histStruct_%d;'), hist_index))

        #reading banana wavelets from the folder---------------------------
        bw_folder = mstring('H:\\MATLAB\\Ear Biometrics\\Wavelet Images\\Wavelet Images (Recognition)')
        bw_filePattern = fullfile(bw_folder, mstring('*.jpg'))
        bw_jpegFiles = dir(bw_filePattern)
        for bw_index in bw_counter:
            bw_baseFileName = bw_jpegFiles(bw_index).name
            bw_fullFileName = fullfile(bw_folder, bw_baseFileName)
            bw(mslice[:], mslice[:], bw_index).lvalue = rgb2gray(im2double(imread(bw_fullFileName)))
            #             subplot(2,2,1), imshow(bw(:,:,bw_counter));
            #             subplot(2,2,2), imshow(img);

            #performing convolution of banana wavelets with query ear image
            convImg(mslice[:], mslice[:]).lvalue = mat2gray(convolve2(double(img), double(bw(mslice[:], mslice[:], bw_index)), mstring('valid'), 0))
            #             subplot(2,2,3), imshow(convImg(:,:,bw_counter));

            #calculating histograms for windows in convolved query ear image
            q_hist(mslice[:], mslice[:]).lvalue = imhist(convImg(mslice[:], mslice[:]), 256)
            #             subplot(2,2,4), imhist(convImg, 256);
            #             drawnow;
            dist_pix(mslice[:], mslice[:]).lvalue = (abs(q_hist(mslice[:], mslice[:]) - d_hist(mslice[:], mslice[:])))
            sum_dist(bw_index).lvalue = sum(dist_pix(mslice[:], mslice[:]), 1)
            eval(sprintf(mstring('clear d_hist_%d;'), hist_index))
        end
        bw_counter = bw_index + 1    #banana wavelet index limit
        clear(mstring('bw'), mstring('convImg'), mstring('row_index'), mstring('col_index'), mstring('q_hist'), mstring('d_hist'))
    end
    summ_dist(ear_img_counter).lvalue = sum(sum_dist(mslice[:]), 1)
    [min_value, min_index] = min(summ_dist(mslice[:]))
    clear(mstring('bw_counter'))
