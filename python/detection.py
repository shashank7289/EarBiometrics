'''
Created on Jan 16, 2017

@author: uid38420
'''
@mfunction("centre_pixel_x, centre_pixel_y")
def detection(img=None):
    #detection - function that detects the pixel aaround which the ear is 
    #located in an ear image
    #Usage:
    #  detection()
    #--------------------------------------------------------------------------

    #preallocation-------------------------------------------------------------
    bw = zeros(30, 30, 88)#banana wavelet
    hist_counter = 1#histogram index counter
    convImg = zeros(547, 691)#convolution result
    q_hist = zeros(256, 1)#histogram of a query image
    d_hist = zeros(256, 1)#histogram of a database image
    dist_pix = zeros(256, 1)#histogram distance at a pixel
    sum_dist = zeros(452, 544)#summation of histogram distances
    min_value = zeros#value of histogram with minimum distance in a banana wavelet
    min_index = zeros#position of histogram with minimum distance in a banana wavelet

    #reading ear image from the folder-----------------------------------------
    [ear_file, ear_path] = uigetfile(mstring('H:\\MATLAB\\Ear Biometrics\\Databases\\XM2VTS\\*.jpg'), mstring('Select an image'))
    img = rgb2gray(im2double(imread(strcat(ear_path, ear_file))))

    #reading banana wavelets from the folder-----------------------------------
    bw_folder = mstring('H:\\MATLAB\\Ear Biometrics\\Wavelet Images\\Wavelet Images (Detection)')
    bw_filePattern = fullfile(bw_folder, mstring('*.jpg'))
    bw_jpegFiles = dir(bw_filePattern)
    for bw_counter in mslice[1:length(bw_jpegFiles)]:
        bw_baseFileName = bw_jpegFiles(bw_counter).name
        bw_fullFileName = fullfile(bw_folder, bw_baseFileName)
        bw(mslice[:], mslice[:], bw_counter).lvalue = rgb2gray(im2double(imread(bw_fullFileName)))
        subplot(2, 2, 1)
        imshow(bw(mslice[:], mslice[:], bw_counter))

        subplot(2, 2, 2)
        imshow(img)


        #performing convolution of banana wavelets with query ear image--------
        convImg(mslice[:], mslice[:]).lvalue = mat2gray(convolve2(double(img), double(bw(mslice[:], mslice[:], bw_counter)), mstring('valid'), 0))
        subplot(2, 2, 3)
        imshow(convImg(mslice[:], mslice[:], bw_counter))


        #loading existing histograms from database-----------------------------
        files = dir(mstring('H:\\MATLAB\\Ear Biometrics\\Histograms\\Banana - Histograms (Detection)\\*.mat'))
        mainDir = pwd
        for hist_index in hist_counter:
            eval(sprintf(mstring('d_histPath=fullfile(mainDir,\'Histograms\',\'Banana - Histograms (Detection)\',files(%d,1).name);'), hist_index))
            eval(sprintf(mstring('d_histStruct_%d=load(d_histPath);'), hist_index))
            eval(sprintf(mstring('d_hist_%d=d_histStruct_%d.hist;'), hist_index, hist_index))
            eval(sprintf(mstring('d_hist = d_hist_%d;'), hist_index))
            eval(sprintf(mstring('clear d_histStruct_%d;'), hist_index))

            #calculating histograms for windows in convolved query ear image---
            for row_index in mslice[1:(547 - 95)]:
                for col_index in mslice[1:(691 - 147)]:
                    window = convImg((mslice[row_index:row_index + 94]), (mslice[col_index:col_index + 146]))
                    q_hist(mslice[:], mslice[:]).lvalue = imhist(window, 256)
                    subplot(2, 2, 4)
                    imhist(window, 256)

                    drawnow()
                    dist_pix(mslice[:], mslice[:], row_index, col_index).lvalue = (abs(q_hist(mslice[:], mslice[:]) - d_hist(mslice[:], mslice[:])))
                    sum_dist(row_index, col_index).lvalue = sum(dist_pix(mslice[:], mslice[:], row_index, col_index), 1)
                end
            end
            [min_value(bw_counter), min_index(bw_counter)] = min(sum_dist(mslice[:]))
            [i, j] = ind2sub(size(sum_dist), min_index)

            mesh(sum_dist)
            eval(sprintf(mstring('clear d_hist_%d;'), hist_index))
            hist_counter = hist_index + 1        #histogram index limit
        end
        clear(mstring('bw'), mstring('convImg'), mstring('row_index'), mstring('col_index'), mstring('q_hist'), mstring('d_hist'))
    end
    min(min_value(mslice[:]))
    ind2sub(size(sum_dist), min_bw_index)
    centre_pixel_x = i(x)
    centre_pixel_y = j(x)
end
