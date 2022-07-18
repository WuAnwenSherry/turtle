from turtle import *
from random import *
from math import *

def rgba2rgb( r, g, b, a, background_r, background_g, background_b):

    Res_R = r * a + (1.0 - a) * background_r
    Res_G = g * a + (1.0 - a) * background_g
    Res_B = b * a + (1.0 - a) * background_b

    return Res_R, Res_G, Res_B

R = 10
m = 5
rangeMax = ceil(sqrt(pow(R, m)))
factor = 0.8
def isInSphere(x,y):
    if(x*x + y*y < rangeMax*rangeMax/4):
        return True
    return False

def isInStar(x,y):
    if(pow(x*x, 1/m) + pow(y*y, 1/m) < R):
        return True
    return False

def drawSounding(x, y):
    if(random() < 0.5):
        return
    setx(x)
    sety(y)
    pd()
    a = 1 - sqrt((x*x+y*y)/(rangeMax*rangeMax))
    if a > 1:
        a = 1
    elif a<0:
        a = 0
    r, g, b = rgba2rgb(1,1,1,a*factor,0,0,0.6)
    pencolor(r,g,b)
    dot()
    pu()

def drawstarXYZ(x, y):
    setx(x)
    sety(y)
    pd()
    a = 1 - sqrt((x*x+y*y)/(rangeMax*rangeMax))
    if a > 1:
        a = 1
    elif a < 0:
        a = 0
    r, g, b = rgba2rgb(1,1,1,a,0,0,0.6)
    pencolor(r,g,b)
    dot()
    pu()

bgcolor(0, 0, 0.6)
ht()

speed(0)
tracer(0,0)

pu()

for x_sample in range(-rangeMax,rangeMax):
    for y_sample in range(-rangeMax,rangeMax):
        if (isInStar(x_sample, y_sample)):
            drawstarXYZ(x_sample,y_sample)
        if isInSphere(x_sample, y_sample):
            drawSounding(x_sample, y_sample)

done()
