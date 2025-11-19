
ok = 1;
while ok
    clc;
    fprintf('PLEASE INPUT REFERENCE TIME:\n');
    tref = input('');
    Nref = round(tref/dt);
    [Vs] = QS_complex2simple_voltage(d_x, d_y, uv, Nref);

    N = length(Vs(:,1));
    figure(2);
    hold off;
    grid on;
    xlabel('x(m)');
    ylabel('y(m)');
    zlabel('U(V)');
    hold on;

    % Create a colormap
    colors = colormap(jet); % Using 'jet' colormap
    cmin = min(Vs(:));
    cmax = max(Vs(:));

    for i = 1:N
        for j = 1:length(Vs(i,:))
            % Normalize the value of Vs to the range of the colormap
            colorIndex = round((Vs(i,j) - cmin) / (cmax - cmin) * (size(colors, 1) - 1)) + 1;
            color = colors(colorIndex, :);
            
            % Plot the stem with the corresponding color
            plot3([x(i,j), x(i,j)], [y(i,j), y(i,j)], [0, Vs(i,j)], 'Color', color);
            plot3(x(i,j), y(i,j), Vs(i,j), 'o', 'Color', color, 'MarkerFaceColor', color);
        end
        % Plot the base line in black
        plot3(x(i,:), y(i,:), zeros(1, length(x(i,:))), 'k', 'LineWidth', 3);
    end

    view(150,60); 
    pause;
    hold off;
    fprintf('WOULD YOU LIKE TO OBSERVE AT A DIFFERENT TIME:\n    PRESS 1:YES\n    PRESS 0:NO\n');
    ok = input('');
end
