function[iv]= current_evaluating_at_each_time_step(iv,uv,Rc,Lc,t,dx,dt)

N = length(iv);
%for i = 1:N,
%    c=6;
%    k(i)=dx(i)/((sqrt(dx(i)^2+c^2)-c)*sqrt(dx(i)^2/4+c^2)*2);
%    ct=0.005;
%    kt=dt/((sqrt(dt^2+ct^2)-ct)*sqrt(dt^2/4+ct^2)*2);
%    Ne = length(iv{i}(t,:));
%    iv{i}(t,:) = 1./(Lc{i}*kt+Rc{i}/2).*((uv{i}(t-1,1:Ne)-uv{i}(t-1,2:Ne+1))*k(i)+(Lc{i}*kt-Rc{i}/2).*iv{i}(t-1,:));
%end

for i = 1:N,
    c=2.6860;%sim20
    %c=4.5480;%sim100
    k(i)=(c+sqrt(c^2+4*(dx(i)/2)^2))/(4*(dx(i)/2)*sqrt((dx(i)/2)^2+c^2));%a1x_MQ
    ct=0.005;
    kt=dt/((sqrt(dt^2+ct^2)-ct)*sqrt(dt^2/4+ct^2)*2);
    %c=6;
    %k(i)=dx(i)/((sqrt(dx(i)^2+c^2)-c)*sqrt(dx(i)^2/4+c^2)*2);
    %ct=0.005;
    %kt=dt/((sqrt(dt^2+ct^2)-ct)*sqrt(dt^2/4+ct^2)*2);
    Ne = length(iv{i}(t,:));
    iv{i}(t,:) = 1./(Lc{i}*kt+Rc{i}/2).*((uv{i}(t-1,1:Ne)-uv{i}(t-1,2:Ne+1))*k(i)+(Lc{i}*kt-Rc{i}/2).*iv{i}(t-1,:));
end
%FDTD
%N = length(iv);
%for i = 1:N,
%    Ne = length(iv{i}(t,:));
%    iv{i}(t,:) = 1./(Lc{i}/dt+Rc{i}/2).*((uv{i}(t-1,1:Ne)-uv{i}(t-1,2:Ne+1))/dx(i)+(Lc{i}/dt-Rc{i}/2).*iv{i}(t-1,:));
%end