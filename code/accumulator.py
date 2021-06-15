
data = [37.5, -0.01, 99.34, 14.7, 1001.0, -6.8, 652.45]
counter = 0
for item in data:
  if item < 0:
    counter = counter + 1
print("Number a values < 0: ", counter)

output = ""
for i in range(10):
  output += "*"
  print(output)


