"""(Lists, Control Flow and Sorting):
1. Initialize a list with 100 random variables ranging from one to ten.
2. Implement a function to sort the variables ascending."""

import random as r

mylist = []

for i in range (0,100):
    mylist.append(r.randrange(1,11))

mylist.sort()

print mylist
