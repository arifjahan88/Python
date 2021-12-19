#scope = The region of a variable is recogniged
#        A variable is only available fron inside the region it is created.
#        A global and localy scope versions of a variable can be created

name = "Ashik Jahan"            #Global Variable

def FunctionName():
    name = "Arif Jahan"         #local Variable
    print(name)

FunctionName()
print(name)

    
    