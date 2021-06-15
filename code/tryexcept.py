

VALIDINPUT = False
while not VALIDINPUT:
  age = input("How old are you? ")
  try:
    age = float(age)
    VALIDINPUT = True
  except ValueError:
    print("Please enter a number...")
print("Thanks!")
