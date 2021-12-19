#   index operator = give access to a sequence's element (str, list, tuple)

name = "aEif JAHAN"

# if (name[0].islower):
#     name = name.upper()
#     print(name)

# first_name = name[:4].upper()
# last_name = name[5:10].lower()
# print(first_name, last_name)

first_name = name[:4]
last_name = name[5:10]
if (first_name.islower):
    print(first_name.upper())
else:
    print("here no lowercase")
if(last_name.isalpha):
    print(last_name.lower())

last_charecter = name[-1]
print(last_charecter)
