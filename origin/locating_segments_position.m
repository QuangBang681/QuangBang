function[x,y,z,r,d] = locating_segments_position(d_x,d_y,p_z,rx,ry,rz)
%       0           x
%       /---------->
%      /|
%     / |
%    /  |
%  yv   |
%       |
%      zv
%   d_x = matrix(1,Nx): lengths of grid cells on x direction
%   d_y = matrix(1,Ny): lengths of grid cells on y direction
%   p_z = matrix(1,(Nx+1)x(Ny+1)): lengths of rods at nodes of grid
%   x = matrix(number of segments,2)
%   y = matrix(number of segments,2)
%   z = matrix(number of segments,2)
%   d = matrix(1,number of segments): 1--->dx   2--->dy   --->dz
%   rx = matrix(Ny+1,Nx): radius of bars parallel to x-axis
%   ry = matrix(Nx+1,Ny): radius of bars parallel to y-axis
%   rz = matrix(1,(Nx+1)x(Ny+1)): radius of rod parallel to z-axis
%
%
%
%
%
%START
Nx = length(d_x);
Ny = length(d_y);
rod = find_non_zero_elements(p_z);
Ns = (Ny+1)*sum(ceil(d_x))+(Nx+1)*sum(ceil(d_y))+sum(ceil(p_z));
x = zeros(Ns,2);y = x; z = x;
d = ones(1,Ns);%bi?n d m?ng giá có Ns ph?n t? t? 1 ??n Ns, m?i ph?n t? ones=1 
r = d;
%SEGMENTS ON X DIRECTION (begin at n = 1)
z1 = 0;
y1 = 0;
Nxs = sum(ceil(d_x));
for j = 1:Ny+1,
    if j>=2,y1 = y1+d_y(j-1); end
    x1 = 0;
    Nxi = 0;
    Nxr = 0;    
    for i = 1:Nx,        
        if i>=2,x1 = x1+d_x(i-1); end  
        Nxr = Nxr+Nxi;                  % Number of segments on x direction so far 
        Nxi = ceil(d_x(i));             % Number of segments on i_th bar on x direction   
        dx  = d_x(i)/Nxi;
        for k = 1:Nxi,
            n = k + Nxr +(j-1)*Nxs;
            %---------------
            d(n) = 1;                   % Parallel to x-axis
            %---------------
            r(n) = rx(j,i);
            %---------------
            x(n,1) = x1+(k-1)*dx;
            x(n,2) = x1+k*dx;
            %---------------
            y(n,1) = y1;
            y(n,2) = y1;
            %---------------
            z(n,1) = z1;
            z(n,2) = z1;
        end
    end
end
%SEGMENTS ON Y DIRECTION (begin at n = 1+(Ny+1)*Nxs)
z1 = 0;
x1 = 0;
Nys = sum(ceil(d_y));
n0 = (Ny+1)*Nxs;
for i = 1:Nx+1,
    if i>= 2, x1 = x1+d_x(i-1); end
    y1 = 0;
    Nyj = 0;
    Nyr = 0;
    for j = 1:Ny,
        if j>=2, y1 = y1+d_y(j-1); end
        Nyr = Nyr+Nyj;                  % Number of segments on y direction
        Nyj = ceil(d_y(j));             % Number of segments on j_th bar on y direction
        dy = d_y(j)/Nyj;
        for k = 1:Nyj,
            n = n0 + k + Nyr + (i-1)*Nys;
            %---------------
            d(n) = 2;                   % parallel to y-axis
            %---------------
            r(n) = ry(i,j);
            %---------------
            x(n,1) = x1;
            x(n,2) = x1;
            %---------------
            y(n,1) = y1+(k-1)*dy;
            y(n,2) = y1+k*dy;
            %---------------
            z(n,1) = z1;
            z(n,2) = z1;
        end
    end
end
%SEGMENTS ON Z DIRECTION
if rod(1)~= 0,
    n0 = (Ny+1)*Nxs+(Nx+1)*Nys;
    Nz = length(rod);
    Nzs = sum(ceil(p_z));
    Nzr = 0;
    Nzk = 0;
    for k = 1:Nz,
        lk = p_z(rod(k));
        Nzr = Nzr+Nzk;
        Nzk = ceil(lk);
        dz = lk/Nzk;
        z1 = 0;
        %-------------------
        [i,j] = locating_node_position(rod(k),Nx);
        x1 = 0;
        y1 = 0;
        if i>=2,x1 = sum(d_x(1:i-1));end
        if j>=2,y1 = sum(d_y(1:j-1));end
        for m = 1:Nzk,
            n = n0+m+Nzr;
            %---------------
            d(n) = 3;                       % Parallel to z-axis
            %---------------
            r(n) = rz(rod(k));
            %---------------
            x(n,1) = x1;
            x(n,2) = x1;
            %---------------
            y(n,1) = y1;
            y(n,2) = y1;
            %---------------
            z(n,1) = z1+(m-1)*dz;
            z(n,2) = z1+m*dz;
        end
    end
end