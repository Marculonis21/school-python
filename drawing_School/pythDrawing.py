import ShapeGr as gr
import turtle as t


class DGraphics(gr.Point):
    
    SLIST = ["circle","point","rect","str"]
    
    
    def __init__(self, shape, x=0, y=0, color="black", size=10):
        
        while True:
            if(shape.lower() in self.SLIST):
                self.__shape__ = shape
                break
            else:
                print("INVALID SHAPE INPUT")
                shape = str(input("\nInput shape: "))

        self.x = x
        self.y = y
        self.color = color
        self.size = size

        self.track = False

    def draw(self):
        t.down() if self.track else t.up()
        t.pencolor(self.color)
        t.setpos(self.x,self.y)
        t.down()

        if(self.shape == "circle"):
            t.circle(self.size)
        elif(self.shape == "point"):
            t.dot(self.size)
        
    
    def screenSize(self,pos=-1):
        width = t.Screen().window_width()
        height = t.Screen().window_height()
        
        if(pos == -1):
            return(width,height)
        elif(pos == 0):
            return(width)
        elif(pos == 1):
            return(height)

if __name__ == "__main__":
    d = DGraphics(shape="point")
    d.screenSize()
