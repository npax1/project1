import csv
FILENAME = "users.csv"
file_mode = input('Виберіть режим праці[ w або н - новий документ | a(анг або укр) - дозапис | r або ч - читати ] --> ')
if file_mode != 'w' or file_mode == 'a' or file_mode == 'н' or file_mode == 'а':
    print(f"Некоректний режим --> {file_mode}")
if file_mode == 'w' or file_mode == 'a' or file_mode == 'н' or file_mode == 'а':
    name = input("Продукт --> ")
    katalog = input("До якої категорії належить товар --> ")
    num = input("Кількість товару --> ")
    opic = input("Опис товару --> ")
    price = input("Ціна товару --> ")
    magazin = input("В якому магазині куплений товар --> ")
    date = input("Коли була здійснена покупка --> ")
    users = [
        {"Продукт": name, "Категорія": katalog, "Кількість": num, "Опис": opic, "Ціна": price, "Магазин": magazin, "Дата": date}
    ]
#----Створення файлу----
if file_mode == 'w' or file_mode == 'н':
    with open(FILENAME, "w", newline="") as myfile:
        columns = ["Продукт", "Категорія", "Кількість", "Опис", "Ціна", "Магазин", "Дата"]
        writer = csv.DictWriter(myfile, delimiter=';', fieldnames=columns)
        writer.writeheader()
        writer.writerows(users)
#----Дозапис файлу----
if file_mode == 'a'or file_mode == 'а':
    with open(FILENAME, "a", newline="") as myfile:
        columns = ["Продукт", "Категорія", "Кількість", "Опис", "Ціна", "Магазин", "Дата"]
        writer = csv.DictWriter(myfile, delimiter=';', fieldnames=columns)
        user = {"Продукт": name, "Категорія": katalog, "Кількість": num, "Опис": opic, "Ціна": price, "Магазин": magazin, "Дата": date}
        writer.writerow(user)
#----Читання файлу----
if file_mode == 'r' or file_mode == 'ч':
    with open(FILENAME, "r", newline="") as myfile:
        reader = csv.reader(myfile)
        for row in reader:
            for index in range(0, len(row)):
                print(row[index], end='\t')
            print()