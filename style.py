# Class of different styles
import os

os.system("")


class Style:
    BOLD = "\033[1m"
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


def clear_screen():
    try:
        os.system('clear')
    except Exception as e:
        print(e)
        os.system('cls')
