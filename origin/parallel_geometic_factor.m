function [I_par] = parallel_geometic_factor(d,x1,x2,y1,y2)
%   x1              x2
%   o---------------o       |
%                           |d
%                           |
%       o--------------o    |
%       y1             y2

f = inline('1./sqrt((x-y).^2+z.^2)','x','y','z');
I_par = dblquad(f,x1,x2,y1,y2,[],[],d);