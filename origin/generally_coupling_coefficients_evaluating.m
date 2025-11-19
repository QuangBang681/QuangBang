function[Aj_i,Bj_i,Dj_i]=generally_coupling_coefficients_evaluating(iv,u_ave,g,ca)
%   iv: curent vector at the previous time step
%   uv: voltage vector at the previous time step
%   g: earth conductance vector at the previous time step
%   ca: capacitance vector at the previous time step
c = iv;
v = u_ave;
N = length(iv);
Aj_i = zeros(N,N);
Bj_i = Aj_i;
Dj_i = Aj_i;
for j = 1:N,
    v_ave_j = u_ave(j);
    i_dis_j = g(j)*v_ave_j;
    q_j     = ca(j)*v_ave_j;
    for i = 1:N,
        if i ==j,
            Aj_i(j,i) = 1;
            Bj_i(j,i) = 1;
            Dj_i(j,i) = 1;
        else
            v_ave_i = u_ave(i);
            i_dis_i = g(i)*v_ave_i;
            q_i     = ca(i)*v_ave_i;
            Aj_i(j,i) = comparing(i_dis_j,i_dis_i);
            Bj_i(j,i) = comparing(q_j,q_i);
            Dj_i(j,i) = comparing_L(c(j),c(i));
        end
    end
end