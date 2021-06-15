

def main():
  L = list("ABCD")
  print(L)
  change2(L)
  print(L)

def change2(mylist):
  mylist[2] = "pony"
  # note...no return statement needed

main()
