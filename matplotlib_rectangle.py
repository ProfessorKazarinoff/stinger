# matplotlib_animation.py
"""
A Python script to run a Matplotlib animation to build a stinger transition
"""

#import necessary packages
import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Create figure and axes
fig,ax = plt.subplots()
x = np.arange(0,1280,1)
y = (720/1280)*x


# Create a Rectangle patch
rect = patches.Rectangle((50,100),50,20,angle=50,linewidth=0,edgecolor='b',facecolor='b')

# Add the patch to the Axes
ax.set_xlim([0,1280])
ax.set_ylim([0,720])
patch = ax.add_patch(rect)

def init():
    patch.rect

def animate(i):
    patch.rect((x[i],y[i]),50,20,angle=i,linewidth=0,edgecolor='b',facecolor='b')
    return patch

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(x), interval=40, blit=True, repeat=False)

plt.show()