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
