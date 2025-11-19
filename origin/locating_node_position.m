function[i,j] = locating_node_position(n,Nx) 
i = mod(n,Nx+1);
j = floor(n/(Nx+1))+1;
if i==0,i = Nx+1; j = j-1; end