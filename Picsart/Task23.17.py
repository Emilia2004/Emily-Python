def c_f(celsius):
    return celsius * 9/5 + 32

def c_k(celsius):
    return celsius + 273.15

def f_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def f_k(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def k_c(kelvin):
    return kelvin - 273.15

def k_f(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

dict = {"celsius_to_kelvin" : c_k,
        "celsius_to_fahrenheit" : c_f,
        "fahrenheit_to_celsius" : f_c,
        "fahrenheit_to_kelvin" : f_k,
        "kelvin_to_celsius" : k_c,
        "kelvin_to_fahrenheit" : k_f
        }

def convert_temperature(value, from_unit, to_unit):
    any = dict[f"{from_unit}_to_{to_unit}"]
    print(any(value))
value = int(input("Enter value you want to change:"))
fromm = input("Enter from unit: ")
to = input("Enter to unit: ")
convert_temperature(value,fromm,to)
