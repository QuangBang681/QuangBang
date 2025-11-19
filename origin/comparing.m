function[sig] = comparing(x,y)

if (x>0)&(y>x),
    sig = x/y;
elseif(y>0)&(x>=y),
    sig = 1;
else sig = 0;
end