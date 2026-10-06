def PerimeterCircle():
    radius = float(input("\nEnter radius of circle: "))
    pi = 3.14159265359
    return 2 * pi * radius

strInput = 'y'

while not strInput == 'n':
    print(f"Circle Perimeter {PerimeterCircle():.2f} \n")
    strInput = input("Continue? [y/n]: ").casefold()

