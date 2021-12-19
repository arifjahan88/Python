#loop control statements = Change a loop execution from it's nosmal sequence
#Break =        used to terminate the loop intirely
#continue =     Skips to the next iteration of the loop
#pass =         does nothing, acts as a place holder

while True:
    name =  input("Enter Your Name: ")
    if name != "":
        break

number = "0=13442323=1212=121"
for i in number:
    if i == "=":
        continue
    print(i, end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i, end=" ")
