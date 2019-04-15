#!/usr/bin/env python3
"""
Tento modul poskytuje třídu Point
"""

import math, turtle as t
from random import *

class Point:
    def __init__(self, x=0, y=0, color='black', size=5):
        """ 2D kartézská souřadnice """
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.track = False


    def draw(self, color='white'):
        """ vykresli objekt """
        t.down() if self.track else t.up()
        t.pencolor(color)
        t.setpos(self.x, self.y)
        t.down()
        t.dot(self.size)
        
    def show(self):
        """ zobrazit objekt """
        self.draw(self.color)            

    def hide(self):
        """ zhasnout objekt """
        self.draw()

    def move(self,x ,y):
        """ přesunout objekt na souřadnice """
        t.up()
        t.setpos(self.x, self.y)
        if not self.track:
            self.hide()
        self.x = x
        self.y = y
        self.show()

    def set_track(self,tr=True):
        self.track = tr

    def distance_from_origin(self):
        """ vzdálenost bodu od počátku """
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Point({0.x!r}, {0.y!r}, {0.color}, {0.size})".format(self)

    def __str__(self):
        return "({0.x!r}, {0.y!r}, {0.color}, {0.size})".format(self)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

t.hideturtle()

if __name__ == "__main__":
    t.speed(10)
    p1 = Point(100,50,'red',20)
    p2 = Point(50,100,'blue',20)
    p1.show()
    p2.show()
    for i in range(randint(10,20)):
        p1.move(randint(-300,300), randint(-300,300))
        p2.move(randint(-300,300), randint(-300,300))
        print(p1,p2)
    p3 = Point(70,70,'green',10)
    p3.show()
    p3.set_track()
    p1.set_track()
    p2.set_track()
    for i in range(randint(10,500)):
        p3.move(randint(-400,400), randint(-400,400))
        p1.move(randint(-300,300), randint(-300,300))
        p2.move(randint(-300,300), randint(-300,300))

    input()
