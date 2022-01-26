from datetime import date
from datetime import datetime
from datetime import timedelta
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


def print_history(books):
    for items in range(len(books)):

        returned = books['is_returned'].values.astype(str)[0]
        if returned == 'yes':
            returned = f"{Style.GREEN}{returned.title()}{Style.RESET}"
        else:
            returned = f"{Style.RED}{Style.BOLD} No {Style.RESET}"
        print()
        print(f"No: {items + 1}\n")
        print(f"Book ID: {Style.YELLOW}{books['book_id'].values.astype(int)[0]}\n{Style.RESET}")
        print(f"Book Name: {Style.YELLOW} {Style.BOLD}{books['book_name'].values.astype(str)[0]}\n {Style.RESET}")
        print(f"Issued Date: {Style.MAGENTA}{books['issued_date'].values.astype(str)[0]}\n {Style.RESET}")
        print(f"Return Date: {Style.MAGENTA}{books['return_date'].values.astype(str)[0]}\n {Style.RESET}")
        print(f"Is Returned: {returned}")
        print(Style.BLUE)
        print('-' * 54)
        print(Style.RESET)


def list_books():
    books = pandas.read_csv('books.csv')
    while True:
        clear_screen()
        if len(books) > 0:
            for i in range(len(books)):
                print_book_details(books.loc[books['id'] == i + 1])
            print(f"{len(books)} books found")
        else:
            print(f"{Style.BOLD}{Style.RED}No books found {Style.RESET}")
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
    search_again = True

    while True:
        if search_again is False:
            try:
                var = input(f"{Style.BOLD}Search Again?(y/N) : {Style.RESET}")
            except ValueError:
                clear_screen()
                break
            var = var.upper()
            if var == 'Y':
                search_again = True
                clear_screen()
                continue
            else:
                clear_screen()
                break

        print()
        print("~" * 24 + Style.BOLD + "SEARCH" + "~" * 24 + Style.RESET)
        try:
            print()
            search_choice = int(input(f"{Style.BOLD}Book ID: {Style.RESET}"))
        except ValueError:
            clear_screen()
            print(f"{Style.BOLD}{Style.RED} Please Enter a valid id {Style.RESET}")
            continue
        else:
            book = books.loc[books['id'] == search_choice]
            if book.empty:
                print(f"\n{Style.BOLD}{Style.RED}No Result Found {Style.RESET}")
                search_again = False
            else:
                clear_screen()
                print("~" * 24 + Style.BOLD + "RESULT" + "~" * 24 + Style.RESET)
                print_book_details(book)
                search_again = False


