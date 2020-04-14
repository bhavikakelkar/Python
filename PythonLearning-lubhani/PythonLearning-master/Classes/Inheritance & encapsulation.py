# Base class 1
class Programming:
    def __init__(self):
        print("this is competitive Programming")
    
    def getScore(self,prg_score):
        self.prg_score=prg_score
    
    def print_score(self):
        return self.prg_score
 
# Base class 2       
class  PythonLearn:
    
    def __init__(self):
        print("Python Learning score")
    def getMarks(self,py):
        self.py=py
    def print_marks(self):
        return self.py
        
#Derived class
class Performance(PythonLearn, Programming):
    
     __coursePrice=1000  #Encapsulation
     price=0
     def __init__(self):
          super().__init__()
          
     def getDetails(self,name,enroll_no):
         self.name= name
         self.enroll_no= enroll_no
     def print_details(self):
         print("Name:", self.name)
         print("enroll_no:", self.enroll_no)
     def price(self):
         price= self.__coursePrice
         return price
         

p= Performance()
p.getDetails("xyz",21)
p.getScore(65)
p.getMarks(67)
p.print_details()

prg= p.print_score()
py = p.print_marks()
price= p.price()


amount=price
if((prg+py)/2 >= 60):
    print("Your Performance is good")
    amount= price- .20*price
else:
    print("You need to work hard!,don't give up")
    
print("total fee:",amount)