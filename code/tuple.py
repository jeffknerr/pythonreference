

def minmax(L):
  """given a list, find and return min and max"""

  min = L[0]
  max = L[0]
  for item in L:
    if item < min:
      min = item
    if item > max:
      max = item
  return min,max

result = minmax([30,45,-4,200,5,6,37,99])
print(result)
print(type(result))
