from datetime import date
from datetime import datetime
from time import sleep

import pandas

from style import clear_screen
from style import Style
from users import print_user_details



def save_book(data):
    data.to_csv('books.csv', index=False)


def save_history(data):
    data.to_csv('issued_history.csv', index=False)


def print_book_details(book):
    available = book['available'].values.astype(int)[0]
    if available > 0:
        available = f"{Style.GREEN}{available} Copies Available {Style.RESET}"
    else:
        available = f"{Style.RED}{Style.BOLD} Unavailable {Style.RESET}"

    print(f"ID: {Style.YELLOW}{book['id'].values.astype(int)[0]}\n{Style.RESET}")
    print(f"Title: {Style.YELLOW} {Style.BOLD}{book['title'].values.astype(str)[0]}\n {Style.RESET}")
    print(f"Author: {Style.MAGENTA}{book['author'].values.astype(str)[0]}\n {Style.RESET}")
    print(f"Genres: {Style.CYAN}{book['genres'].values.astype(str)[0]} {Style.RESET}\n")
    print(f"Year: {Style.WHITE}{book['publication_year'].values.astype(int)[0]} {Style.RESET}\n")
    print(f"Language: {Style.BOLD}{book['language'].values.astype(str)[0]} {Style.RESET}\n")
    print(f"Available: {available}")
    print(Style.BLUE)
    print('-' * 54)
    print(Style.RESET)


def print_history(book):
    print(book)


def list_books():
    books = pandas.read_csv('books.csv')
    while True:
        clear_screen()
        for i in range(len(books)):
            print_book_details(books.loc[books['id'] == i + 1])
        print(f"{len(books)} books found")
        try:
            _ = input(Style.BOLD + Style.BLUE + "\n\bGo to main menu?" + Style.RESET)
        except ValueError:
            clear_screen()
            break
        clear_screen()
        break


def search_books():
    books = pandas.read_csv('books.csv')
    clear_screen()

    while True:
        print()
        print()
        print("~" * 24 + Style.BOLD + "SEARCH" + "~" * 24 + Style.RESET)
        try:
            print()
            search_choice = int(input(f"{Style.BOLD}Book ID: {Style.RESET}"))
        except ValueError:
            clear_screen()
            print(f"{Style.BOLD}{Style.RED} No Result Found {Style.RESET}")
            try:
                search_again = input(f"{Style.BOLD}Try Again?(Y/n) : {Style.RESET}")
            except ValueError:
                continue
            else:
                search_again = search_again.upper()
                if not search_again == 'Y':
                    break
        else:
            book = books.loc[books['id'] == search_choice]
            if book.empty:
                print(f"{Style.BOLD}{Style.RED} No Result Found {Style.RESET}")
                try:
                    search_again = input(f"{Style.BOLD}Try Again?(Y/n) : {Style.RESET}")
                except ValueError:
                    continue
                else:
                    search_again = search_again.upper()
                    if not search_again == 'Y':
                        break
            else:
                print(f"{Style.BOLD}{Style.GREEN} Result Found {Style.RESET}")
                print_book_details(book)
                try:
                    search_again = input(f"{Style.BOLD}Try Again?(Y/n) : {Style.RESET}")
                except ValueError:
                    continue
                else:
                    search_again = search_again.upper()
                    if not search_again == 'Y':
                        break


def issue_book():
    books = pandas.read_csv('books.csv')
    users = pandas.read_csv('users.csv')
    history = pandas.read_csv('issued_history.csv')

    clear_screen()
    now = datetime.now()
    while True:
        print()
        print()
        print("~" * 22 + Style.BOLD + "ISSUE BOOK" + "~" * 22 + Style.RESET)
        user_id = int(input('Enter User ID: '))
        user = users.loc[users['id'] == user_id]
        if not user.empty:
            print("~" * 21 + Style.BOLD + "USER DETAILS" + "~" * 21 + Style.RESET)
            print_user_details(user)
            break
        else:
            clear_screen()
            print(f"{Style.BOLD}{Style.RED} Enter a valid user id {Style.RESET}")
            continue

    while True:
        book_id = int(input('Enter Book ID: '))
        book = books.loc[books['id'] == book_id]
        if book.empty:
            print(f"{Style.BOLD}{Style.RED} Book Not Available{Style.RESET}")
            continue
        else:
            print("~" * 21 + Style.BOLD + "BOOK DETAILS" + "~" * 21 + Style.RESET)
            print_book_details(book)

        if book['available'].values.astype(int)[0] > 0:
            print("book available")
            answer = str(input('Issue this book? (Y/n): '))
            answer = answer.upper()
            if answer == 'Y':
                print("ans Y")
                data = pandas.DataFrame({
                    'user_id': [user['id'].values.astype(int)[0], ],
                    'username': [user['name'].values.astype(str)[0], ],
                    'book_id': [book['id'].values.astype(int)[0], ],
                    'book_name': [book['title'].values.astype(str)[0], ],
                    'issued_date': [now.strftime("%m/%d/%Y"), ],
                    'return_date': [now.strftime("%m/%d/%Y"), ],
                    'is_returned': False,
                })
                result = pandas.concat([history, data])
                # TODO Update available books
                save_history(result)
                print("Book issued successfully")
                sleep(2)
                break
            else:
                print(answer)
                print("Y")
                continue
        else:
            print(f"{Style.BOLD}{Style.RED} Book Not Available{Style.RESET}")
            continue


def return_book():
    history = pandas.read_csv('issued_history.csv')
    users = pandas.read_csv('users.csv')
    print()
    print()
    print("~" * 22 + Style.BOLD + "ISSUE BOOK" + "~" * 22 + Style.RESET)
    while True:
        try:
            user_id = int(input('Enter User ID: '))
        except ValueError:
            print(f"{Style.BOLD}{Style.RED} Enter a valid user id{Style.RESET}")
            continue
        else:
            user = users.loc[users['id'] == user_id]
            if user.empty:
                print(f"{Style.BOLD}{Style.RED} Book Not Available{Style.RESET}")
                continue

            print_user_details(user)
            borrowed_books = history.loc[history['user_id'] == user_id]
            print_history(borrowed_books)
            break

    while True:
        try:
            book_id = int(input('Enter Book ID: '))
        except ValueError:
            print(f"{Style.BOLD}{Style.RED} Enter a valid book id{Style.RESET}")
            continue
        else:
            returning_book = [borrowed_books['book_id'] == book_id]
            if user.empty:
                print(f"{Style.BOLD}{Style.RED} Book Not Available{Style.RESET}")
                continue
            else:
                print(f"\n\n{Style.BOLD}{Style.GREEN} Book Returned successfully{Style.RESET}")
                break


def issued_history():
    history = pandas.read_csv('issued_history.csv')
    print(history)


def add_book():
    books = pandas.read_csv('books.csv')
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
