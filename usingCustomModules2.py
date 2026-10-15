import moduleMain as mwm
# from moduleMain import area as area

def main():
    print(__name__)
    num = int(input("Enter a radius: "))
    print(f"The area of a circle with a radius of {num} is {mwm.area(num)}")
    mwm.main()


if __name__ == "__main__":
    main()