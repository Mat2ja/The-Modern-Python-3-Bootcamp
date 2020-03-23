numbers = range(1,21)

for num in numbers:
    if num == 4 or num == 13:
        print(f"{num} is unlucky")
    elif num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")