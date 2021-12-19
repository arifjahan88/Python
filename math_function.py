import math

pi = 3.1416
neg = -3.1416

x = int(input("X = "))
y = int(input("Y = "))
z = int(input("Z = "))

print(round(pi))
print(math.ceil(pi))
print(abs(neg))                #Absolute Value
print("Power is " + str(pow(x,2)))
#print("{:3} Squre Root " + str(math.sqrt.__format__(z)))
print("{:.4f} Squre Root ".format(math.sqrt(y)))
print("Maximum Value is " + str(max(x,y,z)))
print("Minimum Value is " + str(min(x,y,z)))


