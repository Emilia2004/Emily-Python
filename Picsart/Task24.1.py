def counter_statistics(file_path: str):
    fs = open(file_path, 'r')
    content = fs.read()
    fs.close()

    line_count = content.count('\n')
    words_count = len(content.split())
    characters_count = sum(len(item) for item in content.split())
    print(line_count)
    print(words_count)
    print(characters_count)
    
    fs = open(file_path, 'r')
    
    lines = fs.readlines()
    line_count = len(lines)
    word_count = sum(len([item.split() for item in lines]))
    
    print(line_count)
    print(word_count)
counter_statistics("file.txt")

