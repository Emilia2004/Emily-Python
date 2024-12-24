def make_logger(level):
    def log(message):
        print(level,message)
    return log
error = make_logger("Error!")
error("Syntax error:")
