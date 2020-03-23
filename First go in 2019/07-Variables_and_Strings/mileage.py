print("How many kilometers did you cycle today?")
kms = input()  # get user input

# input() uvijek prima string pa treba konverzija, ili odmah:
# kms = float(input())

miles = float(kms)/1.60934  # convert from string to float and divide
miles = round(miles, 2)  # round the result

print(f"Your {kms}km ride was {miles}mi ")

# ROUND SYNTAX:
# round(thing to round, how many decimal points)
