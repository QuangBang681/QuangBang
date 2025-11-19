function [I_line] = line_geometic_factor(x1,x2,y1,y2)
%   x1              x2      y1                 y2 
%   o---------------o       o------------------o       
%       
if y1<x1,%exchange order of 2 segments
    xt1 = x1;xt2 = x2;
    x1 = y1; x2 = y2;
    y1 = xt1; y2 = xt2;
end
if x2 == y1,    % two segments are near to each other
    I_line = y1*log(abs((y2-x2)/(y1-x1)))-x1*log(abs((y2-x1)/(y1-x1)))+y2*log(abs((y2-x1)/(y2-x2)));
else
    I_line = x2*log(abs((y2-x2)/(y1-x2)))-x1*log(abs((y2-x1)/(y1-x1)))+...
        y2*log(abs((y2-x1)/(y2-x2)))-y1*log(abs((y1-x1)/(y1-x2)));
end