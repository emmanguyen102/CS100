from math import sqrt
def area(a, b, c):
    """
    :param a: 1 side of the triangle
    :param b: the other side of the triangle
    :param c: the other side of the triangle
    :return: the area calculated based on 3 sides of triangle
    """
    s = (float(a)+float(b) + float(c))/2
    area_cal = sqrt(s*(s-float(a))*(s-float(b))*(s-float(c)))
    return area_cal

def main():
    line_1 = input("Enter the length of the first side: ")
    line_2 = input("Enter the length of the second side: ")
    line_3 = input("Enter the length of the third side: ")

    print(f"The triangle's area is {area(line_1, line_2, line_3):.1f}")


if __name__ == "__main__":
    main()
