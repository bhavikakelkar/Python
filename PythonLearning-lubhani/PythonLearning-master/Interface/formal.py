import abc

class geometry(abc.ABC):
    @abc.abstractmethod
    
    def Area(self):
        pass
    

class rectangle(geometry): 
    def Area(self,l,b):
        return l*b
class sqaure(geometry):
    def Area(self,s):
        return s*s
   


R= rectangle()
r= R.Area(10,20)
print("rectangle area=", r)

S= sqaure()
s= S.Area(5)
print("sqaure area=",s)


