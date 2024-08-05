def areacircle(r):
    return 3.14*r*r
def areasquare(a):
    return a*a
def arearectangle(a,b):
    return a*b
def areatriangle(a,h):
    return a*h/2

dict = {"circle" : areacircle,
        "square" : areasquare,
        "rectangle" : arearectangle,
        "triangle" : areatriangle
        }
def calculate_shape(shape,**kwargs):
    s = dict[shape]
    return s(**kwargs)

shape = input("Enter shape: ")
if shape == "circle":
    radius = int(input("Enter radius of circle: "))
    print("Area of circle is:",calculate_shape(shape,r=radius))
if shape == "square":
    side  = int(input("Enter side of square: "))
    print("Area of square is:",calculate_shape(shape,a=side))
if shape == "rectangle":
    side1 = int(input("Enter width of rectangle: "))
    side2 = int(input("Enter length of rectangle: "))
    print("Area of rectangle is:",calculate_shape(shape,a=side1,b=side2))
if shape == "triangle":
    height = int(input("Enter height of triangle: "))
    base = int(input("Enter base of triangle: "))
    print("Area of triangle is:",calculate_shape(shape,a=base,h=height))
