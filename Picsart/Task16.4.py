fs = open("peterrabbit.txt",mode = "r")
x = fs.read()
text = x.split()
example = 0
all = 0
word = 0
up = 0
did = 0
him = 0
for i in text:
    if i == "example":
        example += 1
    elif i == "all":
        all += 1
    elif i == "word":
        word += 1
    elif i == "up":
        up += 1
    elif i == "did":
        did += 1
    elif i == "him":
        him += 1
print("example: ",example )
print("all: ",all)
print("word: ",word)
print("up: ",up)
print("did: ",did)
print("him: ",him)
