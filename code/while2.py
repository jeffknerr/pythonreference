
from random import *

factor = 9
inarow = 0
while inarow < 3:
   otherfactor = randrange(2,13)   # pick number 2-12
   answer = factor * otherfactor
   question = "What is %d*%d? " % (factor,otherfactor)
   useranswer = int(input(question))
   if useranswer == answer:
     inarow = inarow + 1
   else:
     print("Nope...answer = %d" % answer)
     inarow = 0
print("Three in a row...good work!")
