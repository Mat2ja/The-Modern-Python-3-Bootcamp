kms = None
question = "How many kilometers did you run today?"

print(question) 
kms = input()  # get user input, type(string)
# kms = input("How many kilometers did you run today? ")

# input() uvijek prima string pa treba konverzija, ili odmah: kms = float(input())

miles = float(kms)/1.60934  # convert from string to float and divide
miles = round(miles, 2)  # round the result

print(f"Your {kms}km run was {miles}mi")