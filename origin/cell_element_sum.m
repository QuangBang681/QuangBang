function[Gsum,Csum]=cell_element_sum(node,Gc,Cc,dx)
%node = matrix(1,5) elements need calculating sum in matrix x
%x = cell(1,N) in which each cell contain a vector
%dx = matrix(1,N)

Gsum = 0;   Csum = 0;
for i = 1:5,
    if node(i)>0,
        vt1 = Gc{node(i)};
        vt2 = Cc{node(i)};
        Nxi = length(vt1);
        if (mod(i,2)==0)|(i==5),
            n = 1;
        else
            n = Nxi;
        end
        Gsum = Gsum+0.5*vt1(n)*dx(node(i));
                
        Csum = Csum+0.5*vt2(n)*dx(node(i));
    end
end
