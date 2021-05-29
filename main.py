import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.gca(projection='3d')
t = np.linspace(0, 2 * np.pi, 100)
z = t
x = np.sin(z)
y = 2*np.cos(z)
ax.plot(x, y, z, label='Zad 1')
ax.legend()
plt.show()


np.random.seed(100000)
def rand(n, vmin,vmax):
    return (vmax - vmin) * np.random.rand(n) + vmin
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 2

for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    xs = rand(n, 23, 32)
    ys = rand(n, 0, 100)
    zs = rand(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()


fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
r = np.sqrt(x**2 + y**2)
z = np.sin(r)
surf = ax.plot_surface(x, y, z, cmap=cm.PuBu, linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()


fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
x, y = np.meshgrid(x, y)
r = np.sqrt(x**2 + y**2)
z = np.sin(r)
surf = ax.plot_surface(x, y, z, cmap=cm.Oranges, linewidth=0, antialiased=True)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
