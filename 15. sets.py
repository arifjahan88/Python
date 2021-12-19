# Set = Collection which is unordered, unindexed. No duplicate values.

name = {"Arif", "Ashik", "Sraboni"}
address = {"Bogura", "Dhaka", "Jony"}
phone = {"2343", "98798"}

name.add("Jony")
phone.add("Jony")
name.remove("Ashik")
#name.clear()

print(name.difference(address,phone))               #print how many not same value
print(name.intersection(address,phone))             #print the same value

#name.update(address,phone)
#all_set = name.union(address,phone)     #same work in update

# for i in all_set:
#     print(i)
