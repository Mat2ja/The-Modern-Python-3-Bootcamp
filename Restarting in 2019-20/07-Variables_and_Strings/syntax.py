x = 2 # int
y = 2.0 # float
active = False # boolean is always Uppercase
name = "Matija"
town = 'zagreb'
age = '19'

newline = "\n"


print(x)
print(y)
print(active)
active = True
print(active)
print(name + " " + town.capitalize() + newline + age)

print()

'''DYNAMIC TYPING'''
# variable types can be changed by giving it different value (int can become string/boolean...)
print(type(x))
x = "string"
print(type(x))


''' \ - ALT + Q
\n - new line
\t - tabulator
\\ - \
\b - backspace
'''

'''CONCATENATION'''
str_one = "ice"
str_two = "cream"

print(str_one + " " + str_two)
str_one += " cream"
print(str_one);

# python3
time = 4
print(f"I've told you {time} times already!")
formatted = f"I've told you {time + 1} times already!"
print(formatted)

#python2
formatted = "\nI've told you {} times already!".format(time)
print(formatted)

#oldest way (deprecated)
formatted = "\nI've told you %d times already!" % (time)
print(formatted)



'''CONVERTING DATA TYPES'''
decimal = 12.4364253
integer = int(decimal)
print(integer) #12

my_list = [1, 2, 3]
print(my_list)
my_list_as_string = str(my_list)
print(my_list_as_string) #stored as '[1, 2, 3]', printed without quotation marks
