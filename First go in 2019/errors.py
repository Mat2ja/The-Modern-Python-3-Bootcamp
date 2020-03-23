'ERRORS'

# https: // docs.python.org/3/library/exceptions.html

# - SyntaxError - extra colon
# - NameError - name not defined
# - TypeError - wrong type
# -         len(5) ili 3 + 's'
# - IndexError - index that doesn't exist
# - ValueError - argument with right type but innapropriate value
# -         int("foo")
# - KeyError - when dict doesn't have a specific key
# - AtributeError - when a variable doesn't have an atttribute
# -         [1,2,3].hello() - hello() doesn't exist


'OUR OWN ERRORS'
# - raise ERROR_NAME("my text")
#       - raise ValueError('five is invalid color')

# - raise Exception("...")



'HANDLE ERRORS'
# try:
#    ...
# except ErrorName as err:
#    ...
# else:
#    ...
# finally:
#   ...


'DEBUGGING'
import pdb; pdb.set_trace()
# l - list
# n - next line
# p - print
# c - continue = finish debugging
