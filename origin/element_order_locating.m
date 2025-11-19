function[ith] = element_order_locating(a,rod)
N = length(rod);
for i = 1:N,
    if a ==rod(i),break; end
end
ith = i;