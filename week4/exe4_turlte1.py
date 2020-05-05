# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:51:55 2020

@author: mcsbi
"""

import random
import turtle

def isInScreen (w,t):
    if random.random() > 0.1:
        return True
    else:
        return False
    
t = turtle.Turtle()
wn = turtle.Screen()


t.shape("turtle")

while isInScreen (wn, t):
    coin = random.randrange(0, 2)
    if coin ==0:
        t.left(90)
    else:
        t.right(90)
        
    t.forward(50)
wn.exitonclick()
        
