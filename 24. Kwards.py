#   **kwards = A parameter thet will pack all arguments into a dictionary so that a function
#              can accept a varring amount of keyword arguments.

def fun(**kwards):
    #print("Hello", kwards['first'] + kwards['middle'])
    print("Hello", end=" ")
    for key,value in kwards.items():
        print(value, end=" ")

fun(title = "MD", first = "Arif",last = "Roman", middle = "Jahan")
    