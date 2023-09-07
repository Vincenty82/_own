#modules

import os
import platform
import random
import string
import sys

#variables

character_str = string.digits + string.ascii_letters + string.punctuation       # Define character string to choose from.
pswrd_len = 16                                                                  # Define default password lenght.
formatting_reset = "\033[0;0m"                                                  # ANSI SGR control sequence   -> back to default formatting <-
main_loop_check = True                                                          # Reserve main menu loop check initial state. 

#classes

class fg_color:                                                                 # ANSI SGR control sequence   -> foreground color <-   *_0 = reset previous formatting   *_1 = keep previous formatting
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

class bg_color:                                                                 # ANSI SGR control sequence   -> background color <-   *_0 = reset previous formatting   *_1 = keep previous formatting
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
    print("2. Set password length.")
    print("3. Exit.\n")
    sys.stdout.write(formatting_reset)
    while True:
        try:
            choice = int(input(fg_color.cyan_0 + os.getlogin() + "@" + platform.system() + ":> " + formatting_reset))
            break
        except ValueError:
            print(fg_color.red_0 + "\nOnly nubers are supported.\n" + formatting_reset)
    return choice

def generate_password(password_length):                                                                                                 # Generate password
    password = str()                                                                                                                    # Reserve password as string
    for i in range(password_length):
        password = password + (random.choice(character_str))
    print(fg_color.cyan_0 + "\nThis is your " + f"{password_length}" + " character long password:" + formatting_reset)
    print(password)
    return password

def password_length():                                                                                                                  # Set password length
    while True:
            try:
                password_length = int(input("\n" + fg_color.cyan_0 + "What is the desired password lenght? " + formatting_reset))
                break
            except ValueError:
                print(fg_color.red_0 + "\nOnly nubers are supported." + formatting_reset)
    return password_length

#program

print("\n" + bg_color.cyan_0 + "Welcome to the password generator. Choose what you would like to do next." + formatting_reset)
while main_loop_check: 
    main_menu_check = main_menu()
    if main_menu_check == 1:
        pswrd = generate_password(pswrd_len)
    elif main_menu_check == 2:
        pswrd_len = password_length()
    elif main_menu_check == 3:
        main_loop_check = False
    else:
        print(fg_color.red_0 + "\nChoose one of the available options." + formatting_reset)
