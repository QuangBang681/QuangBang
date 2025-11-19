function[isum]=cell_element_current_sum(node,iv,ims,t)
%node = matrix(1,5) elements need calculating sum in matrix x


isum = ims;
for i = 1:5,
    if node(i)>0,
        vt = iv{node(i)};
        Nxi = length(vt(t,:));
        if (mod(i,2)==0)|(i==5),
            n = 1;
            k = -1;
        else
            n = Nxi;
            k = 1;
        end
        isum = isum+k*vt(t,n);        
    end
end

