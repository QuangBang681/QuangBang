function[sig] = comparing_L(x,y)

if (abs(x)>0)&(abs(y)>=abs(x)),
    sig = abs(x/y);
elseif abs(x)>abs(y),
    sig = 1;
else sig = 0;
end