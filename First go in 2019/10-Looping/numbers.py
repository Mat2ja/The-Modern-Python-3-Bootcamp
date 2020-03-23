# Main Solution
for num in range(1, 21):
    if num == 4 or num == 13:
        print(f"{num} is unlucky")
    elif num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

print("\n")

# Slight Refactor
for num in range(1, 21):
    if num == 4 or num == 13:
        state = "unlucky".upper() #ako bi htjeli uppercase
    elif num % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{num} is {state}")
    #print(f"{num} is " + state)
    #print(str(num) + " is " + state)
