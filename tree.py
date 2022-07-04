#原帖https://www.zhihu.com/question/271643290 在@Milo Yip的基础上加了入射投影shadow效果以及调色
from turtle import *
from random import *
from math import *
shadow = Pen()
shadow.pencolor(0.3, 0.3, 0.3)

A = 0
B = -1.4#1.73
C = 1
a0 = 0
b0 = -300
c0 = 0
D = -(A*a0+B*b0+C*c0)

# rotatex = 1
# rotatey = 0
# rotatez = 0
# theta = 90

angle = 45
def cal_t(a, b, c):
    return -(A*a+B*b+C*c+D)/(A*A+B*B+C*C)

def cal_x(a, t):
    return A*t+a
def cal_y(b, t):
    return B*t+b 
def cal_z(c, t):
    return C*t+c 

def rol_x(beta, x, y, z):
    return x*cos(beta) + z*sin(beta)
def rol_y(beta, x, y, z):
    return y
def rol_z(beta, x, y, z):
    return -x*sin(beta) + z*cos(beta)

# def rotate3D(x, y, z, vx, vy, vz, theta):
#     c = cos(theta)
#     s = sin(theta)
#     new_x = (vx*vx*(1 - c) + c) * x + (vx*vy*(1 - c) - vz*s) * y + (vx*vz*(1 - c) + vy*s) * z
#     new_y = (vy*vx*(1 - c) + vz*s) * x + (vy*vy*(1 - c) + c) * y + (vy*vz*(1 - c) - vx*s) * z
#     new_z = (vx*vz*(1 - c) - vy*s) * x + (vy*vz*(1 - c) + vx*s) * y + (vz*vz*(1 - c) + c) * z
#     return new_x, new_y, new_z

def GOX(x, y):
    t = cal_t(x,y,0)
    x_ = cal_x(x, t)
    y_ = cal_y(y, t)
    z_ = cal_z(0, t)
    return rol_x(angle, x_, y_, z_)

def GOY(x, y):
    t = cal_t(x,y,0)
    x_ = cal_x(x, t)
    y_ = cal_y(y, t)
    z_ = cal_z(0, t)
    return rol_y(angle, x_, y_, z_)

def tree(n, l):
    pd()
    shadow.pd()
    t = cos(radians(heading() + 45)) / 8 + 0.25
    #pencolor(t, t* 1.25, t *0.55) #85,107,47
    #pencolor(t, t* 0.67, t *0.39) #244，164，95
    #pencolor(t, t* 0.51, t *0.98) #218, 112, 214
    pencolor(t, t, 0) #255, 255, 0
    pensize(n / 2)
    shadow.pensize(n / 4)
    forward(l)
    x, y = pos()
    shadow.goto(GOX(x, y), GOY(x, y))
    if (n > 0):
        b = random() * 15 + 10
        c = random() * 15 + 10
        d = l * (random() * 0.35 + 0.6)
        right(b)
        x, y = pos()
        shadow.goto(GOX(x, y), GOY(x, y))
        tree(n - 1, d)
        left(b + c)
        x, y = pos()
        shadow.goto(GOX(x, y), GOY(x, y))
        tree(n - 1, d)
        right(c)
        x, y = pos()
        shadow.goto(GOX(x, y), GOY(x, y))
    else:
        right(90)
        x, y = pos()
        shadow.goto(GOX(x, y), GOY(x, y))
        n = cos(radians(heading() - 45)) / 4 + 0.5
        #pencolor(n, n * 1.25, n * 0.55)
        #pencolor(n, n* 0.67, n *0.39) #244，164，95
        #pencolor(n, n* 0.51, n *0.98) #218, 112, 214
        pencolor(n, n, 0) #255, 255, 0
        circle(2)
        left(90)
        x, y = pos()
        shadow.goto(GOX(x, y), GOY(x, y))
    pu()
    shadow.pu()
    backward(l)
    x, y = pos()
    shadow.goto(GOX(x, y), GOY(x, y))

bgcolor(0.5, 0.5, 0.5)
ht()
shadow.ht()
speed(0)
tracer(0,0)
left(90)
shadow.left(90)

pu()
backward(300)
shadow.pu()
shadow.backward(300)
tree(12, 80)
shadow.tilt(90)
done()
