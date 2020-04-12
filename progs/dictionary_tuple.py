"""
#Dictionary
dict1=dict({1:'Sony',2:'Samsung',3:'Honor',4:'Razer'})
print(dict1)

dict3={1:'Acer',6:'Xiaomi',7:'Oneplus',8:'Huawei',5:'Nokia'}

dict2=dict({(1,'Sony'),(2,'Samsung'),(3,'Honor'),(4,'Razer')})
print(dict2)

print(dict3.get(4))
dict3[0]="apple"
print(dict3)

key=dict3.pop(1)
print(key)
print(dict3)

dict1.update(dict3)
print(dict1)
"""
"""
#Tuple

tup1=('apple','xiaomi')
print(tup1)

list=[1,2]
print(tuple(list))

tup2=tuple("samsung")
print(tup2)

tup3=(1,"sony",2,"acer")

tup4=(tup3,tup1)
print(tup4)
tup5=tup4+tup2
print(tup5)

print(tup5[2:])
"""


