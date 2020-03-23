""" # gives us a class type of an object
>>> type(54)
<class 'int'>
>>> type(1.1)
<class 'float'>
>>> type("tekst")
<class 'str'>

>>> child = None
>>> type(child)
<class 'NoneType'>


>>> int(5)
5
>>> float(5)
5.0
>>> int(5.5)
5

# if any of the values is a float, result will be a float
>>> 1+3
4
>>> 1+1.0
2.0
>>> 32 / 6
5.333333333333333
>>> 5**2 # exponent
25
>>> 25 ** 0.5 # square root of 25
5.0
>>> 14%5 # modulo - ostatak dijeljenja
4
>>> 14/5 # result of division is always a float, even when dividing two ints
2.8
>>> 1/2 # result of division is always a float
0.5
>>> 14//5 # integer division - removes the decimals, always rounds "down" (4.6 is 4)
2
>>> 14.0//5 # int division
2.0
>>> 10 * 4 # result is an int
40
>>> 10 * 4. # result is a float
40.0


  """