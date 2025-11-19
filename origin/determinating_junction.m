function[node,element]=determinating_junction(d_x,d_y,p_z)
%   node = matrix(Nju,5): (kx1 kx2 ky1 ky2 kz)
%               /
%              /
%         ----o----
%            /|
%           / |
%             |
%   element = matrix(Nel,2): ( end1----->end2 )  
 

Nx = length(d_x);
Ny = length(d_y);
[rod] = find_non_zero_elements(p_z);
if rod(1)~=0,
    Nz = length(rod);
else Nz = 0;
end
Nju = (Nx+1)*(Ny+1);
Nel = 2*Nx*Ny+Nx+Ny+Nz;
nxe = (Ny+1)*Nx;
nye = 2*Nx*Ny+Nx+Ny;

node = zeros(Nju,5);
element = zeros(Nel,2);

    for j = 2:Ny,
          for i = 2:Nx,
                n = i+(j-1)*(Nx+1);
                kx1 = i-1+(j-1)*Nx;
                kx2 = i+(j-1)*Nx;
                ky1 = nxe+j-1+(i-1)*Ny;
                ky2 = nxe+j+(i-1)*Ny;  
                element(kx1,2) = n;
                element(kx2,1) = n;
                element(ky1,2) = n;
                element(ky2,1) = n;                
                if p_z(n)~=0,
                    cz = element_order_locating(n,rod);
                    kz = nye+cz;
                    element(kz,1) = n;
                else
                    kz = 0;
                end
                    node(n,:) = [kx1,kx2,ky1,ky2,kz];               
                
          end
    end
    % Bien j = 1,j = Ny+1
    for i = 2:Nx,
          %-----------------j = 1
          n = i;
          kx1 = i-1;
          kx2 = i;
          ky1 = 0;
          ky2 = nxe+1+(i-1)*Ny; 
          
          element(kx1,2) = n;
          element(kx2,1) = n;
          %element(ky1) = n;
          element(ky2,1) = n;                
          if p_z(n)~=0,
             cz = element_order_locating(n,rod);
             kz = nye+cz;
             element(kz,1) = n;
          else
             kz = 0;
          end
          node(n,:) = [kx1,kx2,ky1,ky2,kz];               
                
          %------------------- j = Ny+1
          n = i+Ny*(Nx+1);
          kx1 = i-1+Ny*Nx;
          kx2 = i+Ny*Nx;
          ky1 = nxe+Ny+(i-1)*Ny; 
          ky2 = 0;
          
          element(kx1,2) = n;
          element(kx2,1) = n;
          element(ky1,2) = n;
          %element(ky2) = n;                
          if p_z(n)~=0,
             cz = element_order_locating(n,rod);
             kz = nye+cz;
             element(kz,1) = n;
          else
             kz = 0;
          end
          node(n,:) = [kx1,kx2,ky1,ky2,kz];
    end
    
    % Bien i = 1, i = Nx+1
    for j = 2:Ny,
          %---- i = 1
          n = 1+(j-1)*(Nx+1);  
          kx1 = 0;
          kx2 = 1+(j-1)*Nx;
          ky1 = nxe+j-1;
          ky2 = nxe+j;   
          
          %element(kx1) = n;
          element(kx2,1) = n;
          element(ky1,2) = n;
          element(ky2,1) = n;                
          if p_z(n)~=0,
             cz = element_order_locating(n,rod);
             kz = nye+cz;
             element(kz,1) = n;
          else
             kz = 0;
          end
          node(n,:) = [kx1,kx2,ky1,ky2,kz];
          %----i = Nx+1
          n = Nx+1+(j-1)*(Nx+1);
          kx1 = Nx+(j-1)*Nx;
          kx2 = 0;
          ky1 = nxe+j-1+Nx*Ny;
          ky2 = nxe+j+Nx*Ny; 
          
          element(kx1,2) = n;
          %element(kx2) = n;
          element(ky1,2) = n;
          element(ky2,1) = n;                
          if p_z(n)~=0,
             cz = element_order_locating(n,rod);
             kz = nye+cz;
             element(kz,1) = n;
          else
             kz = 0;
          end
          node(n,:) = [kx1,kx2,ky1,ky2,kz];
    end
    %Bien i = 1, j = 1
    n = 1;  
    kx1 = 0;
    kx2 = 1;    
    ky1 = 0;
    ky2 = nxe+1;   
    
    %element(kx1) = n;
    element(kx2,1) = n;
    %element(ky1) = n;
    element(ky2,1) = n;                
    if p_z(n)~=0,
       cz = element_order_locating(n,rod);
       kz = nye+cz;
       element(kz,1) = n;
    else
        kz = 0;
    end
    node(n,:) = [kx1,kx2,ky1,ky2,kz];
    %Bien i = 1, j = Ny+1
    n = 1+Ny*(Nx+1);
    kx2 = 1+Ny*Nx;
    kx1 = 0;
    ky2 = 0;
    ky1 = nxe+Ny;  
    
    %element(kx1) = n;
    element(kx2,1) = n;
    element(ky1,2) = n;
    %element(ky2) = n;                
    if p_z(n)~=0,
       cz = element_order_locating(n,rod);
       kz = nye+cz;
       element(kz,1) = n;
    else
        kz = 0;
    end
    node(n,:) = [kx1,kx2,ky1,ky2,kz];
    %Bien i = Nx+1, j = 1
    n = Nx+1;
    kx1 = Nx; 
    kx2 = 0;
    ky1 = 0;
    ky2 = nxe+1+Nx*Ny; 
    
    element(kx1,2) = n;
    %element(kx2) = n;
    %element(ky1) = n;
    element(ky2,1) = n;                
    if p_z(n)~=0,
       cz = element_order_locating(n,rod);
       kz = nye+cz;
       element(kz,1) = n;
    else
        kz = 0;
    end
    node(n,:) = [kx1,kx2,ky1,ky2,kz];
    %Bien i = Nx+1,j = Ny+1
    n = (Ny+1)*(Nx+1);
    kx1 = (Ny+1)*Nx;  
    kx2 = 0;
    ky1 = nxe+(Nx+1)*Ny;  
    ky2 = 0;
    element(kx1,2) = n;
    %element(kx2) = n;
    element(ky1,2) = n;
    %element(ky2) = n;                
    if p_z(n)~=0,
       cz = element_order_locating(n,rod);
       kz = nye+cz;
       element(kz,1) = n;
    else
        kz = 0;
    end
    node(n,:) = [kx1,kx2,ky1,ky2,kz];

    