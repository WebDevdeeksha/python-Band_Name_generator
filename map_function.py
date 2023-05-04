# Return double of n
# def double(n):
#     return n+n

# numbers = [1,2,3,4,5,6]
# double_num = list(map(double, numbers))
# print(double_num)


# Double all numbers using map and lambda
# numbers = [1,2,2.3,4.5,6]
# double_num = list(map(lambda x: x+x, numbers))
# print(double_num)

# Add two lists using map and lambda
# num1 = [1,2,3,4,5]
# num2 = [1.2,3.4,5.6,8,9]
# numbers = list(map(lambda a,b: a+b, num1, num2))
# print(numbers)

# name1 = ["meena_", "komal_", "leela_", "adhira_"]
# name2 = ["joker", "pokar", "poker", "12"]
# name = list(map(lambda a,b: a+b, name1, name2))
# print(name)

# List of strings
# names = ["manish", "shreya", "heena"]
# test = list(map(list, names))
# print(test)

# Using Map() With Len()
# names = ["manish", "shreya", "heena"]
# length = list(map(len, names))
# print(length)

# using map function with sqrt function 
# import math
# numbers = [4,9,16,25,256,225, 11.56, 44.89]
# sq_root = list(map(lambda a: math.sqrt(a), numbers))
# print(sq_root)

# Using Map in Python as an Iterator (change lower case characters in upper case)
# def upper(char):
#     return (char.upper())

# lower_str = "This is simplilearn"
# lower_tuple = ("Welcome to Simpli_learn")

# upper_str = list(map(upper, lower_str))
# upper_tuple = list(map(upper, lower_tuple))
# print(upper_tuple)
# print(upper_str)

# # Using map() function and lambda and count() function create a list consisted of the number of occurence of both letters: A and a.
# lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
# lst2 = list(map(lambda x: x.lower().count("a"), lst1))
# print(lst2)

# Using map() function, first return a new list with absolute values of existing list. Then for ans_1, find the total sum of the new list's elements.
# lst = [99.3890,-3.5, 5, -0.7123, -9, -0.003]
# abs_list = list(map(abs, lst))
# print(abs_list)
# total_sum = sum(abs_list)
# print(total_sum)

# Write a Python program to compute the sum of elements of an array of integers. Use the map() function.
array = [12, 2, 23, 22, 11]
# array_sum = sum(array)
array_sum = list(map(lambda x: x[0]+x[1], array))
print(array_sum)


