close all;clc;



E=0:3e-5:3.4e-3;%E=Ef is 1.37E-7, resolution of the curve, so necessary.

Gamma=0.0005;

q=1.6e-19;

m=0.067*9e-31;

B=10;

Ec=(1.0567e-34)*B/m; %multiplied by hbar here



%Ef = 3.47E-3 (based off of the chart)



writerObj = VideoWriter('QH.avi'); % Name it.

writerObj.FrameRate = 24; % How many frames per second.

open(writerObj);





for BB=0.1:.01:2

    for i = 1:15%number of curves

        E0=0+(1.0567e-34)*i*BB/m;%make this em over m, divide by m to get cyclo e

        QH = exp(-(E-E0).^2/Gamma.^2);%%make gamma appropriate value

        xlabel('Energy')

        ylabel('DOS')

        figure(1);hold on;plot(E,QH)

        %area(E)



    end



    frame = getframe(gcf); % 'gcf' can handle if you zoom in to take a movie.

    writeVideo(writerObj, frame);

    close all;

end



close(writerObj); % Saves the movie.



%Fermi energy calculated based on graphs, not sure about how to find exact

%fermi energy, and how to scale the magnetic feuld, or the relevance of Ec,

%as well as the proper step size or the final values. Help with these is

%needed
