fs = open("exclusive_mode.txt",mode = "x",errors = "FileExistError")
fs.write("Hello there!")
