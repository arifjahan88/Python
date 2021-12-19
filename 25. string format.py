#   str.format() = Optional methods that gives users more control when displaying output 

animal = "The fox"
animal2 = "The lazy dog"
number = "1399"
number1 = 31416

print(animal + " Jumps over " + animal2)
print("{} jumps over {} ".format(animal,animal2))
print("{0} jumps over {1} ".format(animal,animal2))         #Positional Arguments
print("{animal2} jumps over {animal} ".format(animal = "Cow", animal2 = "Tiger"))   #Keyword argument

text = "{1} jumps over {0} "
print(text.format(animal,animal2))

print("{:7} this is number".format(number))
print("{:<10} this is number".format(number))
print("{:^10} this is number".format(number))
print("{:.2f} this is number".format(number1))
print("{:b} this is number".format(number1))        #Binary_Form
print("{:,} this is number".format(number1))
print("{:o} this is number".format(number1))
print("{:X} this is number".format(number1))
print("{:E} this is number".format(number1))

