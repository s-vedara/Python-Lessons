


#name = input("Please enter: ")
#print("Вы ввели " + name)
#
#num1 = input("Enter X: ")
#num2 = input("Enter Y: ")
#summa = int(num1) + int(num2)
#print(summa)

message = ""

while True:
    message = input("Enter Password:")
    if message == 'sekret':
        break
    print(message + "Password not correct")

print("Password was:" + message)


