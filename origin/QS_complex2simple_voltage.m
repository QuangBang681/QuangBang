function[Vs]=QS_complex2simple_voltage(d_x,d_y,uv,t)
%Vc: parameters in complex geometrical model
%Vs: parameters in simple model where position of segments are not
%    considered
Nx = length(d_x);
Ny = length(d_y);

Ns = (Ny+1)*sum(ceil(d_x))+(Nx+1)*sum(ceil(d_y));

Vs = zeros(Ns,2);

if Ns == length(Vs(:,1)),                    %Thong so dung

Nxs = sum(ceil(d_x));
for j = 1:Ny+1,
    Nxi = 0;
    Nxr = 0;
    for i = 1:Nx,
        Nxr = Nxr+Nxi;                  % Number of segments on x direction so far 
        Nxi = ceil(d_x(i));             % Number of segments on i_th bar on x direction         
        nc = i+(j-1)*Nx; 
        ns = (j-1)*Nxs+Nxr;
        Vs(ns+1:ns+Nxi,1)=uv{nc}(t,1:Nxi)';
        Vs(ns+1:ns+Nxi,2)=uv{nc}(t,2:Nxi+1)';
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
        Vs(ns+1:ns+Nyj,1)=uv{nc}(t,1:Nyj)';  
        Vs(ns+1:ns+Nyj,2)=uv{nc}(t,2:Nyj+1)';
    end
end

else                                    % Thong so sai
    printf('\nKich thuoc luoi khong khop voi so phan tu cua Xs');
end