def repeat_element(element, times):
    for i in range(times):
        yield element


element = input("Enter element you want to repeat: ")
times = int(input("Enter how many times to repeat: "))

gen = repeat_element(element,times)
for i in gen:
    print(i)
