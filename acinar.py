#imports
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#the function to make the plot
def function_z(x,y):
    return 50 - (x**2 + y**2) #note: I changed the powers by 2 each time in the gif to show the flattening cuboid effect of the transformation

#how many data points I want to use/how dense or sparse I want them to be placed
N=10
x_values = np.linspace(-5,5,N)
y_values = np.linspace(-5,5,N)

#to create the mesh look on the graph
X,Y = np.meshgrid(x_values, y_values)

Z = function_z(X,Y)

#Making the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')  #'viridis' shows the curvature-like map

#Adding labels and the title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.plot_wireframe(X,Y,Z)

#how to hide the numbers of the axes (since we are not looking at scale)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])

#model the title
ax.set_title('Plot of Z = 50 - (x^2 + y^2)', fontweight='bold', pad=-50,)

#Adjust the layout of the plot
ax.view_init(elev=30, azim=70)

#Show the plot
plt.show()
