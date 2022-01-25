from datetime import date

import pandas

books = pandas.read_csv('books.csv')


def save_book(data):
    data.to_csv('books.csv', index=False)


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


def issue_book():
    pass


def return_book():
    pass


def issued_history():
    pass


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

