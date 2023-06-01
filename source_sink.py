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