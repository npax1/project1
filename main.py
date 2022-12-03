import sys
import time
import os

print("вітаю в моїй програмі")


def clearConsole(): lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def WP():
    new_old = input("ти тут новенький?(відповідати лише на англійській)").lower()

    if new_old == "no" or new_old == "old":
        print("ви тут в перше")
    elif new_old == "yes" or new_old == "new":
        print("Register: ")
        time.sleep(1.5)
        #  запит на ввод пароля
        userName = input("введіть ім я")
        # запит на ввод ім я
        passWord = int(input("""введіть пароль але лише цифри"""))
        file = open("us_ps.txt")
        file.write("User name = " + userName + "\n" + "Password = " + str(passWord) + "\n" + "Car color = ")
        file.close()
        clearConsole()
        if userName != "" and passWord != "":
            print("ти пам ётаєш свій пароль?")

            un_check = input("введи ім я")
            ps_check = int(input("пароль!!"))

            if un_check == userName and ps_check == passWord:
                print("проходь")
            sys.exit()
WP()