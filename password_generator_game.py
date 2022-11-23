import random

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','(',')']

letter_no = int(input("How many letters do u want in ur password? "))
numbers_no = int(input("How many numbers do u want in ur password? "))
symbols_no = int(input("How many symbols do u want in ur password? "))

password = ""
for letter in range(0,letter_no):
    password += random.choice(letters)

for number in range(0,numbers_no):
    password += random.choice(numbers)

for symbol in range(0,symbols_no):
    password += random.choice(symbols)

print(f"Your password is {password}")

# shuffled password
passwords = []
password_list = list(password)
password = ""
for char in password_list:
    random.shuffle(password_list)
    password += char
print(f"Your shuffled password is {password}")
