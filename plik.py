import random 
zmienna = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
ans = int(input("Podaj dlugosc hasla: "))

haslo = " "
for i in range(ans):
    randomSign = random.choice(zmienna)
    haslo += randomSign




print(haslo)

