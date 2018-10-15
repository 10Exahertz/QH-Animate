#import matplotlib
#matplotlib.use('Agg')
# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
# import pylab as py
# import matplotlib.animation as animation
# from matplotlib.animation import FuncAnimation

# fig = plt.figure()
# ax = plt.axes(xlim=(0, 3.5e-3), ylim=(0, 1))
# line, = ax.plot([], [], lw=2)

# def init():
#    line.set_data([], [])
#    return line,

# # Set up formatting for the movie files
# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)


# Gamma=0.0005
# q=1.6e-19
# m=0.067*9e-31
# B=10
# Ec=(1.0567e-34)*B/m
# e=2.78

# for x in xrange(1,15):
# 	pass
# 	def update(i):
# 			plt.ylabel('DOS')
# 			plt.xlabel('Energy')
# 			plt.title('QH Animation')
# 			E=np.linspace(0,3.4e-3,200)
# 			E0=0+(1.0567e-34)*x*i/m #x is just an iteration of lines, can put in any number
# 			QH = e**(-(E-E0)**2/Gamma**2)
# 			line.set_data(E,QH)

# 			return line, 

# #compose plot

# anim = animation.FuncAnimation(fig, update,frames=np.linspace(0,2,100),init_func=init, blit=True)
# anim.save('QHanimate.mp4', writer=writer)

# plt.show()


##plt.show()
#Gamma=0.0005
#q=1.6e-19
#m=0.067*9e-31
#B=10
#Ec=(1.0567e-34)*B/m
#e=2.78

#for x in xrange(1,15):
#	pass
#	E=np.linspace(0,3.5e-3,200)
#	E0=0+(1.0567e-34)*x*.1/m #x is just an iteration of lines, can put in any number
#	QH = e**(-(E-E0)**2/Gamma**2)
#compose plot
#	py.plot(E,QH)
#py.ylabel('Energy')
#py.xlabel('Magnetic Field')
#py.title('LL Fan Diagram')
#py.show(), this method works as expected for one image
#import matplotlib
#matplotlib.use("nbagg")

import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import matplotlib.animation as animation
import pylab as p

Gamma=0.0002
q=1.6e-19
m=0.067*9e-31
B=10
Ec=(1.0567e-34)*B/m
#e=2.78

#E0=0+(1.0567e-34)*x*i/m

fig, ax = plt.subplots()

plt.xticks([3.47e-3], ["$E_F$"])
plt.ylabel('DOS')
plt.xlabel('Energy')
plt.title('Quantum Hall Landau Level Animation')
plt.axvline(x=3.47e-3,color='black',linestyle='--', linewidth = 1, zorder = 200)#x here is the fermi energyof the system

n = 60 #number of lines
x = np.arange(0, 4e-3, 1.7e-5)        # x-array, third number is interval here, x is energy
lines = [ax.plot(x, np.e**(-(x-((1.0567e-34)*1*1/m))**2/Gamma**2),color='b', zorder=i+3)[0] for i in range(n)]
fills = [ax.fill_between(x,0,(np.e**(-(x-((1.0567e-34)*1*1/m))**2/Gamma**2)), facecolor='b', zorder=i+3) for i in range(n)]


def animate(i):
    for d, line in enumerate(lines):
        p=(d+1)/2.
        line.set_ydata(np.e**((-(x-((1.0567e-34)*p*i/m))**2)/Gamma**2))
        fills[d].remove()
        fills[d] = ax.fill_between(x,0,(np.e**(-(x-((1.0567e-34)*p*i/m))**2/Gamma**2)), facecolor='b', zorder=d+3)# update the data
    return lines + fills


#Init only required for blitting to give a clean slate.
def init():
    for line in lines:
        line.set_ydata(np.ma.array(x, mask=True))
    return lines

ani = animation.FuncAnimation(fig, animate, np.arange(.2, 3.0, .01), init_func=init, #0.2 is the starting point for time at 0 to make sim accurate
    interval=10, blit=True)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=25, metadata=dict(artist='Me'), bitrate=5000)

ani.save('QHanimati3.mp4', writer=writer)



plt.show()
