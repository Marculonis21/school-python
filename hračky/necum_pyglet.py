#!/usr/bin/env python3

import pyglet
from pyglet.gl import *
import random

COLORS = [(0,255,0,255),(0,0,255,255),(55,55,55,255),(255,0,255,255),(255,255,0,255),(0,255,255,255)]

colorPoint = random.choice(COLORS)

window = pyglet.window.Window(900,500,"Pyglet+OpenGL")

clicks = 0
xX = []
yY = []


def tik(t):
    #print(t)
    pass

def line(startx,starty,endx,endy):
    glBegin(GL_LINE_STRIP)
    for i in range(clicks):
        glVertex2f(int(xX[i]),int(yY[i]))
    glEnd()
    
    
pyglet.clock.schedule_interval(tik, 1/30)

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glColor3f(0,0,0)
    glVertex2f(window.width/2, 0)
    glColor3f(0.5,0.5,0.5)
    glVertex2f(0, window.height)
    glColor3f(1,1,1)
    glVertex2f(window.width, window.height)
    glEnd()

    line(20,20,500,500)



    
    labelX = pyglet.text.Label("Nečum!!",
                          font_size = 72,
                          x = window.width/2,
                          y = window.height/2,
                          anchor_x='center',
                          color = colorPoint)
    labelX.draw()

@window.event
def on_mouse_press(x,y,but,mod):
    global colorPoint
    print(x,y,but,mod)
    colorPoint = random.choice(COLORS)
    print(colorPoint)
    global xX,yY,clicks
    
    xX.append(x)
    yY.append(y)
    clicks += 1
    
pyglet.app.run()

