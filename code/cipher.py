

word = "dog"
newword = ""
for letter in word:
  newnumber = ord(letter) + 3
  newletter = chr(newnumber)
  newword = newword + newletter
print(word, newword)

