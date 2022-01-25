import pandas

users = pandas.read_csv('users.csv')


def save_user(data):
    data.to_csv('users.csv', index=False)


def login():
    try:
        user_id = int(input('Enter your user id : '))
    except ValueError:
        print("please enter a valid user id")
        return False, None

    try:
        users.set_index('id', inplace=False)
        user = users.loc[users['id'] == user_id]
        print(user)
    except Exception as e:
        print(f"Invalid id {e}")
        return False, None

    password = str(input('Enter your password: '))
    print(password)
    print(user['password'])
    if password == user['password'].values.astype(str)[0]:
        print("login success")
        return True, user
    else:
        print("invalid password")
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
