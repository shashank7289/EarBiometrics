function B_b = banana_wavelet(x, y, f, a, c, s, sigma_x, sigma_y, u, v)

% banana_wavelet - function that generates banana wavelets
%
% Usage:
%   banana_wavelet (x, y, f, a, c, s, sigma_x, sigma_y, u, v)
%
% Input:
%   x           - no. of rows of wavelet
%   y           - no. of columns of wavelet
%   f           - frequency
%   a           - orientation
%   c           - curvature
%   s           - size
%   sigma_x     - scale of Gaussian filter in x direction
%   sigma_y     - scale of Gaussian filter in y direction
%   u           - for different values of orientation
%   v           - for different values of frequency
%
% Output:
%   B_b         - Banana Wavelet
% -------------------------------------------------------------------------

gamma = 1;  %constant

%Initialization
G_b = zeros(x,y);
F_b = zeros(x,y);
B_b = zeros(x,y);

for m = -x/2 + 1 : x/2
    for n = -y/2 + 1 : y/2
        
        f1 = f + (v/10);
        alpha = u * a;
        
        x_c = m*cos(alpha) + n*sin(alpha);
        x_s = -m*sin(alpha) + n*cos(alpha);
        
        % G_b(x,y) - Gaussian function
        G_b(m+x/2,n+y/2) = exp((-(f1^2/2)) * ((1/(sigma_x)^2) * ((x_c + c*(x_s)^2)^2)...
            + ((1/(sigma_y)^2) * (1/s^2) * (x_s)^2)));
        
        % F_b(x,y) - curved complex wave function
        F_b(m+x/2,n+y/2) = exp(1i * f1 * (x_c + c * (x_s)^2));
        
        % DC_b - bias of the banana wavelets
        DC_b = exp(-sigma_x/2);
        
        % B_b - Banana Wavelet
        B_b(m+x/2,n+y/2) = gamma * G_b(m+x/2,n+y/2) * (F_b(m+x/2,n+y/2) - DC_b);
                   
    end
end

%FI(x_0,b) = conv(B_b,img_array)*(x_0);

end