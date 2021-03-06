from sympy import Matrix, Symbol, symbols, solveset, solve, simplify, S, diff, det, erf, log, sqrt, pi, sin, cos, tan, asin, acos, atan2, init_printing, pretty_print
import numpy as np
import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D

theta0 = 0
theta1 = 0
theta2 = 0
theta3 = 0
theta4 = 0
theta5 = 0
theta6 = 0

theta0 = np.deg2rad(theta0)
theta1 = np.deg2rad(theta1)
theta2 = np.deg2rad(theta2)
theta3 = np.deg2rad(theta3)
theta4 = np.deg2rad(theta4)
theta5 = np.deg2rad(theta5)
theta6 = np.deg2rad(theta6)

a1 = 500
a2 = 1300
a3 = -55
a4 = 0
a5 = 0
a6 = 0

d1 = 1045
d2 = 0
d3 = 0
d4 = 1025
d5 = 0
d6 = 290

alpha1 = 90*(pi/180)
alpha2 = 0*(pi/180)
alpha3 = 90*(pi/180)
alpha4 = -90*(pi/180)
alpha5 = 90*(pi/180)
alpha6 = 0*(pi/180)

#d-h parameters table

p0 = [0, 0, 0, 1]
p0x = (p0[0])
p0y = (p0[1])
p0z = (p0[2])
print(p0)


d_h_table_0_1 = np.array([[cos(theta1), -sin(theta1)*cos(alpha1), sin(theta1)*sin(alpha1), a1*cos(theta1)],
                        [sin(theta1), cos(theta1)*cos(alpha1), -cos(theta1)*sin(alpha1), a1*sin(theta1)],
                        [0, sin(alpha1), cos(alpha1), d1],
                        [0, 0, 0, 1]])

transform_0_1 = d_h_table_0_1
last_column1 = transform_0_1[:, 3]
p1 = np.delete(last_column1, 3, 0)
print(p1)
p1x = np.unique(p1[0])
p1y = np.unique(p1[1])
p1z = np.unique(p1[2])




d_h_table_1_2 = np.array([[cos(theta2), -sin(theta2)*cos(alpha2), sin(theta2)*sin(alpha2), a2*cos(theta2)],
                        [sin(theta2), cos(theta2)*cos(alpha2), -cos(theta2)*sin(alpha2), a2*sin(theta2)],
                        [0, sin(alpha2), cos(alpha2), d2],
                        [0, 0, 0, 1]])

transform_1_2 = transform_0_1 @ d_h_table_1_2
last_column2 = transform_1_2[:, 3]
p2 = np.delete(last_column2, 3, 0)
print(p2)
p2x = np.unique(p2[0])
p2y = np.unique(p2[1])
p2z = np.unique(p2[2])



d_h_table_2_3 = np.array([[cos(theta3), -sin(theta3)*cos(alpha3), sin(theta3)*sin(alpha3), a3*cos(theta3)],
                          [sin(theta3), cos(theta3)*cos(alpha3), -cos(theta3)*sin(alpha3), a3*sin(theta3)],
                          [0, sin(alpha3), cos(alpha3), d3],
                          [0, 0, 0, 1]])

transform_2_3 = transform_1_2 @ d_h_table_2_3
last_column3 = transform_2_3[:, 3]
p3 = np.delete(last_column3, 3, 0)
print(p3)
p3x = np.unique(p3[0])
p3y = np.unique(p3[1])
p3z = np.unique(p3[2])


d_h_table_3_4 = np.array([[cos(theta4), -sin(theta4)*cos(alpha4), sin(theta4)*sin(alpha4), a4*cos(theta4)],
                          [sin(theta4), cos(theta4)*cos(alpha4), -cos(theta4)*sin(alpha4), a4*sin(theta4)],
                          [0, sin(alpha4), cos(alpha4), d4],
                          [0, 0, 0, 1]])

transform_3_4 = transform_2_3 @ d_h_table_3_4
last_column4 = transform_3_4[:, 3]
p4 = np.delete(last_column4, 3, 0)
print(p4)
p4x = np.unique(p4[0])
p4y = np.unique(p4[1])
p4z = np.unique(p4[2])

d_h_table_4_5 = np.array([[cos(theta5), -sin(theta5)*cos(alpha5), sin(theta5)*sin(alpha5), a5*cos(theta5)],
                          [sin(theta5), cos(theta5)*cos(alpha5), -cos(theta5)*sin(alpha5), a5*sin(theta5)],
                          [0, sin(alpha5), cos(alpha5), d5],
                          [0, 0, 0, 1]])

transform_4_5 = transform_3_4 @ d_h_table_4_5
last_column5 = transform_4_5[:, 3]
p5 = np.delete(last_column5, 3, 0)
print(p5)
p5x = np.unique(p5[0])
p5y = np.unique(p5[1])
p5z = np.unique(p5[2])

d_h_table_5_6 = np.array([[cos(theta6), -sin(theta6)*cos(alpha6), sin(theta6)*sin(alpha6), a6*cos(theta6)],
                          [sin(theta6), cos(theta6)*cos(alpha6), -cos(theta6)*sin(alpha6), a6*sin(theta6)],
                          [0, sin(alpha6), cos(alpha6), d6],
                          [0, 0, 0, 1]])

transform_5_6 = transform_4_5 @ d_h_table_5_6
last_column6 = transform_5_6[:, 3]
p6 = np.delete(last_column6, 3, 0)
p6x = np.unique(p6[0])
p6y = np.unique(p6[1])
p6z = np.unique(p6[2])
print(p6)

#multiplying to find transformation from frame 0 to 6
#(@ symbol used for matrix multiplication)

transform_0_6 = d_h_table_0_1 @ d_h_table_1_2 @ d_h_table_2_3 @ d_h_table_3_4 @ d_h_table_4_5 @ d_h_table_5_6

#defining the variables I want to use as symbols
theta1,theta2,theta3,theta4,theta5,theta6 = symbols('theta_1 theta_2 theta_3 theta_4 theta_5 theta_6')
theta = Matrix([theta1,theta2,theta3,theta4,theta5,theta6])

init_printing()

print('T1=',T1,'\n\nT2=',T2,'\n\nT3=',T3,'\n\nT4=',T4,'\n\nT5=',T5,'\n\nT6=',T6)
print('p1=',p1,'\n\np2=',p2,'\n\np3=',p3,'\n\np4=',p4,'\n\np5=',p5,'\n\np6=',p6)

