import requests
import time
from random import choice
from pyfiglet import figlet_format
from termcolor import colored, cprint
from colorama import init


init()  # initalizes the colors

available_colors = ('red', 'green', 'yellow', 'blue',
                    'magenta', 'cyan')
random_color = choice(available_colors)

negative_responses = ('n', 'no', 'nah', 'nope')

header = figlet_format("Dad Joke 3000")
header = colored(header, color=random_color, attrs=['bold'])
print(header)

while True:
    term = input("Let me tell you a joke! Give me a topic: ")
    response_json = requests.get(
        "https://icanhazdadjoke.com/search",
        headers={"Accept": "application/json"},
        params={"term": term}
    ).json()

    results = response_json["results"]
    total_jokes = response_json["total_jokes"]

    if total_jokes > 1:
        print(
            f"I've got {total_jokes} {colored(term, color=random_color, attrs=['bold'])} jokes. Here's one: ")

        first_try = True
        while True:
            random_result = choice(results)
            idx = results.index(random_result)   # index of the random_result

            if not first_try:
                print("\nHere's another:")
            cprint(random_result['joke'], color='yellow', attrs=['bold'])

            results.pop(idx)  # remove used result
            total_jokes -= 1  # less jokes to choose from
            first_try = False  # no more "Here's another" print

            if total_jokes >= 1:
                another = input(
                    f"Another {term} joke? (y/n) > ")
                if another.lower() not in negative_responses:
                    continue
            break
    elif total_jokes == 1:
        print(f"I've got one joke about {term}. Here it is:\n")
        cprint(results[0]['joke'], color='yellow', attrs=['bold'])
    else:
        print(f"Sorry, I don't have any jokes about {term}! Please try again.")

    again = input("Search more jokes? (y/n) > ")
    if again.lower() in negative_responses:
        cprint("\nThank you for listening to my jokes!",
               color=random_color, attrs=['bold'])
        time.sleep(1)  # delay in seconds
        break
    print("\n")
