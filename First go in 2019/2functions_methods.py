'BUILT IN FUNCTIONS'

#  - all([...]) - returns True if all elements of the iterable are true
#          - all([num % 2 == 0 for n in nums])
#          - moze i bez [] - ako netrebamo listu, ako samo generiramo jednom i ne storamo ju
#                         - GENERATOR EXPRESSION - saves a lot of space
#  - any([...]) - True if any element is true

#  - sorted(list or tuple) - vraca sortiranu listu, ne mijenja original (to radi lista.sort())
#          - sorted(..., reverse=True) - reverse
#          - sorted(..., key=..., moze i reverse=True kao trece)

#  - max(...) 
#          - (..., key=...) - drugi argument je sortiranje
#  - min(...)

#  - reversed(list or tuple) - vraca kopiju, ne mijenja original, pretvorit u listu ako ocemo print
#                             ali bolje korisitit slice[::-1] jer obrne cijelu string, a ne radi da svaki char svoj string
#          - for char in reversed("hello world"):
#                print(char)
#          - for x in range(0,10)[::-1]:       for x in reversed(range(0,10)):   (JEDNAKO!!)
#                  print(x)                            print(x)
    
#  - len(...)     ili      nesto.__len__() - samo 1 argument  
#  - abs(...)
#          - fabs(...) - import math, konvertira u float
#  - sum(...) - 2. argumnet je start, 0 by default
#  - round(...,dec_points) - ako samo 1 arg, zaokruzi 3.6 je 4 - round(3.6,None)

#  - zip(a,b) - spaja liste a i b u tuple parove, unutar jedne liste [(prvi iz a i prvi iz b),(...)...]
#              jos treba pretvorit u listu/dict il bilosta - list(zip(a,b,c...))
#          - list(zip(*lista)) - unpacka listu tuplesa
    



'CLASS'
# __init__
# __repr__

# cls
# self

# isinstance(nesto, klasa)

# @classmethod  
# @property
# @nesto.setter

# super().__init__(name, species='cat') - doesn't have self !!! 

# METHOD RESOLUTION ORDER
# class_name.__mro__
# class_name.mro()
# help(class_name) - NAJBOLJE

# raise NotImplementedError

# METHODS - https://docs.python.org/3/reference/datamodel.html
# __init__
# __repr__ 
# __str__
# __len__
# __add__    +
# __mul__    *




'READ & WRITE'
# with open('filename') as file_object:
# .read()
# .readlines()
# .rstrip() - remove new lines from the right side
# .replace()

# with open('filename', 'w') as file_object:
# .write()

'JSON'''
# import json
# var = json.load(file_object)
# json.dump(thing, file_object)

 


'TESTING'
# import unittest
# class ...TestCase(unittest.TestCase):
#       def test_....(self)                              - testira funkciju
#               nesto = ...
#               self.assertEqual(nesto, 'izgleda_ovako') - trebaju bit jedanko
# unittest.main() - runs the test

# def setUp(self)

# assertEqual(a, b) - Verify that a == b
# assertNotEqual(a, b) - Verify that a != 
# assertTrue(x) - Verify that x is True
# assertFalse(x) - Verify that x is False
# assertIn(item, list) - Verify that item is in list
# assertNotIn(item, list) - Verify that item is not in list



'ITERATORS'
# a = iter(...)
# next(a) - kad prode, gotovo je, nema ispocetka



'GENERATOR FUNCTIONS' # can return more than once, when invoked it returns a generator
# yield (instead return)
# when called, its a generetaor object, we place it in a variable and call next(variable)

