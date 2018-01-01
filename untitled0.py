#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 22:36:08 2017

@author: zhaoyiting
"""

import numpy as np

from pylab import *
from math import *
import random

#initialization
def Random_walk():
    x=[0]
    x2=[0]
    global n
    n=1000

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
n=1000
time=range(n+1)
m=500
x_1=Random_walk()[0]
x_2=Random_walk()[0]
x2=Random_walk()[1]
for i in range(m):
    x2=x2+Random_walk()[1]
x2=x2/(m+1)


figure(figsize=[16,8])
subplot(121)
plot(time,x_1)
plot(time,x_2)
xlim(0,1000)
xlabel('step number')
#ylim(-1,1)
ylabel('x')
title('Random walk in one dimension')
subplot(122)
scatter(time,x2,s=1)
plot(time,time)
xlim(0,1000)
xlabel('step number')
ylim(0,1000)
ylabel('$<x^2>$')
title('Random walk in one dimension')
savefig('Random walk 1D.png')
show()