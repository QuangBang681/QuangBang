function [I_per] = perpendicular_geometic_factor(x1,x2,yb,xb,y1,y2,d)
%   x1              x2
%  yb o---------------o     
%         /d                 
%     xb /                 
%       o y1                
%       |             
%       |
%       |
%       |
%       |
%       |
%       |
%       o y2

f = inline('1./sqrt(x.^2+y.^2+z.^2)','x','y','z');%tr??c s?a l?i
I_per = dblquad(f,x1-xb,x2-xb,y1-yb,y2-yb,[],[],d);%tr??c s?a l?i

