import csv
FILENAME = "data.csv"
mode = (input('login->'))
if mode == "yes":
    login = (input('login->'))
    password = (input('password->'))
    path = (input('path->'))

    data = [
        {"login": login , "password": password , "path": path}
    ]
    with open(FILENAME, "a", newline="") as myfile:
        columns = ["login", "password","path"]
        writer = csv.DictWriter(myfile, delimiter=';', fieldnames=columns)
        writer.writeheader()
        writer.writerows(data)
if mode == "no":
    login1 = (input('login->'))
    password1 = (input('password->'))
    inp = open('data.csv', 'r')
    for login, password, path in (i.split(';') for i in inp.readlines()):
        #print( )
        if login1 == login:
            if password1 == password:
                print("Yes")
                print(path)
