from termcolor import colored, cprint
from colorama import init
import sys

init()


def divide(a, b):
    '''divides two given numbers'''
    try:
        result = a/b
    except ZeroDivisionError:
        cprint("Don't divide by zero!", 'red', attrs=['bold'])
    else:
        cprint(f"{a} divided by {b} is {round(result, 2)}",
               color='yellow', attrs=['bold'])


cprint("\tLet's divide some numbers!!!",
       color='yellow', attrs=['bold'])
# print(colored("\tLet's divide some numbers!!!", color='yellow', attrs=['bold']))


while True:
    # DEBUGGING
    # import pdb; pdb.set_trace()
    try:
        a = int(input("\n\ta is "))
        b = int(input("\tb is "))
    except ValueError as err:
        cprint("Must be a number!", 'red', attrs=['bold'])
        cprint(f"---> {err}", 'red', attrs=['bold'])
        continue

    divide(a, b)

    repeat = input("Start over? (y/n) > ")
    if repeat == 'n':
        cprint(
            "\n##### Thank you for trying my program! #####", color='cyan', attrs=['bold'])
        break
