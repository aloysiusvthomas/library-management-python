from books import add_book
from books import issue_book
from books import issued_history
from books import list_books
from books import return_book
from books import search_books
from style import clear_screen
from users import login

authenticated_user = None

clear_screen()
while authenticated_user is None:
    is_logged_in = False
    while is_logged_in is False:
        is_logged_in, authenticated_user = login()

is_admin = bool(authenticated_user['is_admin'].values.astype(int)[0])

while True:
    print(
        """
        1. List all Books.\n
        2. Search.\n
        3. Issued Books.\n
        4. Return Book.\n
        """
    )
    if is_admin:
        print(
            """
            5. Issue Book.\n
            6. Add Book.\n
            7. Add User.\n
            """
        )
    print("Please select a choice to continue\n")
    choice = int(input('Enter your Choice : '))

    if choice == 1:
        list_books()
    elif choice == 2:
        search_books()
    elif choice == 3:
        issue_book()
    elif choice == 4:
        return_book()
    elif choice == 5:
        issued_history()

    elif choice == 6:
        add_book()
    else:
        print("ha")
