import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


sigma = 10
rho = 28
beta = 8 / 3


dt = 0.01
total_time = 20


x, y, z = 0.0, 1.0, 1.05


steps = int(total_time / dt)

xs = np.empty(steps)
ys = np.empty(steps)
zs = np.empty(steps)


xs[0], ys[0], zs[0] = x, y, z


for i in range(1, steps):
    dx = sigma * (ys[i - 1] - xs[i - 1]) * dt
    dy = (xs[i - 1] * (rho - zs[i - 1]) - ys[i - 1]) * dt
    dz = (xs[i - 1] * ys[i - 1] - beta * zs[i - 1]) * dt
    xs[i] = xs[i - 1] + dx
    ys[i] = ys[i - 1] + dy
    zs[i] = zs[i - 1] + dz


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim((-20, 20))
ax.set_ylim((-30, 30))
ax.set_zlim((0, 50))


line, = ax.plot([], [], [], lw=0.8, color='blue')


def update(num):
    line.set_data(xs[:num], ys[:num])
    line.set_3d_properties(zs[:num])
    return line,
ani = FuncAnimation(fig, update, frames=steps, interval=20, blit=True)

plt.show()
