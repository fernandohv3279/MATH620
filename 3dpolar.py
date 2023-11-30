import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Create the mesh in polar coordinates and compute corresponding Z.
r = np.linspace(0, 1.25, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)
# Z = ((R**2 - 1)**2)

Z = np.sin(np.arctan(np.tan(P)))

# Express the mesh in the cartesian system.
X, Y = R*np.cos(P), R*np.sin(P)

# x, y = np.linspace(-1.25, 1.25, 100), np.linspace(-1.25, 1.25, 100)
# X, Y = np.meshgrid(x,y)
# Z = np.sin(np.arctan(Y/X))

# Plot the surface.
ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)

# Tweak the limits and add latex math labels.
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
# ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_xlabel("x")
# ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_ylabel("y")
# ax.set_zlabel(r'$V(\phi)$')

plt.show()
