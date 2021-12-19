#   tuple = collection which is ordered and unchangeble 
#           used to group together related data.

name = ("Arif", "Jahan", 24)

print(name.count("Arif"))
print(name.index(24))

for i in name:
    print(i, end=" ")

if "Arif" in name:
    print("He is Here")
else:
    print("He is missing")
