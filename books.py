from datetime import date
from datetime import datetime

import pandas

books = pandas.read_csv('books.csv')
users = pandas.read_csv('users.csv')
history = pandas.read_csv('issued_history.csv')


def save_book(data):
    data.to_csv('books.csv', index=False)


def save_history(data):
    data.to_csv('issued_history.csv', index=False)


def list_books():
    print(books)


def search_books():
    while True:
        print("1. Search by title: ")
        print("2. Search by id: ")
        print("3. Search by author: ")
        print("4. Search by language: ")
        print("6. Search by language: ")

        search_choice = int("Enter your choice: ")

        if search_choice == 1:
            pass
        elif search_choice == 2:
            pass
        else:
            pass


def print_book_details(book):
    print(f"ID: {book['title'].values.astype(str)[0]}")
    print(f"Title: {book['id'].values.astype(int)[0]} \t\t Author: {book['author'].values.astype(str)[0]}")
    print(f"Genres: {book['genres'].values.astype(str)[0]} \t\t Year: {book['publication_year'].values.astype(int)[0]}")
    print(
        f"Language: {book['language'].values.astype(str)[0]} \t\t Available: {book['available'].values.astype(str)[0]}")


def issue_book():
    now = datetime.now()
    user = None
    while True:
        try:
            user_id = int(input('Enter User ID: '))
        except ValueError:
            print("Enter a valid number")
            continue
        else:
            user = users.loc[users['id'] == user_id]
            print(f"ID: {user['id'].values.astype(int)[0]} \t\t Name: {user['name'].values.astype(str)[0]}")
            break

    while True:
        try:
            book_id = int(input('Enter Book ID: '))
        except ValueError:
            print("please enter a valid book id")
            continue
        else:
            book = books.loc[books['id'] == book_id]
            print_book_details(book)

            if book['available'].values.astype(int)[0] > 0:
                try:
                    answer = str(input('Issue this book? (Y/n): '))
                except ValueError:
                    answer = 'Y'
                answer = answer.upper()
                if answer == 'Y':
                    data = pandas.DataFrame({
                        'id': [user['id'].values.astype(int)[0], ],
                        'name': [user['name'].values.astype(str)[0], ],
                        'book_id': [book['id'].values.astype(int)[0], ],
                        'book_name': [book['title'].values.astype(str)[0], ],
                        'issued_date': now.strftime("%m/%d/%Y"),
                        'return_date': [book['title'].values.astype(str)[0], ],
                        'is_returned': False,
                    })
                    result = pandas.concat([history, data])
                    # TODO Update available books
                    save_history(result)
                    print("Book issued successfully")
            else:
                print("Book not available")
            break


def return_book():
    while True:
        try:
            user_id = int(input('Enter User ID: '))
        except ValueError:
            print("Enter a valid number")
            continue
        else:
            user = users.loc[users['id'] == user_id]
            print(f"ID: {user['id'].values.astype(int)[0]} \t\t Name: {user['name'].values.astype(str)[0]}")
            # TODO Display Borrowed Books
            break

    pass


def issued_history():
    print(history)


def add_book():
    title = None
    author = None
    genres = None
    publication_year = None
    language = None
    copies = None
    while True:
        try:
            title = str(input('Enter book title : '))
        except ValueError:
            print("Enter a valid title")
            continue
        else:
            break

    while True:
        try:
            author = str(input('Enter author name : '))
        except ValueError:
            print("Enter a valid name")
            continue
        else:
            break

    while True:
        try:
            genres = str(input('Enter book genres : '))
        except ValueError:
            print("Enter a valid genres")
            continue
        else:
            if not genres.isalpha():
                print("Enter a valid genres")
                return False
            else:
                break

    while True:
        try:
            publication_year = int(input('Enter publication year : '))
        except ValueError:
            print("Enter a valid year")
            continue
        else:
            today = date.today()
            if publication_year > today.year:
                print("Enter a valid year")
                continue
            else:
                break

    while True:
        try:
            language = str(input('Enter book language : '))
        except ValueError:
            print("Enter a valid language")
            continue
        else:
            if not language.isalpha():
                print("Enter a valid language")
                continue
            else:
                break

    while True:
        try:
            copies = int(input('Enter number of copies: '))
        except ValueError:
            print("Enter a valid number")
            continue
        else:
            break

    last = books.tail(1)
    data = pandas.DataFrame(
        {
            'id': [last['id'].values.astype(int)[0] + 1, ],
            'title': [title, ],
            'author': [author, ],
            'genres': [genres, ],
            'publication_year': [publication_year, ],
            'language': [language, ],
            'copies': [copies, ],
            'available': [copies, ]
        }
    )
    result = pandas.concat([books, data])
    save_book(result)
