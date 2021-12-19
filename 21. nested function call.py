#nested function calls = finction calls inside other function calls inner most function calls
#                        are resolved first returned value is used as argument for the next outer function.

# number = input("Enter a positive number")
# number = float(number)
# number = abs(number)
# number = round(number)
# print(number)

print(round(abs(float(input("Enter a whole positive number")))))        #shortcut