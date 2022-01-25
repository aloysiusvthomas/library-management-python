import pandas

from style import clear_screen
from style import Style

users = pandas.read_csv('users.csv')


def save_user(data):
    data.to_csv('users.csv', index=False)


def login():
    print(Style.BOLD + Style.GREEN + f'\n\n\t\t --LOGIN--\n' + Style.RESET)
    try:
        user_id = int(input('Enter your user id : '))
    except ValueError:
        clear_screen()
        print(Style.RED + "please enter a valid user id" + Style.RESET)
        return False, None

    user = users.loc[users['id'] == user_id]

    if user.empty:
        clear_screen()
        print(Style.RED + "please enter a valid user id" + Style.RESET)
        return False, None

    if user['is_admin'].values.astype(int)[0] == 0:
        clear_screen()
        print(Style.RED + "please enter a valid user id" + Style.RESET)
        return False, None

    password = str(input('Enter your password: '))
    if password == user['password'].values.astype(str)[0]:
        clear_screen()
        print("\n\n" + Style.GREEN + f"Login Successful" + Style.RESET)
        print(
            "\n" + Style.BOLD + Style.GREEN + Style.BARS * 10 + f"Welcome Admin" + Style.BARS * 10 + Style.RESET)
        return True, user
    else:
        clear_screen()
        print(Style.RED + "please enter a valid password" + Style.RESET)
    return False, None


def register():
    try:
        name = str(input('Enter your name : '))
        password = str(input('Enter your password : '))
    except ValueError:
        print("please enter a valid input")
        return False, None
    last = users.tail(1)
    data = pandas.DataFrame(
        {'id': [last['id'].values.astype(int)[0] + 1, ], 'name': [name, ], 'password': [password, ], 'is_admin': [0, ]})
    result = pandas.concat([users, data])
    save_user(result)
    user = users.tail(1)
    return True, user
