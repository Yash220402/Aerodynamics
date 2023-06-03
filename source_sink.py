import math 
import numpy
import matplotlib as plt
import matplotlib.pyplot as plt

N = 50
x_start, x_end = -2.0, 2.0
y_start, y_end = -1.0, 1.0

x = numpy.linspace(x_start, x_end, N)
y = numpy.linspace(y_start, y_end, N)

X, Y = numpy.meshgrid(x, y)  # create meshgrid

width = 10
height = (y_end - y_start) / (x_end - x_start) * width
plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)
plt.xlim(x_start, x_end)
plt.ylim(y_start, y_end)
plt.scatter(X, Y, s=5, color="red", marker='o')
plt.show()

# Source Flow
strength_source = 5.0
x_source, y_source = -1.0, 0.0

# compute the velocity field on the mesh grid
u_source = (strength_source / (2*math.pi) * (X-x_source) / ((X-x_source)**2 + (Y-y_source)**2))
v_source = (strength_source / (2*math.pi) * (Y-y_source) / ((X-x_source)**2 + (Y-y_source)**2))

# plot the streamlines
width = 10.0
height = (y_end - y_start) / (x_end - x_start) * width
plt.figure(figsize==(width, height))
plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)
plt.xlim(x_start, x_end)
plt.ylim(y_start, y_end)
plt.streamplot(X, Y, u_source, v_source, density=2, linewidth=1, arrowsize=2, arrowstyle="->")
plt.scatter(x_source, y_source, color="#CD2305", s=80, marker='o')
plt.show()