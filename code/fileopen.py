

VALIDFILE = False
while not VALIDFILE:
  filename = input("File to open: ")
  try:
    infile = open(filename, "r")
    VALIDFILE = True
  except FileNotFoundError:
    print("I couldn't find that file...")
print("Got it!")
