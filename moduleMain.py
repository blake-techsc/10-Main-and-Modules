pi = 3.141592653

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def circumference(radius):
    return 2 * pi * radius

def area(radius: float) -> float:
    """
    Takes radius of circle and returns the area
    """
    return pi * (radius ** 2)

def main():
    print(area(7))
    print("America ya!")
    print(pi)
    # every python file (module) has a certain built in variable called __name__
    # if you run the file directly, __name__ is "__main__"
    # if you import the file __name__ becomes the name of the script
    print(__name__)
    print("America ya!")

if __name__ == "__main__":
    main()