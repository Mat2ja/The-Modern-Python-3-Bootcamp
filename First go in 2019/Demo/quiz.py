
x = 0
y = -1

x or y and x - 1 == y and y + 1 == x

'''
Here it is broken down: x or y # truthy because y is -1 which is a nonzero value; 
x - 1 == y # true because x - 1 is -1, and -1 == -1; 
x or y and x - 1 == y # true because both sides of the AND are truthy; 
y + 1 == x # truthy because -1 + 1 does in fact equal zero; 
x or y and x - 1 == y and y + 1 == x # also truthy because both sides of the second AND are truthy
'''
