#code
class shape:
    def __init__(self,name):
        self.name=name
    def Area(self):
        pass
    def call(self):
        print("This is abstract class for shape")


class sqaure(shape):
    
    def __init__(self, length):
        super().__init__("Square")
        self.length = length
    def Area(self):
        print("area of sqaure")
        return self.length**2
    def call(self):
        print("this is sqaure")
        
class rectangle(shape):
    
    def __init__(self,l,b):
        super().__init__("rectangle")
        self.length=l
        self.breadth=b
    def Area(self):
        print("area of rectangle")
        return self.length*self.breadth
        
        
sq=sqaure(5)
rec=rectangle(4,5)

print(sq.Area())
print(rec.Area())
sq.call()
rec.call()