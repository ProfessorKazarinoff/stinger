import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

nx = 1080
ny = 720

fig = plt.figure()
plt.axis([0,nx,0,ny])
ax = plt.gca()
ax.set_aspect(1)
x = np.arange(0,10,1)
y = x
def init():
    # initialize an empty list of cirlces
    return []

def animate(i):
    # draw circles, select to color for the circles based on the input argument i. 
    someColors = ['r', 'b', 'g', 'm', 'y']
    patches = []
    patches.append(ax.add_patch(plt.Rectangle(
        xy=(i,0.5*i),width=5*i,height=5*i,angle=.3*i
        )))
    return patches

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1080, interval=10, blit=True)
plt.show()
