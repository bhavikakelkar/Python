class mapping:
    def __init__(self,data):
        self.__data=data
        
    def __len__(self):
        return len(self.__data)
        
    def __contains__(self,member):
        return member in self.__data
    
   
    
        

m= mapping(["bat","cat","rat"])
print(len(m))



print("bat"in m)
print("balloon" not in m)
