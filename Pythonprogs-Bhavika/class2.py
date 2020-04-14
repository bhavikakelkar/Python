#inheritance
class A:
  def __init__(self,name):
    self.name=name

  def printsome(self):
      print("HI,i am"+self.name)

class B(A): #singlelevel
    def printsome2(self):
        print("hello")

class C(B): #multilevel
    def printsome3(self):
        print("Hola")

class D:
    def __init__(selfself,name):
        self.name=name

    def printsome4(self):
        print("Adios "+self.name)

class E(C,D):
    def printsome(self):
        print("Bye")



a=A("C++")
b=B("Python")
b.printsome()
b.printsome2()
c1=C("Java")
c1.printsome2()
c1.printsome()
e=E("C#")
e.printsome3()
e.printsome4()
