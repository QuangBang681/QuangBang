function[iv,uv,dx] = making_initial_value(Nt,d_x,d_y,p_z)

Nx = length(d_x);
Ny = length(d_y);
[rod] = find_non_zero_elements(p_z);
if rod(1)~=0,
    Nz = length(rod);
else Nz = 0;
end
Nsum = 2*Nx*Ny+Nx+Ny+Nz;
iv = cell(1,Nsum);
uv = iv;
dx = ones(1,Nsum);
for j = 1:Ny+1,
    for i = 1:Nx,
        n = i+(j-1)*Nx;
        Nxi = ceil(d_x(i));
        iv(n) = {zeros(Nt+1,Nxi)};        
        uv(n) = {zeros(Nt+1,Nxi+1)}; 
        dx(n) = d_x(i)/Nxi;
    end
end
for i = 1:Nx+1,
    for j = 1:Ny,
        n = (Ny+1)*Nx+j+(i-1)*Ny;
        Nyj = ceil(d_y(j));
        iv(n) = {zeros(Nt+1,Nyj)};
        uv(n) = {zeros(Nt+1,Nyj+1)}; 
        dx(n) = d_y(j)/Nyj;
    end
end
if Nz~=0, 
    for k = 1:Nz,
        n = k + 2*Nx*Ny+Nx+Ny;
        Nzk = ceil(p_z(rod(k)));
        iv(n) = {zeros(Nt+1,Nzk)};        
        uv(n) = {zeros(Nt+1,Nzk+1)}; 
        dx(n) = p_z(rod(k))/Nzk;
    end
end