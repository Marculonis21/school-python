import ShapeGr as gr
import turtle as t


class RocketGr(gr.Point):    
    
    def __init__(self, color="black", size=10, angle=0):
        self.x = 0
        self.y = 0
        self.size = size
        self.angle = angle
        self.color = color
        
    def screenSize(self,pos=-1):
        width = t.Screen().window_width()
        height = t.Screen().window_height()
        
        if(pos == -1):
            return(width,height)
        elif(pos == 0):
            return(width)
        elif(pos == 1):
            return(height)

    def draw(self, color='white'):
        print("a")
        t.down()
        t.pencolor(color)
    
        t.begin_fill()
        for i in range(4):
            t.forward(10*self.size)
            t.right(100)
        
        t.end_fill()
        
    def move(self, x, y):
        t.up()
        t.setpos(x, y)
        self.x = x
        self.y = y
        
    def set_color(self, color="black"):
        self.color = color

if __name__ == "__main__":
    rocket = RocketGr(size = 20)
    rocket.set_color("red")

    print(rocket.color)
    rocket.move(-400,100)
    rocket.show()

    
