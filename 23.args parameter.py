#*args = parameter thet will pack all urguments into a tuple useful so that a function
#        can accept a varrying amount of arguments

def add(*age):
    sum = 0
    age = list(age)             #individual mark kora
    age[0] = 0
    for x in age:
        sum += x
    return sum


print(add(1,2,3,4,5,6))