#   exception = Events detected during execution that inturrupt the flow of a program

try:
    a = int(input("enter a number to divide: "))
    b = int(input("Which number to devide! "))
    result = a / b
except ZeroDivisionError as e:          
    print(e)
    print("Fuck you")
except ValueError as e:              # e means which problem are here...problem syntax. 
    print(e)
    print("Enter only number please.")
except Exception as e:
    print(e)
    print("Somrthing Error")
else:
    print("{:.2f}".format(result))
finally:
    print("Thank you so much")