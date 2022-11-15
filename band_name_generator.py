print("Welcome to the Delhi city!")
city_name = input("From which city you belong? ")
pet_name = input("What is your pet name? ")

print(f"your band name must be {city_name} {pet_name}! What say :)")

# print first four letters of city_name and pet_name as band_name
a = 0
b = 0
city_four = ""
pet_four = ""
for num in city_name:
    if (a < 4):
        city_four += num
    a += 1

for char in pet_name:
    if (b < 4):
        pet_four += char
    b += 1
print(f"Then your band name must be {city_four} {pet_four}.")



