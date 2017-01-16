%read_imgs - function that reads images from a folder
%
% Usage:
%   read_imgs()
%
% Arguments:
%   folder      - location from where the images are to be read
% -------------------------------------------------------------------------
function X = read_imgs()
folder = 'E:\Academics\Projects\MATLAB\Ear Biometrics\Databases\XM2VTS - Sample';
filePattern = fullfile(folder, '*.jpg');
jpegFiles = dir(filePattern);
for k = 1:length(jpegFiles)
    baseFileName = jpegFiles(k).name;
    fullFileName = fullfile(folder, baseFileName);
    %fprintf(1, 'Now reading %s\n', fullFileName);
    img = imread(fullFileName);
    imshow(img);    % Display image.
    drawnow;    % Force display to update immediately.
end
end