import getpass
import random
import string
from time import sleep

import pandas

from style import clear_screen
from style import Style


def save_user(data):
    data.to_csv('users.csv', index=False)


def print_user_details(user):
    print(
        f"ID: {Style.YELLOW}{user['id'].values.astype(int)[0]}{Style.RESET} \t Name: {Style.MAGENTA} {Style.BOLD}{user['name'].values.astype(str)[0]} {Style.RESET}"
    )
    print(Style.BLUE)
    print('-' * 54)
    print(Style.RESET)


def login():
    users = pandas.read_csv('users.csv')
    print()
    print("~" * 24 + Style.BOLD + "LOGIN" + "~" * 25 + Style.RESET)
    print()
    try:
        username = str(input('\tEnter your username : '))
    except ValueError:
        clear_screen()
        print(Style.RED + "please enter a valid username" + Style.RESET)
        return False, None

    user = users.loc[users['name'] == username]

    if user.empty:
        clear_screen()
        print(Style.RED + "please enter a valid username" + Style.RESET)
        return False, None

    if user['is_admin'].values.astype(int)[0] == 0:
        clear_screen()
        print(Style.RED + "please enter a valid user id" + Style.RESET)
        return False, None

    password = getpass.getpass("\tEnter your password : ")
    if password == user['password'].values.astype(str)[0]:
        clear_screen()
        print("\n\n" + Style.GREEN + f"Login Successful" + Style.RESET)
        print(
            "\n" + Style.BOLD + Style.GREEN + '-' * 20 + f"Welcome Admin" + '-' * 21 + Style.RESET)
        sleep(3)
        clear_screen()
        return True, user
    else:
        clear_screen()
        print(Style.RED + "please enter a valid password" + Style.RESET)
    return False, None


def add_user():
    users = pandas.read_csv('users.csv')
    while True:
        try:
            name = str(input('Enter your name : '))
        except ValueError:
            print(f"{Style.BOLD}{Style.RED} Please Enter a valid name {Style.RESET}")
            continue
        last = users.tail(1)
        password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        data = pandas.DataFrame(
            {'id': [last['id'].values.astype(int)[0] + 1, ], 'name': [name, ], 'password': [password, ],
             'is_admin': [0, ]})
        result = pandas.concat([users, data])
        save_user(result)
        user = users.tail(1)
        clear_screen()
        print(f"{Style.BOLD}{Style.GREEN} User added")
        print_user_details(user)
        try:
            _ = input(Style.BOLD + Style.BLUE + "\n\bGo to main menu?" + Style.RESET)
        except ValueError:
            clear_screen()
            break
        clear_screen()
        break


def list_users():
    users = pandas.read_csv('users.csv')
    while True:
        clear_screen()
        for i in range(len(users)):
            print_user_details(users.loc[users['id'] == i + 1])
        print(f"{len(users)} Users found")
        try:
            _ = input(Style.BOLD + Style.BLUE + "\n\bGo to main menu?" + Style.RESET)
        except ValueError:
            clear_screen()
            break
        clear_screen()
        break
