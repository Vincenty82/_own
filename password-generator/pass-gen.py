#modules

import random
import string
import sys

#variables

password = str()                                                            # Reserve password as string
character_str = string.digits + string.ascii_letters + string.punctuation   # Define character string to choose from
password_length = 16                                                        # Define default password lenght
formatting_reset = "\033[0;0m"                                              # ANSI SGR control sequence
main_loop_check = True

#classes

class fg_color:                                                             # ANSI SGR control sequence
    black_0 = "\033[0;30m"
    red_0 = "\033[0;31m"
    green_0 = "\033[0;32m"
    yellow_0 = "\033[0;33m"
    blue_0 = "\033[0;34m"
    magenta_0 = "\033[0;35m"
    cyan_0 = "\033[0;36m"
    white_0 = "\033[0;37m"
    black_1 = "\033[1;30m"
    red_1 = "\033[1;31m"
    green_1 = "\033[1;32m"
    yellow_1 = "\033[1;33m"
    blue_1 = "\033[1;34m"
    magenta_1 = "\033[1;35m"
    cyan_1 = "\033[1;36m"
    white_1 = "\033[1;37m"

class bg_color:                                                             # ANSI SGR control sequence
    black_0 = "\033[0;40m"
    red_0 = "\033[0;41m"
    green_0 = "\033[0;42m"
    yellow_0 = "\033[0;43m"
    blue_0 = "\033[0;44m"
    magenta_0 = "\033[0;45m"
    cyan_0 = "\033[0;46m"
    white_0 = "\033[0;47m"
    black_1 = "\033[1;40m"
    red_1 = "\033[1;41m"
    green_1 = "\033[1;42m"
    yellow_1 = "\033[1;43m"
    blue_1 = "\033[1;44m"
    magenta_1 = "\033[1;45m"
    cyan_1 = "\033[1;46m"
    white_1 = "\033[1;47m"

#funkcje

def main_menu():
    sys.stdout.write(fg_color.green_0)
    print("\n1. Generate password.")
    print("2. Set password lenght.")
    print("3. Exit.\n")
    sys.stdout.write(formatting_reset)
    return int(input("Type the option number and press Enter:"))

def generate_password(a):
    password = str()
    for i in range(a):
        password = password + (random.choice(character_str))
    return password

#program

while main_loop_check: 
    if main_menu() == 1:
        print(f"\n{generate_password(password_length)}")
    elif main_menu() == 2:
        password_length = int(input("\nWhat is the desired password lenght?:"))
    else:
        main_loop_check = False

#wynik

# print(password)