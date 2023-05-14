import functools
import operator

list1 = [9,2,13,4,5]
list_sum = (functools.reduce(lambda a,b: a+b, list1))
print("totla sum is: ")
print(list_sum)
print("The maximum element of list is: ")
print(functools.reduce(max, list1))
print("The minimum element of list is: ", functools.reduce(min, list1))

print()
print("The total sum using operator module is: ", functools.reduce(operator.add, list1))
print("The multiplication of list using operator module is: ", functools.reduce(operator.mul, list1))
print("String addition demonstration is: ", functools.reduce(operator.add, ["geeks", "for", "geeks"]))
