"""
you are given two complex numbers, and you have
to print the result of their addition or
 multiplication
"""


class complexNumb:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def add1(self,c):
        real=self.real+c.real
        img=self.img+c.img
        self.real=real
        self.img=img

    def mul(self,c):
        real=(self.real*c.real)-(self.img*c.img)
        img=(self.real*c.img)+(self.img*c.real)
        self.real=real
        self.img=img
    
    def print(self):
        print(self.real,"+i",self.img)


c1=int(input("enter real part"))
c2=int(input("enter complex part"))
obj1=complexNumb(c1,c2)
c3=int(input("enter real part2"))
c4=int(input("enter complex part2"))
choice=int(input("enter choice"))
obj2=complexNumb(c3,c4)
if(choice==1):
    obj1.add1(obj2)
    obj1.print()
elif(choice==2):
    obj1.mul(obj2)
    obj1.print()
