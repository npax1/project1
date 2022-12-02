import csv
FILENAME = "data.csv"

login = (input('login->'))
password = (input('password->'))
path = (input('path->'))

data = [
    {"login": login , "password": password , "path": path}
]
with open(FILENAME, "w", newline="") as myfile:
    columns = ["login", "password","path"]
    writer = csv.DictWriter(myfile, fieldnames=columns)
    writer.writeheader()
    writer.writerows(data)