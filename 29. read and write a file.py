#  ----Read Mode-----
try:
    with open('C:\\Users\\ashik\Desktop\\New Text Document.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("get lost")



#   -----Write Mode-----
text = "Oaw i am learning python code \n let's enjoy \n okkkkk"
try:
    with open('C:\\Users\\ashik\Desktop\\New Text Document.txt', 'w') as file: #here 'w' means write
        file.write(text)
except FileNotFoundError:
    print("get lost")