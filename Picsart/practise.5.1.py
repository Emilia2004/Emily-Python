file = open("peterrabbit.txt",mode = "r")
lines = file.read().splitlines()
file.close()
file = open("peterrabbit.txt",mode = "w")
for line in lines:
    tokens = line.split()
    for i in range(len(tokens)):
        if len(tokens[i]) == 3:
            tokens[i] = f"({tokens[i]})"
        elif len(tokens[i]) == 4:
            tokens[i] = f'"{tokens[i]}"'
        elif len(tokens[i]) == 3:
            tokens[i] = f"'{tokens[i]}'"
        elif len(tokens[i]) == 6:
            tokens[i] = f"<{tokens[i]}>"
    newline = " ".join(tokens)
    file.write(newline+"\n")
file.close()
