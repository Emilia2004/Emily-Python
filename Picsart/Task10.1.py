word = input()
z = 0
for i in range(len(word)):
    if word[i] == "z":
        z = i
        break
if z>0:
    print(z)
else:
     print("Character not found")
