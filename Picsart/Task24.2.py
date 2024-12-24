def process_json(file_path):
    fs = open(file_path)
    return fs.read()


ls = process_json('input.json')
print(ls)
