#Nested_loop = The "inner loop" loop will finish all of it's interaction before
#              finishing one interaction of the "outer loop"

rows = 2             #int(input("Enter your row size: "))
column = 4            #int(input("Enter your column size: "))
symbol = "*"         #input("Enter your symbol: ")

# for i in range(rows + 1):
#     for j in range(column + 1):
#         print(symbol, end=" ")
#     print()

for i in range(0,5):
    for j in range(0,i+1):              
        print(symbol, end=" ")
    print()


for i in range(5,0,-1):
    for j in range(0,i-1):
        print(symbol, end=" ")
    print()


for i in range(0,5):
    temp = 1
    for j in range(5, 0, -1):
        if j > i:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print("")

