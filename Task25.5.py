def read_file_lines(file_path):
    file = open(file_path, mode = 'r')
    for line in file:
        yield line.strip()


file_path = "file.txt"
gen = read_file_lines(file_path)
for i in gen:
    print(i)
