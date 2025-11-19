function[x1,x2,yb,xb,y1,y2,di]=input_perpendicular_case(xs1,ys1,zs1,d1,xs2,ys2,zs2,d2)

if d1==1,               %x---------->x
    if d2==2,           %y---------->y
        x1 = xs1(1);
        x2 = xs1(2);
        yb = ys1(1);
        xb = xs2(1);
        y1 = ys2(1);
        y2 = ys2(2);        
        di = abs(zs1(1)-zs2(1));        
    else                %y---------->z
        x1 = xs1(1);
        x2 = xs1(2);
        yb = zs1(1);
        xb = xs2(1);
        y1 = zs2(1);
        y2 = zs2(2);
        di = abs(ys1(1)-ys2(1));        
    end
elseif d1==2,           %x---------->y
    if d2==3,           %y---------->z
        x1 = ys1(1);
        x2 = ys1(2);
        yb = zs1(1);
        xb = ys2(1);
        y1 = zs2(1);
        y2 = zs2(2);
        di = abs(xs1(1)-xs2(1));
    else                %y---------->x
        x1 = ys1(1);
        x2 = ys1(2);
        yb = xs1(1);
        xb = ys2(1);
        y1 = xs2(1);
        y2 = xs2(2);
        di = abs(zs1(1)-zs2(1));
    end
else                    %x---------->z
    if d2==1,           %y---------->x
        x1 = zs1(1);
        x2 = zs1(2);
        yb = xs1(1);
        xb = zs2(1);
        y1 = xs2(1);
        y2 = xs2(2);
        di = abs(ys1(1)-ys2(1));
    else                %y---------->y
        x1 = zs1(1);
        x2 = zs1(2);
        yb = ys1(1);
        xb = zs2(1);
        y1 = ys2(1);
        y2 = ys2(2);
        di = abs(xs1(1)-xs2(1));
    end    
end