def issue_book():
    books = pandas.read_csv('books.csv')
    users = pandas.read_csv('users.csv')
    history = pandas.read_csv('issued_history.csv')

    clear_screen()
    now = datetime.now()
    after_one_week = now + timedelta(days=5)
    user = None
    while True:
        print()
        print("~" * 22 + Style.BOLD + "ISSUE BOOK" + "~" * 22 + Style.RESET)
        try:
            user_id = int(input('\nEnter User ID: '))
        except ValueError:
            clear_screen()
            print(f"{Style.BOLD}{Style.RED}Enter a valid user id  {Style.RESET}")
            continue
        user = users.loc[users['id'] == user_id]
        if not user.empty:
            print()
            print("~" * 21 + Style.BOLD + "USER DETAILS" + "~" * 21 + Style.RESET)
            print()
            print_user_details(user)
            break
        else:
            clear_screen()
            print(f"{Style.BOLD}{Style.RED}Enter a valid user id {Style.RESET}")
            continue

    while True:
        try:
            book_id = int(input('Enter Book ID: '))
        except ValueError:
            clear_screen()
            print()
            print("~" * 21 + Style.BOLD + "USER DETAILS" + "~" * 21 + Style.RESET)
            print()
            print_user_details(user)
            print(f"{Style.BOLD}{Style.RED}Enter a valid Book id  {Style.RESET}")
        else:
            book = books.loc[books['id'] == book_id]
            if book.empty:
                clear_screen()
                print()
                print("~" * 21 + Style.BOLD + "USER DETAILS" + "~" * 21 + Style.RESET)
                print()
                print_user_details(user)
                print(f"{Style.BOLD}{Style.RED}No book found{Style.RESET}")
                continue
            else:
                clear_screen()
                print()
                print("~" * 21 + Style.BOLD + "USER DETAILS" + "~" * 21 + Style.RESET)
                print()
                print_user_details(user)
                print("~" * 21 + Style.BOLD + "BOOK DETAILS" + "~" * 21 + Style.RESET)
                print()
                print_book_details(book)

                if book['available'].values.astype(int)[0] > 0:
                    print(f"\n{Style.BOLD}{Style.GREEN}Book available{Style.RESET}")

                    try:
                        answer = input(f'\n{Style.BOLD}Issue this book? (y/N): ')
                    except ValueError:
                        print(f"\n {Style.BOLD}{Style.RED}Book not issued{Style.RESET}")
                        sleep(2)
                        clear_screen()
                        break

                    answer = answer.upper()
                    if answer == 'Y':
                        last = history.tail(1)
                        if last.empty:
                            last = 1
                        else:
                            last = last['id'].values.astype(int)[0] + 1

                        data = pandas.DataFrame({
                            'id': [last, ],
                            'user_id': [user['id'].values.astype(int)[0], ],
                            'username': [user['name'].values.astype(str)[0], ],
                            'book_id': [book['id'].values.astype(int)[0], ],
                            'book_name': [
                                f"{book['title'].values.astype(str)[0]} by {book['author'].values.astype(str)[0]}", ],
                            'issued_date': [now.strftime("%m/%d/%Y"), ],
                            'return_date': [after_one_week.strftime("%m/%d/%Y"), ],
                            'is_returned': "no",
                        })
                        result = pandas.concat([history, data])
                        save_history(result)
                        print(f"\n{Style.BOLD}{Style.GREEN}Book issued successfully{Style.RESET}")
                        books.loc[books['id'] == book_id, 'available'] = books.loc[
                                                                             books['id'] == book_id, 'available'] - 1
                        save_book(books)
                        sleep(2)
                        clear_screen()
                        break
                    else:
                        print(f"\n{Style.BOLD}{Style.RED}Book not issued{Style.RESET}")
                        sleep(2)
                        clear_screen()
                        break
                else:
                    print(f"{Style.BOLD}{Style.RED}Book Not Available{Style.RESET}")
                    sleep(2)
                    clear_screen()
                    print()
                    print("~" * 21 + Style.BOLD + "USER DETAILS" + "~" * 21 + Style.RESET)
                    print()
                    print_user_details(user)
                    continue


def return_book():
    borrowed_books = None
    history = pandas.read_csv('issued_history.csv')
    users = pandas.read_csv('users.csv')
    books = pandas.read_csv('books.csv')
    clear_screen()
    print()
    print("~" * 21 + Style.BOLD + "RETURN BOOK" + "~" * 22 + Style.RESET)
    while True:
        try:
            user_id = int(input('\nEnter User ID: '))
        except ValueError:
            clear_screen()
            print()
            print("~" * 21 + Style.BOLD + "RETURN BOOK" + "~" * 22 + Style.RESET)
            print(f"{Style.BOLD}{Style.RED}Enter a valid user id{Style.RESET}")
            continue
        else:
            user = users.loc[users['id'] == user_id]
            if user.empty:
                clear_screen()
                print()
                print("~" * 21 + Style.BOLD + "RETURN BOOK" + "~" * 22 + Style.RESET)
                print(f"{Style.BOLD}{Style.RED}Enter a valid user id{Style.RESET}")
                print(f"{Style.BOLD}{Style.RED}Enter a valid user id{Style.RESET}")
                continue

            print()
            print("~" * 21 + Style.BOLD + "USER DETAILS" + "~" * 21 + Style.RESET)
            print()
            print_user_details(user)
            borrowed_books = history.loc[history['user_id'] == user_id]
            borrowed_books = borrowed_books.loc[borrowed_books['is_returned'] == 'no']
            if borrowed_books.empty:
                print(f"{Style.BOLD}{Style.RED}No book issued to this user{Style.RESET}")
                sleep(2)
                break
            else:
                print()
                print("~" * 21 + Style.BOLD + "ISSUED BOOKS" + "~" * 21 + Style.RESET)
                print_history(borrowed_books)
            break

    while True:
        try:
            book_id = int(input('\nEnter Returning Book ID: '))
        except ValueError:
            print(f"{Style.BOLD}{Style.RED}Enter a valid book id from issued books{Style.RESET}")
            continue
        else:
            returning_book = borrowed_books.loc[borrowed_books['book_id'] == book_id]
            if returning_book.empty:
                print(f"{Style.BOLD}{Style.RED}Enter a valid book id from issued books{Style.RESET}")
                continue
            else:
                books.loc[books['id'] == book_id, 'available'] = books.loc[books['id'] == book_id, 'available'] + 1
                save_book(books)

                returning_book_record_id = returning_book['id'].values.astype(int)[0] + 1
                history.loc[history['id'] == returning_book_record_id, 'is_returned'] = 'yes'
                save_history(history)

                print(f"\n\n{Style.BOLD}{Style.GREEN}Book Returned successfully{Style.RESET}")
                sleep(2)
                clear_screen()
                break


