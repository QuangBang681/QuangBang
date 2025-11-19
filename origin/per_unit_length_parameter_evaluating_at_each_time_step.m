function[Gs,Cs,Ls] = per_unit_length_parameter_evaluating_at_each_time_step(Aj_i,Bj_i,Dj_i,R,P,L)

F = R*Aj_i;
Gs = 1./diag(F);
F = P*Bj_i;
Cs = 1./diag(F);
F = L*Dj_i;
Ls = diag(F);

Gs = Gs';
Cs = Cs';
Ls = Ls';