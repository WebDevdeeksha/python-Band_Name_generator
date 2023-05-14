# change string in upper case and do reverse

# str = "geeksforgeeks"
# upper_str = lambda string: string.upper()
# rev_str = lambda string: string[::-1]
# rev_upper = lambda string: string.upper()[::-1]
# print(upper_str(str))
# print(rev_str(str))
# print(rev_upper(str))


# cube_numbers = lambda x: x*x*x
# print(cube_numbers(8))

is_even_list = [lambda val=x: val * 5 for x in range(1, 10)]

# iterate on each lambda function
# and invoke the function to get the calculated value
for num in is_even_list:
	print(num)