def issued_history():
    history = pandas.read_csv('issued_history.csv')
    while True:
        clear_screen()
        if len(history) > 0:
            print("~" * 16 + Style.BOLD + "ISSUED BOOKS HISTORY" + "~" * 16 + Style.RESET)
            print_history(history)
            print(f"{len(history)} records found")
        else:
            print(f"{Style.BOLD}{Style.RED}No records found {Style.RESET}")
        try:
            _ = input(Style.BOLD + Style.BLUE + "\n\bGo to main menu?" + Style.RESET)
        except ValueError:
            clear_screen()
            break
        clear_screen()
        break


def add_book():
    clear_screen()
    print("~" * 21 + Style.BOLD + "ADD NEW BOOK" + "~" * 21 + Style.RESET)
    print()
    books = pandas.read_csv('books.csv')
    title = None
    author = None
    genres = None
    publication_year = None
    language = None
    copies = None
    while True:
        try:
            title = input('Enter book title : ')
        except ValueError as e:
            print(f"{Style.BOLD}{Style.RED}Enter a valid title\n {Style.RESET}")
            continue
        else:
            if title:
                break
            else:
                print(f"{Style.BOLD}{Style.RED}Enter a valid title\n {Style.RESET}")
                continue
    while True:
        try:
            author = input('Enter author name : ')
        except ValueError:
            print(f"{Style.BOLD}{Style.RED}Enter a valid name\n {Style.RESET}")
            continue
        else:
            if author:
                break
            else:
                print(f"{Style.BOLD}{Style.RED}Enter a valid name\n {Style.RESET}")
                continue

    while True:
        try:
            genres = str(input('Enter book genres : '))
        except ValueError:
            print(f"{Style.BOLD}{Style.RED}Enter a valid genres\n {Style.RESET}")
            continue
        else:
            if not genres.isalpha():
                print(f"{Style.BOLD}{Style.RED}Enter a valid genres\n {Style.RESET}")
                return False
            else:
                break

    while True:
        try:
            publication_year = int(input('Enter publication year : '))
        except ValueError:
            print(f"{Style.BOLD}{Style.RED}Enter a valid year\n {Style.RESET}")
            continue
        else:
            today = date.today()
            if publication_year > today.year:
                print(f"{Style.BOLD}{Style.RED}Enter a valid year\n {Style.RESET}")
                continue
            else:
                break

    while True:
        try:
            language = str(input('Enter book language : '))
        except ValueError:
            print(f"{Style.BOLD}{Style.RED}Enter a valid language\n {Style.RESET}")
            continue
        else:
            if not language.isalpha():
                print(f"{Style.BOLD}{Style.RED}Enter a valid language\n {Style.RESET}")
                continue
            else:
                break

    while True:
        try:
            copies = int(input('Enter number of copies: '))
        except ValueError:
            print(f"{Style.BOLD}{Style.RED}Enter a valid number\n {Style.RESET}")
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
    print(f"{Style.BOLD}{Style.GREEN}\n\nBOOK SAVED\n {Style.RESET}")
    sleep(2)
    clear_screen()
    save_book(result)
