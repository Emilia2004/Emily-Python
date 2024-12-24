def manually_iterates(numbers):
    iterator=iter(numbers)

    while True:
        number=next(iterator, None)
        if number is None:
            break
        print(number)

ls=[12,22,3,78,51]
manually_iterates(ls)

