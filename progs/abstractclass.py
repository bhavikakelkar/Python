"""
from abc import ABC,abstractmethod
class computer(ABC):
    @abstractmethod
    def cpu(self):
        pass

class mobile(computer):

    def cpu(self):
        print("hello")


#comp=computer()
mob=mobile()
mob.cpu()

"""
class student:
    def __init__(self,marks1,marks2):
        self.marks1=marks1
        self.marks2=marks2

    def __add__(self,s2):
        m1=self.marks1+s2.marks1
        m2=self.marks2+s2.marks2
        return m1,m2


a=int(input("enter marks1 of first stud:-"))
b=int(input("enter marks2 of first stud:-"))
s1=student(a,b)
a=int(input("enter marks1 of sec stud:-"))
b=int(input("enter marks2 of sec stud:-"))
s2=student(a,b)

ans1,ans2=s1+s2
print(ans1,ans2)
