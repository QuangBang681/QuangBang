function[R,P,L]= pul_parameter_matrixes(x,y,z,r,d,depth,res,eps)
%pul: per-unit length
%           0                   x
%           -------------------->
%          /|
%         / |
%        /  |
%       /   |
%    y v    |
%           |
%           |
%           v z
%
%   
%           
%   
%           
%   res:    soil resistivity
%   eps:    soil relative permittivity
%   
eps0 = 1/(4*pi*9e9);
muy0 = 4*pi*1e-7;
k_eps = (eps-1)/(eps+1);
N = length(x(:,1));
R = zeros(N,N);
P = R;
L = R;
for i = 1:N,
    round(i*100/N)
    li = abs(x(i,2)-x(i,1))+abs(y(i,2)-y(i,1))+abs(z(i,2)-z(i,1));%truong hop rieng
    Ii_i = 2*li*(log(2*li/r(i))-1);
    if d(i) ==3,        % z-direction
        zim = image_locating(z(i,:),depth); 
        Ii_ii = line_geometic_factor(zim(1),zim(2),z(i,1),z(i,2));
    elseif d(i)==2,     % y-direction
        Ii_ii = parallel_geometic_factor(2*depth,y(i,1),y(i,2),y(i,1),y(i,2));
    else %d(i) ==1,      % x-direction
        Ii_ii = parallel_geometic_factor(2*depth,x(i,1),x(i,2),x(i,1),x(i,2));
    end      
    R(i,i) = res/(4*pi*li)*(Ii_i+Ii_ii);    
    P(i,i) = 1/eps/eps0/(4*pi*li)*(Ii_i+k_eps*Ii_ii);
    L(i,i) = muy0/(4*pi*li)*Ii_i;
    for j = 1:N,        
        if j~=i,
            if d(i)~=d(j),          % segment i perpendicular to segment j
                [x1,x2,yb,xb,y1,y2,dij]=input_perpendicular_case(x(i,:),y(i,:),z(i,:),d(i),x(j,:),y(j,:),z(j,:),d(j));
                Ii_j = perpendicular_geometic_factor(x1,x2,yb,xb,y1,y2,dij);
                zim = image_locating(z(j,:),depth);
                [x1,x2,yb,xb,y1,y2,dij]=input_perpendicular_case(x(i,:),y(i,:),z(i,:),d(i),x(j,:),y(j,:),zim,d(j));
                Ii_jj = perpendicular_geometic_factor(x1,x2,yb,xb,y1,y2,dij);
                %Calculate R, P, L
                R(i,j) = res/(4*pi*li)*(Ii_j+Ii_jj);
                P(i,j) = 1/(4*pi*eps*eps0*li)*(Ii_j+k_eps*Ii_jj);
                %L(i,j) = 0;
            else                    % segment i and segment j are in the same direction
                switch d(i),
                    case 1,         % x direction
                        dij = sqrt((y(i,1)-y(j,1))^2+(z(i,1)-z(j,1))^2);
                        zim = image_locating(z(j,:),depth);
                        dijj = sqrt((y(i,1)-y(j,1))^2+(z(i,1)-zim(1))^2);
                        if dij~=0, % parallel case 
                            Ii_j = parallel_geometic_factor(dij,x(i,1),x(i,2),x(j,1),x(j,2));
                            Ii_jj = parallel_geometic_factor(dijj,x(i,1),x(i,2),x(j,1),x(j,2));
                        else        % in the same line
                            Ii_j = line_geometic_factor(x(i,1),x(i,2),x(j,1),x(j,2));
                            Ii_jj = parallel_geometic_factor(dijj,x(i,1),x(i,2),x(j,1),x(j,2));
                        end
                    case 2,         % y direction
                        dij = sqrt((x(i,1)-x(j,1))^2+(z(i,1)-z(j,1))^2);
                        zim = image_locating(z(j,:),depth);
                        dijj = sqrt((x(i,1)-x(j,1))^2+(z(i,1)-zim(1))^2);
                        if dij~=0,  % parallel case
                            Ii_j = parallel_geometic_factor(dij,y(i,1),y(i,2),y(j,1),y(j,2));
                            Ii_jj = parallel_geometic_factor(dijj,y(i,1),y(i,2),y(j,1),y(j,2));
                        else        % in the same line
                            Ii_j = line_geometic_factor(y(i,1),y(i,2),y(j,1),y(j,2));
                            Ii_jj = parallel_geometic_factor(dijj,y(i,1),y(i,2),y(j,1),y(j,2));
                        end
                    case 3,         % z direction
                        dij = sqrt((y(i,1)-y(j,1))^2+(x(i,1)-x(j,1))^2);
                        zim = image_locating(z(j,:),depth);
                        if dij~=0,  % parallel case
                            Ii_j = parallel_geometic_factor(dij,z(i,1),z(i,2),z(j,1),z(j,2));
                            Ii_jj = parallel_geometic_factor(dij,z(i,1),z(i,2),zim(1),zim(2));
                        else        % in the same line
                            Ii_j = line_geometic_factor(z(i,1),z(i,2),z(j,1),z(j,2));
                            Ii_jj = line_geometic_factor(z(i,1),z(i,2),zim(1),zim(2));
                        end
                end
                %Calculate R, P, L
                R(i,j) = res/(4*pi*li)*(Ii_j+Ii_jj);
                P(i,j) = 1/(4*pi*eps*eps0*li)*(Ii_j+k_eps*Ii_jj);
                L(i,j) = muy0/(4*pi*li)*Ii_j;
            end            
        end
    end
end