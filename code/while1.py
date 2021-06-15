
from random import *

value = 0
limit = 10
while value < limit:
   print("value: %2d -- limit = %2d" % (value, limit))
   print("picking random number from 1-10...")
   randnumber = randrange(1,11)
   print(">>>>> picked %d" % randnumber)
   if randnumber > 6:
      value = value + 2
print("-"*30)
print("Done!")

