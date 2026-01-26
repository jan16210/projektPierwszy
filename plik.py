import random
elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_length = int(input("Podaj długość karnetu: "))

password = ""
for i in range(pass_length):
    password += random.choice(elements)

print(password)
