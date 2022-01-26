from books import add_book
from books import issue_book
from books import issued_history
from books import list_books
from books import return_book
from books import search_books
from style import clear_screen
from style import Style
from users import add_user
from users import list_users
from users import login

authenticated_user = None

clear_screen()
while authenticated_user is None:
    is_logged_in = False
    while is_logged_in is False:
        is_logged_in, authenticated_user = login()

is_admin = bool(authenticated_user['is_admin'].values.astype(int)[0])

while True:
    print("")
    print("~" * 25 + Style.BOLD + "MENU" + "~" * 25 + Style.RESET)
    print("\n\n Please Select a choice to continue\n\n")
    print("1. List all Books.")
    print("2. Search Books by ID.")
    print("3. Issue Books.")
    print("4. Return Books.")
    print("5. Issued Books History.")
    print("6. Add Books.")
    print("7. Add User.")
    print("8. List All User.")
    print("9. Exit.")
    print()
    print()
    print(Style.BOLD + "~" * 54 + Style.RESET)

    choice = int(input(Style.BOLD + '\nChoice : ' + Style.RESET))

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
        continue
    elif choice == 6:
        add_book()
        continue
    elif choice == 7:
        add_user()
        continue
    elif choice == 8:
        list_users()
        continue
    elif choice == 9:
        print("""
             ████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗
             ╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║
             ░░░██║░░░███████║███████║██╔██╗██║█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║
             ░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║
             ░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝
             ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░""")
        break
    else:
        clear_screen()
        print(f"Choice: {choice}")
        print(Style.BOLD + Style.RED + "Invalid Choice " + Style.RESET)
        continue
