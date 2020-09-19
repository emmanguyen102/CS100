"""
COMP.CS.100 Programming 1
Hang Nguyen, hang.t.nguyen@tuni.fi, student id K429778
Code template for geometric shapes.
"""

import math

def square_circumference(a):
    """
    Calculates total circumference of square
    :param a: length of 1 side
    :return: circumference of square
    """
    return (4*a)

def square_surface_area(a):
    """
    Calculates surface area of square
    :param a: length of square
    :return: surface area of square
    """
    return (a*a)

def rectangle_circumference(a,b):
    """
    Calculates total circumferences of a rectangle
    :param a: side 1
    :param b: side 2
    :return: total circumferences of a rectangle
    """
    return (2*(a+b))

def rectangle_surface_area(a,b):
    """
    calculates surface area of a rectangle
    :param a: side 1
    :param b: side 2
    :return: surface area of a rectangle based on side1, side 2
    """
    return (a*b)

def circle_circumference(a):
    """
    Calculates total circumference of a circle
    :param a: radius
    :return: total circumferences of a circle
    """
    return (2*a*math.pi)

def circle_surface_area(a):
    """
    Calcualtes surface area of a circle
    :param a: radius
    :return: calculates surface area of a circle
    """
    return (a*a*math.pi)

def menu():
    """
    This function prints a menu for user to select which
    geometric shape to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter, q stops this (s/r/q): ")
        while answer == "s":
            s_len = float(input("Enter the length of the square's side: "))
            if s_len <= 0:
                continue
            else:
                print("The total circumference is", "{0:.2f}".format(square_circumference(s_len)))
                print("The surface area is", "{0:.2f}".format(square_surface_area(s_len)))
                break
        while answer == "r":
            r_len_1 = float(input("Enter the length of the rectangle's side 1: "))
            if r_len_1 <= 0:
                continue
            while r_len_1 >0:
                r_len_2 = float(input("Enter the length of the rectangle's side 2: "))
                if r_len_2 <=0:
                    continue
                else:
                    print("The total circumference is", "{0:.2f}".format(rectangle_circumference(r_len_1, r_len_2)))
                    print("The surface area is", "{0:.2f}".format(rectangle_surface_area(r_len_1, r_len_2)))
                    break
            break
        while answer == "c":
            circle_radius = float(input("Enter the circle's radius: "))
            if circle_radius <= 0:
                continue
            else:
                print("The total circumference is", round(circle_circumference(circle_radius),2))
                print("The surface area is", round(circle_surface_area(circle_radius),2))
                break
        if answer == "q":
            break
        if answer != "q" and answer != "c" and answer != "s" and answer != "r":
            print("Incorrect entry, try again!")

        print()  # Empty row for the sake of readability


def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()
