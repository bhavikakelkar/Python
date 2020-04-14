"""
myset={1,2,3,4}
print(myset)
myset2=set()
myset2=set(['a','b'])
myset2.add('c')
myset2.add((5,4))
myset2.update([1,2,3,4])
print(myset2)
myset2.discard(2)
print(myset2)
first={'apple','nokia','sony'}
second={'sony','acer','razer'}
print(first.union(second))
print(first.difference(second))

a=input()
b=a.split()
print(b)

"""
"""
Given  sets of integers, M and N, print their symmetric
difference. The term symmetric difference indicates those
values that exist in either M or N but do not exist in both
"""

a=int(input("enter number of ints(m):-"))
b=input("enter numbers ").split()
c=int(input("enter number of ints(n):-"))
d=input("enter numbers ").split()
x=set(b)
y=set(d)
p=y.difference(x)
q=x.difference(y)
r=p.union(q)
print ((sorted(r)))
