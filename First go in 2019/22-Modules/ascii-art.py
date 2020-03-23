from pyfiglet import figlet_format
from termcolor import colored
from colorama import init

def print_art(msg, color):
	valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

	if color not in valid_colors:
		color = "magenta"

	ascii_art = figlet_format(msg)
	colored_ascii = colored(ascii_art, color=color, attrs=['bold'])
	print(colored_ascii)


init()

msg = input("What would you like to print? ")
color = input("What color? ")

print_art(msg, color)