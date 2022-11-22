print("Welcome to Python Love Calculator!")
name1 = input("Enter 1st name: ")
name2 = input("Enter 2nd name: ")
name = name1 + name2
name = name.lower()

t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')
l = name.count('l')
o = name.count('o')
v = name.count('v')

true = t+r+u+e
love = l+o+v+e

love_score = int(str(true) + str(love))
if(love_score>10) and (love_score<39):
    print("AWESOME TOGETHER")
elif(love_score>40) and (love_score<50):
    print("FABULOUS TOGETHER")
else:
    print("COMPATIBLE TOGETHER")