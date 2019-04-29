import ShapeGr as gr
import turtle as t


class DGraphics(gr.Point):
    
    SLIST = ["ryba", "circle","point","rect","str"]
    
    
    def __init__(self, shape, x=0, y=0, size=10, inColor="black", outColor="black"):
        
        while True:
            if(shape.lower() in self.SLIST):
                self.__shape__ = shape
                break
            else:
                print("INVALID SHAPE INPUT")
                shape = str(input("\nInput shape: "))

        self.x = x
        self.y = y
        self.inColor = inColor
        self.outColor = outColor
        self.size = size

        self.track = False

        self.transX = 0
        self.transY = 0
        
        self.matrixPointX = 0
        self.matrixPointY = 0

    def draw(self):
        t.down() if self.track else t.up()
        t.color(self.inColor,self.outColor)
        t.down()

        t.begin_fill()
        t.left(60)
        for i in range(4):
            t.forward(10*self.size)
            t.right(100)
        t.end_fill()
        
    def move(self,x,y):
        self.x = x
        self.y = y

        t.up()
        t.setpos(self.transX + x, self.transY + y)
        print("newPos {}:{}".format(self.transX + x, self.transY + y))
        
    def screenSize(self,pos=-1):
        width = t.Screen().window_width()
        height = t.Screen().window_height()
        
        if(pos == -1):
            return(width,height)
        elif(pos == 0):
            return(width)
        elif(pos == 1):
            return(height)

    def translate(self, x, y):
        self.transX = x
        self.transY = y
        print("translated {}:{}".format(x, y))
        
    def pushMatrix(self):
        self.matrixPointX = self.transX
        self.matrixPointY = self.transY
        print("pushMatrix {}:{}".format(self.matrixPointX, self.matrixPointY))

    def popMatrix(self):
        self.transX = self.matrixPointX
        self.transY = self.matrixPointY
        print("popMatrix {}:{}".format(self.transX, self.transY))

        

if __name__ == "__main__":
    d = DGraphics(shape="ryba", size = 50,inColor = "red", outColor="blue")
    d.draw()
    
    

    
