#Напишите программу, которая запрашивает год и проверяет его високосность

year = int(input("Enter year: "))
result = None

if year % 100 == 0:
    if year % 400 == 0 :
        result = "Високосный"
    else:
        result = " Не Високосный"
elif year % 4 == 0:
    result = "Високосный"
else:
    result = " Не Високосный"

print(result)

