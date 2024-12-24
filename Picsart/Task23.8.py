def make_greeting(greeting):
    def greet(name):
        print(greeting,name)
    return greet

greeting = input("Enter greeting message: ")
name = input("Enter user's name: ")
func = make_greeting(greeting)
func(name)
