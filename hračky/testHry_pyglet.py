#!/usr/bin/env python
import pyglet
from pyglet.gl import *

window = pyglet.window.Window(500,500,"TEST SCENE",resizable=True)

setSize = 50
playField = []
PRESSDRAW = False

mousePosX = 0
mousePosY = 0

mouseX = -1
mouseY = -1
    
def drawLine(startX, startY, endX, endY, r=1,g=1,b=1):
    glBegin(GL_LINES)
    glColor3f(r,g,b)
    glVertex2f(int(startX), int(startY))
    glVertex2f(int(endX), int(endY))
    glEnd()

def drawRect(x,y,sizeX,sizeY, r=1,g=1,b=1):
    glBegin(GL_QUADS)
    glColor3f(r,g,b)
    glVertex2f(int(x), int(y))
    glVertex2f(int(x+sizeX), int(y))
    glVertex2f(int(x+sizeX), int(y+sizeY))
    glVertex2f(int(x), int(y+sizeY))
    glEnd()

def drawX(posX,posY):
    posX += setSize/2
    posY += setSize/2
    label = pyglet.text.Label("X",
                              font_size=setSize-8,
                              anchor_x='center',
                              anchor_y='center')
    label.x = posX
    label.y = posY+2
    
    label.draw()

def drawO(posX,posY):
    posX += setSize/2
    posY += setSize/2
    label = pyglet.text.Label("O",
                              font_size=setSize-8,
                              anchor_x='center',
                              anchor_y='center')

    label.x = posX
    label.y = posY+2
    
    label.draw()

def boardCheck():
    global playField
    a = []
    b = []
    
    for i in range(len(playField)):
        if(i%2 == 0):
            a+=playField[i]
        else:
            b+=playField[i]
            

@window.event
def on_draw():
    global PRESSDRAW
    glClearColor(0.1,0.1,0.1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    numX = int(window.width/setSize) + 1
    numY = int(window.height/setSize) + 1

    global mouseX,mouseY
    mouseX = -1
    mouseY = -1
    for x in range(numX):
        drawLine(x*setSize,0,x*setSize,window.height)
        if(x*setSize > mousePosX and mouseX == -1):
            mouseX = x-1
            
    for y in range(numY):
        drawLine(0,y*setSize,window.width,y*setSize)
        if(y*setSize > mousePosY and mouseY == -1):
            mouseY = y-1

    if(PRESSDRAW):
        drawRect(mouseX*setSize, mouseY*setSize+1, setSize-1,setSize-1, 0.5,0.5,0.5)
        PRESSDRAW = False
    else:
        drawRect(mouseX*setSize, mouseY*setSize+1, setSize-1,setSize-1, 0.3,0.3,0.3)

    TURN = 0
    #print(playField)
    for item in playField:
        if(TURN == 0):
            drawO(item[0]*setSize,item[1]*setSize)
            TURN = 1
        elif(TURN == 1):
            TURN = 0
            drawX(item[0]*setSize,item[1]*setSize)
    
    
@window.event
def on_mouse_motion(x,y,dx,dy):
    global mousePosX, mousePosY

    mousePosX = x
    mousePosY = y
    
@window.event
def on_mouse_release(x,y,mod,plus):
    global playField,PRESSDRAW
    

    if not ([mouseX,mouseY] in playField):
        PRESSDRAW = True
        playField += [[mouseX,mouseY]]
        print("press")
        print(playField)

def tik(t):
    #print(t)
    pass

pyglet.clock.schedule_interval(tik,1/60)    
pyglet.app.run()
