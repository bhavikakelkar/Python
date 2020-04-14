"""
Basic functions

listno=[1,2,3,4,5] #Number
liststr=["Bhavika","Simba"] #string
listmulti=[listno,liststr] #multidimensional
print(listmulti)
listmixed=[1,"bhavika",2,"simba"] #mixed
print(len(listmulti))
listmixed.append("python")
print(listmixed)
listmulti.append((100,200)) #adding tuple
print(listmulti)
listno.insert(1,"python")
print(listno)

"""

"""
You are given three integers  and  representing the dimensions of a cuboid along with an integer . You have to print a list of all possible 
coordinates given by  on a 3D grid where the sum of  is not equal to . 
"""
x = int(input("Enter x:-"))
y = int(input("Enter y:-"))
z = int(input("Enter z:-"))
n = int(input("enter n:-"))
for a in range(x+1):

    for b in range(y+1):

        for c in range(z+1):

            if a + b + c != n:
                list=[a,b,c]
                print(list,end="")

