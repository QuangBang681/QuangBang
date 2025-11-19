function[uv]= voltage_evaluating_at_each_time_step(iv,uv,V,element,Gc,Cc,t,dx,dt)
    
    N = length(iv);
%{
%RBF_IMQ%    
for i = 1:N,
    c=5.1360;%sim20
    %c=8.0760;%sim100    
    k(i)=(dx(i)/2)/((1/(c^2)^(1/2) - 1/(c^2 + 4*(dx(i)/2)^2)^(1/2))*(c^2 + (dx(i)/2)^2)^(3/2));%a1x_IMQ
    ct=0.005;
    kt=dt/((sqrt(dt^2+ct^2)-ct)*sqrt(dt^2/4+ct^2)*2);
    Ne = length(iv{i}(t,:));   
    uv{i}(t,1) = V(element(i,1));
    if element(i,2)~=0,
        uv{i}(t,Ne+1) = V(element(i,2));
    else
        uv{i}(t,Ne+1) = 1/(Cc{i}(Ne)/2*kt+Gc{i}(Ne)/4)*(iv{i}(t,Ne)*k(i)+(Cc{i}(Ne)/2*kt-Gc{i}(Ne)/4)*uv{i}(t-1,Ne+1));
    end
    G = 0.5*(Gc{i}(1:Ne-1)+Gc{i}(2:Ne));
    C = 0.5*(Cc{i}(1:Ne-1)+Cc{i}(2:Ne));
    uv{i}(t,2:Ne) = 1./(C*kt+G/2).*((iv{i}(t,1:Ne-1)-iv{i}(t,2:Ne))*k(i)+(C*kt-G/2).*uv{i}(t-1,2:Ne));    
end
%}

%{    
%RBF_GA%    
for i = 1:N,
    c=4.3520;%sim20
    %c=6.7040;%sim100
    k(i)=(2*(dx(i)/2)*exp(-(dx(i)/2)^2/c^2))/(c^2*(1-exp(-4*(dx(i)/2)^2/c^2)));%a1x_GA
    ct=0.005;
    kt=dt/((sqrt(dt^2+ct^2)-ct)*sqrt(dt^2/4+ct^2)*2);
    Ne = length(iv{i}(t,:));   
    uv{i}(t,1) = V(element(i,1));
    if element(i,2)~=0,
        uv{i}(t,Ne+1) = V(element(i,2));
    else
        uv{i}(t,Ne+1) = 1/(Cc{i}(Ne)/2*kt+Gc{i}(Ne)/4)*(iv{i}(t,Ne)*k(i)+(Cc{i}(Ne)/2*kt-Gc{i}(Ne)/4)*uv{i}(t-1,Ne+1));
    end
    G = 0.5*(Gc{i}(1:Ne-1)+Gc{i}(2:Ne));
    C = 0.5*(Cc{i}(1:Ne-1)+Cc{i}(2:Ne));
    uv{i}(t,2:Ne) = 1./(C*kt+G/2).*((iv{i}(t,1:Ne-1)-iv{i}(t,2:Ne))*k(i)+(C*kt-G/2).*uv{i}(t-1,2:Ne));    
end
%}

%{
%RBF_IQ%    
for i = 1:N,
    c=6.0180;%sim20
    %c=9.4480;%sim100
    k(i)=(c^2*(c^2 + 4*(dx(i)/2)^2))/(2*(dx(i)/2)*(c^2 + (dx(i)/2)^2)^2);%a1x_IQ
    ct=0.005;
    kt=dt/((sqrt(dt^2+ct^2)-ct)*sqrt(dt^2/4+ct^2)*2);
    Ne = length(iv{i}(t,:));   
    uv{i}(t,1) = V(element(i,1));
    if element(i,2)~=0,
        uv{i}(t,Ne+1) = V(element(i,2));
    else
        uv{i}(t,Ne+1) = 1/(Cc{i}(Ne)/2*kt+Gc{i}(Ne)/4)*(iv{i}(t,Ne)*k(i)+(Cc{i}(Ne)/2*kt-Gc{i}(Ne)/4)*uv{i}(t-1,Ne+1));
    end
    G = 0.5*(Gc{i}(1:Ne-1)+Gc{i}(2:Ne));
    C = 0.5*(Cc{i}(1:Ne-1)+Cc{i}(2:Ne));
    uv{i}(t,2:Ne) = 1./(C*kt+G/2).*((iv{i}(t,1:Ne-1)-iv{i}(t,2:Ne))*k(i)+(C*kt-G/2).*uv{i}(t-1,2:Ne));    
end
%}

%RBF_MQ%    
for i = 1:N,
    c=2.6860;%sim20
    %c=4.5480;%sim100
    k(i)=(c+sqrt(c^2+4*(dx(i)/2)^2))/(4*(dx(i)/2)*sqrt((dx(i)/2)^2+c^2));%a1x_MQ
    ct=0.005;
    kt=dt/((sqrt(dt^2+ct^2)-ct)*sqrt(dt^2/4+ct^2)*2);
    Ne = length(iv{i}(t,:));   
    uv{i}(t,1) = V(element(i,1));
    if element(i,2)~=0,
        uv{i}(t,Ne+1) = V(element(i,2));
    else
        uv{i}(t,Ne+1) = 1/(Cc{i}(Ne)/2*kt+Gc{i}(Ne)/4)*(iv{i}(t,Ne)*k(i)+(Cc{i}(Ne)/2*kt-Gc{i}(Ne)/4)*uv{i}(t-1,Ne+1));
    end
    G = 0.5*(Gc{i}(1:Ne-1)+Gc{i}(2:Ne));
    C = 0.5*(Cc{i}(1:Ne-1)+Cc{i}(2:Ne));
    uv{i}(t,2:Ne) = 1./(C*kt+G/2).*((iv{i}(t,1:Ne-1)-iv{i}(t,2:Ne))*k(i)+(C*kt-G/2).*uv{i}(t-1,2:Ne));    
end

%{
N = length(iv);
for i = 1:N,
    Ne = length(iv{i}(t,:));   
    uv{i}(t,1) = V(element(i,1));
    if element(i,2)~=0,
        uv{i}(t,Ne+1) = V(element(i,2));
    else
        uv{i}(t,Ne+1) = 1/(Cc{i}(Ne)/2/dt+Gc{i}(Ne)/4)*(iv{i}(t,Ne)/dx(i)+(Cc{i}(Ne)/2/dt-Gc{i}(Ne)/4)*uv{i}(t-1,Ne+1));
    end
    G = 0.5*(Gc{i}(1:Ne-1)+Gc{i}(2:Ne));
    C = 0.5*(Cc{i}(1:Ne-1)+Cc{i}(2:Ne));
    uv{i}(t,2:Ne) = 1./(C/dt+G/2).*((iv{i}(t,1:Ne-1)-iv{i}(t,2:Ne))/dx(i)+(C/dt-G/2).*uv{i}(t-1,2:Ne));    
end
%}