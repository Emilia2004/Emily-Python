user_name = input("Enter name of user: ")
user_surname = input("Enter surname of user: ")
user_age = int(input("Enter age of user: "))
user_city = input("Enter city of user: ")
def user_profile(name,surname,*,age,city):
    print(name,surname,age,city)
user_profile(user_name,user_surname,age = user_age,city = user_city)
