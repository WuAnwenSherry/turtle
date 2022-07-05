from turtle import *
from random import *
from math import *

R = 200 #半径

L =  300 #光源位置
X_l = -L
Y_l = L
Z_l = L

factor = 0.9 #光源颜色
R_l = 0.8 * factor
G_l = 1 * factor
B_l = 0.44 * factor

def normal(x, y, z): #单位向量
    len = sqrt(x*x+y*y+z*z)
    return x/len, y/len, z/len

def dotproduct(x1,y1,z1,x2,y2,z2):#向量点积
    return x1*x2+y1*y2+z1*z2

def inSphere(x, y):
    return (x*x+y*y <= R*R)

def isShadowed(x,y,z,rx,ry,rz):
    if(x*rx+y*ry+z*rz > 0):
        return False
    return True

def sphereXYZ(x, y, z):
    setx(x)
    sety(y)
    pd()
    r_x_=X_l-x
    r_y_=Y_l-y
    r_z_=Z_l-z
    r_x, r_y, r_z = normal(r_x_, r_y_, r_z_)
    x_norm, y_norm, z_norm = normal(x,y,z)
    if (isShadowed(x_norm,y_norm,z_norm,r_x,r_y,r_z)):
        pencolor(0,0,0)
    else:
        pencolor(abs(R_l*dotproduct(x_norm,y_norm,z_norm,r_x,r_y,r_z)), abs(G_l*dotproduct(x_norm,y_norm,z_norm,r_x,r_y,r_z)), abs(B_l*dotproduct(x_norm,y_norm,z_norm,r_x,r_y,r_z))) #255, 255, 0
    dot()
    pu()

bgcolor(0.5, 0.5, 0.5)
ht()

speed(0)
tracer(2000,0)

pu()

for x_sample in range(-R,R):
    for y_sample in range(-R,R):
        if (inSphere(x_sample, y_sample)):
            z_sample = sqrt(R*R-x_sample*x_sample-y_sample*y_sample)
            sphereXYZ(x_sample,y_sample,z_sample)

done()
