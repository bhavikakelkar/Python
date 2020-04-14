class College:
    def __init__(self):
        print("This is non parametrized constructor")
        
    def getCollege(self,clg_name):
        self.clg_name=clg_name
        
    def printCollege(self):
        print("Your college is:", self.clg_name)
        
class Student(College):
    isStudent="yes" #static variable
    def __init__(self,name,rollno):
        print("This is parametrized constructor")
        self.name=name
        self.rollno=rollno

    def printDetails(self):
        print("Student Name:",self.name)
        print("Student Roll Number:",self.rollno)
    
    @classmethod
    def is_Student(cls): #static method
        print("is Student:",cls.isStudent)
        
        
#main code
S= Student("lubhani",92)
S.getCollege("igdtuw")
S.printCollege()
S.printDetails()
Student.is_Student()
print(Student.isStudent)
