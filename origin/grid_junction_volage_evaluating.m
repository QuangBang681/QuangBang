function[V]= grid_junction_volage_evaluating(V,node,iv,uv,t,Gc,Cc,Ims,dx,dt)
%Ims = matrix(1,N):     points out the value and position of lightning current
%                       on grounding grid

N = length(node(:,1));
for n = 1:N,
    no = node(n,:);
    [Gsum,Csum]=cell_element_sum(no,Gc,Cc,dx);
    [isum]=cell_element_current_sum(no,iv,Ims(n),t);
    V(n) = 1/(Gsum/2+Csum/dt)*(isum+(Csum/dt-Gsum/2)*V(n));
end