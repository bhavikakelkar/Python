"""
You are given a string and your task is to swap cases.
 In other words, convert all lowercase letters
  to uppercase letters and vice versa.
"""

def swap_case(str):
    a = ""
    for i in str:
        if (i.isupper() == True):
            a+=(i.lower())
        else:
            a+=(i.upper())
    return a

loop='y'
while(loop=='y'):
    strinput=input("Enter a string")
    ans=swap_case(strinput)
    print(ans)
 #   print(len(strinput))
# print(strinput[3:-2])- slicing
    loop=input("Continue?")
