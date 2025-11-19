function[non_zero] = find_non_zero_elements(M)
N = length(M);
non_zero = 0;
count = 0;
for i = 1:N,
    if M(i)~=0,count = count+1;non_zero(count) = i; end
end