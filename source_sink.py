import math 
import numpy
import matplotlib as plt

N = 50
x_start, x_end = -2.0, 2.0
y_start, y_end = -1.0, 1.0

x = numpy.linspace(x_start, x_end, N)
y = numpy.linspace(y_start, y_end, N)

X, Y = numpy.meshgrid(x, y)