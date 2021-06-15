

def main():
  x = 5
  result = functionA(x)
  print("result: ", result)

def functionA(y):
  y = y*2
  answer = functionB(y)
  return answer 

def functionB(z):
  z = z + 1
  return z

main()
