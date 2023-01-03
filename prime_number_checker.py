def prime_checker(number):
    isprime = True
    for num in range(2,number):
        if(number%num==0):
            isprime = False

    if(isprime==False):
        print(f"{number} is not a prime number.")
    else:
        print(f"{number} is a prime number.")

n = int(input("Enter a number to check: "))
prime_checker(n)
