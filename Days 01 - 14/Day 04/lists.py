fruit = ["apple", "orange", "guava"]
if fruit[0] or fruit[1] or fruit[3] == "apple":
    print ("yes")


fruit[0] = "mango"
print(fruit)
fruit.extend(["banana", "pear"])
print(fruit)
