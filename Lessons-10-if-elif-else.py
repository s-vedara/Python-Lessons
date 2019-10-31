


##Условные операторы

x = input('Enter  a number: ')
x = int(x)

if x == 25:
    print("yes you right")
else:
    print("No you are wrong!")



age = 15
if (age <=4):           #Если
    print("Yau are baby!")
    break       ##Можно прервать цикл
elif (age > 4) and (age < 12):     ##Иначе
    print("You are kid")
elif (age >= 12) and (age < 19):
    print("You are teenager")
else:
    print("You are old!")
print("----END----")
