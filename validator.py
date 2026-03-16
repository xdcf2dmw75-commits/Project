print("1 - Проверить ник")
print("2 - Проверить email")
print("3 - Проверить номер")

choice = input("Выбери: ")

if choice == "1":
    username = input("Ник: ")
    if len(username) >= 3:
        print("Ник валидный")
    else:
        print("Ник невалидный")

elif choice == "2":
    email = input("Email: ")
    if "@" in email and "." in email:
        print("Email валидный")
    else:
        print("Email невалидный")

elif choice == "3":
    number = input("Номер: ")
    if number.isdigit() and len(number) >= 10:
        print("Номер валидный")
    else:
        print("Номер невалидный")

else:
    print("Ошибка выбора")
