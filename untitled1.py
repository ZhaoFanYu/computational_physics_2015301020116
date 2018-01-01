#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 21:39:37 2017

@author: zhaoyiting
"""
# random walks in 2D
import numpy as np

from pylab import *
from math import *
import random

#initialization
def Random_walk1():
    x=[50]
    x2=[0]
    global n
    n=500

    for i in range(n):
        r=random.uniform(0,1)
        if r<0.5:
            x.append(x[i]+1)
        else:
            x.append(x[i]-1)
        x2.append(x[i+1]**2)
        #print r
    x2=array(x2)
    return [x,x2]
def Random_walk2():
    y=[50]
    y2=[0]
    global n
    n=500

    for i in range(n):
        r=random.uniform(0,1)
        if r<0.5:
            y.append(y[i]+1)
        else:
            y.append(y[i]-1)
        y2.append(y[i+1]**2)
        #print r
    y2=array(y2)
    return [y,y2]
n=1000
time=range(n+1)
m=500
x_1=Random_walk1()[0]
y_1=Random_walk2()[0]
x_2=Random_walk1()[0]
y_2=Random_walk2()[0]
x_3=Random_walk1()[0]
y_3=Random_walk2()[0]
x2=Random_walk()[1]
for i in range(m):
    x2=x2+Random_walk()[1]
x2=x2/(m+1)


figure(figsize=[16,8])
subplot(121)
plot(x_1,y_1)

xlim(0,100)
ylim(0,100)
xlabel('x')
#ylim(-1,1)
ylabel('y')
title('Random walk in two dimension-one particle')

subplot(122)
#scatter(time,x2,s=1)
plot(x_3,y_3)
plot(x_2,y_2)
xlim(0,100)
xlabel('x')
ylim(0,100)
ylabel('y')
title('Random walk in one dimension-two particles')
#savefig('Random walk 1D.png')

show()