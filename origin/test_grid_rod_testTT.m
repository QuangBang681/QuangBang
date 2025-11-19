%TINH TOAN QUA DO TREN LUOI NOI DAT
clear;
clc;
%NHAP THOI GIAN MO PHONG
tsim = 20e-6;

%NHAP THONG SO CUA DAT 
res = 1000;%dien tro suat cua dat
eps = 9;%do tham dien ty doi cua d
%LUOI 11
%NHAP THONG SO KICH THUOC CUA LUOI
depth = 0.8;%do chon sau
d_x = [2 4 5.5 5.5 6 8 7 7 10.5 6 3.5];%kich thuoc luoi theo phuong ngang
d_y = [2.5 5 5 7 5 5 5.5 5.5 3.5 3];%kich thuoc luoi theo phuong doc
%d_x =ones(1,2)*10;%kich thuoc luoi theo phuong ngang
%d_y =ones(1,2)*10;%kich thuoc luoi theo phuong doc
rx = 0.007*ones(length(d_y)+1,length(d_x));%ban kinh cac thanh theo phuong ngang
ry = 0.007*ones(length(d_x)+1,length(d_y));%ban kinh cac thanh theo phuong doc
re = 0.25e-6;%dien tro suat cua vat lieu lam luoi
%------------------------------------------------------
%Vi tri va kich thuoc coc neu co(vi tri danh theo thu tu tu trai qua
%phai, tu tren xuong duoi
p_z = 0*ones(1,(length(d_x)+1)*(length(d_y)+1));
%p_z(1:5) = 3*ones(1,5);%coc dai 3 m %??t giá tr? c?a 5 ph?n t? ??u tiên c?a p_z thành 3, t??ng ?ng v?i vi?c ??t c?c có ?? dài 3 mét ? các v? trí ??u tiên trên l??i.
%p_z(21:25) = 3*ones(1,5);%??t giá tr? c?a 5 ph?n t? t?i các v? trí 21 ??n 25 thành 3, t?o ra m?t c?c khác có ?? dài 3 mét trên l??i
%p_z(1:5:21) = 3*ones(1,5);%??t giá tr? c?a m?i ph?n t? cách nhau 5 v? trí t? 1 ??n 21 thành 3. ?i?u này t?o ra m?t c?c kéo dài t? v? trí 1 ??n 21 trên l??i
%p_z(5:5:25) = 3*ones(1,5);%??t giá tr? c?a m?i ph?n t? cách nhau 5 v? trí t? 5 ??n 25 thành 3, t?o ra m?t c?c khác trên l??i.
p_z(1) = 3; %??t giá tr? c?a các ph?n t? t?i các v? trí 7, 9, 13, 17 và 19 thành 3, t?o ra các c?c ng?n có ?? dài 3 mét t?i các v? trí ??c bi?t trên l??i
p_z(3) = 3; 
p_z(5) = 3; 
p_z(7) = 3;
p_z(8) = 3;
p_z(9) = 3;
p_z(12) = 3;
p_z(25) = 3;
p_z(36) = 3;
p_z(49) = 3;
p_z(73) = 3;
p_z(77) = 3;
p_z(97) = 3;
p_z(101) = 3;
p_z(108) = 3;
p_z(121) = 3;
p_z(124) = 3;
p_z(126) = 3;
p_z(127) = 3;
p_z(129) = 3;
p_z(132) = 3;
%p_z(19) = 3;
p_z = 0*p_z;
rz = 0.015*ones(1,length(p_z));%T?o m?t m?ng rz v?i ?? dài b?ng v?i p_z, trong ?ó m?i ph?n t? ??u có giá tr? là 0.015, có th? là kích th??c bán kính c?a các c?c
%------------------------------------------------------

%NHAP GIA TRI DONG SET VA VI TRI CUA SET VAO LUOI
is = inline('12500*(exp(-190099*t)-exp(-2922879*t))','t');
%is = inline('1*(exp(-27e3*t)-exp(-56e5*t))','t');
Imsc = 0*p_z;
Imsc(1) = 1;         %Vi tri vao cua set ba vi tri goc tam canh

%TINH TOAN VI TRI VA KICH THUOC CUA CAC PHAN DOAN       %ok
[x,y,z,r,d] = locating_segments_position(d_x,d_y,p_z,rx,ry,rz); 

%XAC DINH TUONG QUAN GIUA CAC NODE VA CAC PHAN DOAN     %ok
[node,element]=determinating_junction(d_x,d_y,p_z);

%TINH TOAN CAC MA TRAN THONG SO TREN DON VI DAI R,P,L   %ok
load('matrix_test')
%dk = 1;

%if dk ==1,
    %delete('matrix_test.mat');
    %tic
    %[R,P,L]= pul_parameter_matrixes(x,y,z,r,d,depth,res,eps);
    %save('matrix_test','R','P','L');
    %time = toc;
    %phut = floor(time/60);
    %giay = time - 60*phut;
    %gio = floor(phut/60);
    %phut = phut -60*gio;
    %fprintf('Time to calculate parameter matrixes:\n %f gio   %f phut   %f giay',gio,phut,giay);
    %pause(5);
%else
    %load('matrix_test.mat');
%end
%--------------------------------------------------------------------------

%TINH SO KHOANG CUA BUOC THOI GIAN
dt = 1/(3e8);
Nt = round(tsim/dt);
tv = [0:Nt]*dt;
%KHOI TAO MA TRAN THONG SO RS,LS,GS,CS TRONG MO HINH DON GIAN       %ok
Ne = length(r);
Rs = re/(pi)./(r.^2);
Ls = zeros(1,Ne);
Gs = Ls;
Cs = Ls;
for i = 1:Ne,
    Ls(i) = L(i,i);
    Gs(i) = 1/R(i,i);
    Cs(i) = 1/P(i,i);
end

%--------------------------------------------------------------------------
[Rc]=simple2complex(d_x,d_y,p_z,Rs);    
%==============%ok  

%KHOI TAO CELL DONG VA AP CHO TINH TOAN
[iv,uv,dx] = making_initial_value(Nt,d_x,d_y,p_z);
V=zeros(1,(length(d_x)+1)*(length(d_y)+1));
%BIEN KIEM TRA LOI CHUONG TRINH
Gob = zeros(1,Nt);Lob = Gob;Cob = Gob;
%TINH TOAN GIA TRI DONG AP TAI CAC VI TRI TREN LUOI THEO THOI GIAN
tic
for t = 1:Nt,
    %----------------------------------------------------------------------
    %   TINH DONG SET TAI BUOI THOI GIAN KHAO SAT                   %ok
    Ims = Imsc*is(tv(t+1));                                        
        
    %----------------------------------------------------------------------
    %   CHUYEN DOI DONG TU MO HINH PHUC TAP SANG MO HINH DON GIAN   %ok
    [Is]=complex2simple_current(d_x,d_y,p_z,iv,t);
    [Vs]=complex2simple_voltage(d_x,d_y,p_z,uv,t);    
    
    %----------------------------------------------------------------------
    %   TINH TOAN CAC HE SO TUONG HO GIUA CAC PHAN DOAN             %ok
    [Aj_i,Bj_i,Dj_i]=generally_coupling_coefficients_evaluating(Is,Vs,Gs,Cs);
    
    %----------------------------------------------------------------------
    %   TINH TOAN CAC MA TRAN THAM SO TREN DON VI DAI TRONG MO HINH DON
    %   GIAN                                                        %ok
    [Gs,Cs,Ls] = per_unit_length_parameter_evaluating_at_each_time_step(Aj_i,Bj_i,Dj_i,R,P,L);
    Gob(t) = Gs(1);    Lob(t) = Ls(1);    Cob(t) = Cs(1);
    %----------------------------------------------------------------------
    %   CHUYEN CAC MA TRAN THAM SO TU MON HINH DON GIAN SANG MO HINH PHUC
    %   TAP                                                         %ok
    [Lc]=simple2complex(d_x,d_y,p_z,Ls);
    [Gc]=simple2complex(d_x,d_y,p_z,Gs);
    [Cc]=simple2complex(d_x,d_y,p_z,Cs);
    
    %----------------------------------------------------------------------
    %   TINH TOAN GIA TRI DONG TAI BUOC THOI GIAN KHAO SAT          %ok
    
    [iv]= current_evaluating_at_each_time_step(iv,uv,Rc,Lc,t+1,dx,dt);
   
    %----------------------------------------------------------------------
    %   TINH TOAN GIA TRI AP TAI CAC NUT LUOI O BUOC THOI GIAN KHAO SAT %ok
    [V]= grid_junction_volage_evaluating(V,node,iv,uv,t+1,Gc,Cc,Ims,dx,dt);
    
    %----------------------------------------------------------------------
    %   TINH TOAN GIA TRI AP TAI BUOC THOI GIAN KHAO SAT            %ok
    [uv]= voltage_evaluating_at_each_time_step(iv,uv,V,element,Gc,Cc,t+1,dx,dt);    
    
    %----------------------------------------------------------------------    
    round(t/Nt*100)
end

time = toc;
phut = floor(time/60);
giay = time - 60*phut;
gio = floor(phut/60);
phut = phut -60*gio;
fprintf('Time to calculate values of current an voltage at each time step:\n %f gio   %f phut   %f giay \n',gio,phut,giay);
plot(tv*10^6,uv{1}(:,1)'); xlabel('t(us)'); ylabel('U(V)');
grid on;
save('ket_qua_luoi_test.mat','tv','uv');
pause; 
hold off; %on moi off cu tren nen
QUAN_SAT_SU_PHAN_BO_THE_TREN_LUOI_THEO_THOI_GIAN;

