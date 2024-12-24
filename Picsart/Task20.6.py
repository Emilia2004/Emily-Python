title = input("Enter title of report: ")
author = input("Enter author of report: ")
def report(title,author,*,year=2023,place="Yerevan"):
    print(title,author,year,place)
report(title,author)
report(title,author,place="New York")
