function[Vs]=complex2simple_voltage(d_x,d_y,p_z,Vc,t)
%Vc: parameters in complex geometrical model
%Vs: parameters in simple model where position of segments are not
%    considered
Nx = length(d_x);
Ny = length(d_y);
[rod] = find_non_zero_elements(p_z);
if rod(1)~=0,
    Nz = length(rod);
else Nz = 0;
end
Ns = (Ny+1)*sum(ceil(d_x))+(Nx+1)*sum(ceil(d_y))+sum(ceil(p_z));

Nc = 2*Nx*Ny+Nx+Ny+Nz;

Vs = zeros(1,Ns);

if Ns == length(Vs),                    %Thong so dung

Nxs = sum(ceil(d_x));
for j = 1:Ny+1,
    Nxi = 0;
    Nxr = 0;
    for i = 1:Nx,
        Nxr = Nxr+Nxi;                  % Number of segments on x direction so far 
        Nxi = ceil(d_x(i));             % Number of segments on i_th bar on x direction         
        nc = i+(j-1)*Nx; 
        ns = (j-1)*Nxs+Nxr;
        Vs(ns+1:ns+Nxi)=0.5*(Vc{nc}(t,1:Nxi)+Vc{nc}(t,2:Nxi+1));                   
    end
end
Nys = sum(ceil(d_y));
n0 = (Ny+1)*Nxs;
for i = 1:Nx+1,
    Nyj = 0;
    Nyr = 0;
    for j = 1:Ny,
        Nyr = Nyr+Nyj;
        Nyj = ceil(d_y(j));
        nc = (Ny+1)*Nx+j+(i-1)*Ny;
        ns = (i-1)*Nys+Nyr+n0;
        Vs(ns+1:ns+Nyj)=0.5*(Vc{nc}(t,1:Nyj)+Vc{nc}(t,2:Nyj+1));   
    end
end
if Nz~=0, 
    n0 = (Ny+1)*Nxs+(Nx+1)*Nys;
    Nzs = sum(ceil(p_z));
    Nzr = 0;
    Nzk = 0;
    for k = 1:Nz,
        lk = p_z(rod(k));
        Nzr = Nzr+Nzk;
        Nzk = ceil(lk);        
        nc = k + 2*Nx*Ny+Nx+Ny;  
        ns = Nzr+n0;
        Vs(ns+1:ns+Nzk)=0.5*(Vc{nc}(t,1:Nzk)+Vc{nc}(t,2:Nzk+1));
    end
end
else                                    % Thong so sai
    printf('\nKich thuoc luoi khong khop voi so phan tu cua Xs');
end