import matplotlib.pyplot as plt
import numpy
import matplotlib.pyplot
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sympy import Matrix, Symbol, symbols, solveset
from sympy import S, erf, log, sqrt, pi, sin, cos, tan
from sympy import init_printing

#kinematics simulator

#d-h parameters in mm
a1 = 500
a2 = 1300
a3 = 55
a4 = 0
a5 = 0
a6 = 0

d1 = 1045
d2 = 0
d3 = 0
d4 = 1025
d5 = 290
d6 = 0

theta1 = 0
theta2 = 0
theta3 = 0
theta4 = 0
theta5 = 0
theta6 = 0

alpha1 = -90*(pi/180)
alpha2 = 0*(pi/180)
alpha3 = 90*(pi/180)
alpha4 = -90*(pi/180)
alpha5 = 90*(pi/180)
alpha6 = 0*(pi/180)

#p1 to p6 are points in 3D space defined as symbolic matrices that can be transformed mathematically
#note that they are 4 dimensional so they can be used with homogenous transforms with the last 'W' coordinate always 1
#(to facilitate translation as well as rotation)
#p1 = Matrix([0, 0, 0, 1])
#p2 = Matrix([a1, 0, d1, 1])
#p3 = Matrix([a1, 0, d1+a2, 1])
#p4 = Matrix([a1+710, 0, d1+a2-a3, 1])
#p5 = Matrix([a1+d4, 0, d1+a2-a3, 1])
#p6 = Matrix([a1+d4+d6, 0, d1+a2-a3, 1])


#d-h parameters table

p0 = [0, 0, 0, 1]
p0x = (p0[0])
p0y = (p0[1])
p0z = (p0[2])


d_h_table_0_1 = np.array([[cos(theta1), -sin(theta1)*cos(alpha1), sin(theta1)*sin(alpha1), a1*cos(theta1)],
                        [sin(theta1), cos(theta1)*cos(alpha1), -cos(theta1)*sin(alpha1), a1*sin(theta1)],
                        [0, sin(alpha1), cos(alpha1), d1],
                        [0, 0, 0, 1]])

transform_0_1 = d_h_table_0_1
last_column1 = transform_0_1[:, 3]
p1 = np.delete(last_column1, 3, 0)
#print(p1)
p1x = np.unique(p1[0])
p1y = np.unique(p1[1])
p1z = np.unique(p1[2])



d_h_table_1_2 = np.array([[cos(theta2), -sin(theta2)*cos(alpha2), sin(theta2)*sin(alpha2), a2*cos(theta2)],
                        [sin(theta2), cos(theta2)*cos(alpha2), -cos(theta2)*sin(alpha2), a2*sin(theta2)],
                        [0, sin(alpha2), cos(alpha2), d2],
                        [0, 0, 0, 1]])

transform_1_2 = d_h_table_1_2
last_column2 = transform_1_2[:, 3]
p2 = np.delete(last_column2, 3, 0)
p2x = p1x
#print(p2x)
p2y = np.unique(p2[1])
p2z = np.unique(p2[2]) +p1z + np.unique(p2[0])
#print(p2z)


d_h_table_2_3 = np.array([[cos(theta3), -sin(theta3)*cos(alpha3), sin(theta3)*sin(alpha3), a3*cos(theta3)],
                          [sin(theta3), cos(theta3)*cos(alpha3), -cos(theta3)*sin(alpha3), a3*sin(theta3)],
                          [0, sin(alpha3), cos(alpha3), d3],
                          [0, 0, 0, 1]])

transform_2_3 = d_h_table_2_3
last_column3 = transform_2_3[:, 3]
p3 = np.delete(last_column3, 3, 0)
p3x = p1x + 710
#print(p3x)
p3y = np.unique(p3[1])
p3z = p2z - np.unique(p3[0])
#print(p3z)

d_h_table_3_4 = np.array([[cos(theta4), -sin(theta4)*cos(alpha4), sin(theta4)*sin(alpha4), a4*cos(theta4)],
                          [sin(theta4), cos(theta4)*cos(alpha4), -cos(theta4)*sin(alpha4), a4*sin(theta4)],
                          [0, sin(alpha4), cos(alpha4), d4],
                          [0, 0, 0, 1]])

transform_3_4 = d_h_table_3_4
last_column4 = transform_3_4[:, 3]
p4 = np.delete(last_column4, 3, 0)
p4x = p2x + np.unique(p4[2])
print(p4x)
p4y = np.unique(p4[1])
p4z = p3z

d_h_table_4_5 = np.array([[cos(theta5), -sin(theta5)*cos(alpha5), sin(theta5)*sin(alpha5), a5*cos(theta5)],
                          [sin(theta5), cos(theta5)*cos(alpha5), -cos(theta5)*sin(alpha5), a5*sin(theta5)],
                          [0, sin(alpha5), cos(alpha5), d5],
                          [0, 0, 0, 1]])

transform_4_5 = d_h_table_4_5
last_column5 = transform_4_5[:, 3]
p5 = np.delete(last_column5, 3, 0)
p5x = p4x + np.unique(p5[2])
p5y = np.unique(p5[1])
p5z = p4z

d_h_table_5_6 = np.array([[cos(theta6), -sin(theta6)*cos(alpha6), sin(theta6)*sin(alpha6), a6*cos(theta6)],
                          [sin(theta6), cos(theta6)*cos(alpha6), -cos(theta6)*sin(alpha6), a6*sin(theta6)],
                          [0, sin(alpha6), cos(alpha6), d6],
                          [0, 0, 0, 1]])

#multiplying to find transformation from frame 0 to 6
#(@ symbol used for matrix multiplication)

transform_0_6 = d_h_table_0_1 @ d_h_table_1_2 @ d_h_table_2_3 @ d_h_table_3_4 @ d_h_table_4_5 @ d_h_table_5_6

print("Homogeneous Matrix from frame 0 to frame 6:  ")
#print(transform_0_6)

#the final T vector contains the position of the end effector, the R matrix contains the orientation
#of the end effector

#trying to print out t, I need to get rid of the fourth value
last_column = transform_0_6[:, 3]
#print(last_column)

end_effector_positon = np.delete(last_column, 3, 0)
#print(end_effector_positon)

#creating axis
fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(111, projection='3d')

#add axis labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

#add axis limits
ax.set_xlim([-200, 2000])
ax.set_ylim([-200, 2000])
ax.set_zlim([-200, 2000])


ux = np.unique(end_effector_positon[0])
uy = np.unique(end_effector_positon[1])
uz = np.unique(end_effector_positon[2])


#adding the final end effector position to the plot
ax.plot3D(ux, uy, uz, 'red', marker="o")
ax.plot3D(p0x, p0y, p0z, 'blue', marker="o")
ax.plot3D(p1x, p1y, p1z, 'blue', marker="o")
ax.plot3D(p2x, p2y, p2z, 'blue', marker="o")
ax.plot3D(p3x, p3y, p3z, 'blue', marker="o")
ax.plot3D(p4x, p4y, p4z, 'blue', marker="o")
ax.plot3D(p5x, p5y, p5z, 'blue', marker="o")

#showing plot
matplotlib.pyplot.show()

#trying to extract values from tables