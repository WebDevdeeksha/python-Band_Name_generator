import random

name_string = input("Enter name series: ")
print(name_string)

# split function split the string into list by given enclosed
# character in parenthesis suppose comma or space (" ")

names = name_string.split(",")
print(names)
last_item = len(names)
print(last_item)

a = random.randint(0,last_item-1)
random_char = names[a]
print(f"{random_char} is going to buy the milk today.")

