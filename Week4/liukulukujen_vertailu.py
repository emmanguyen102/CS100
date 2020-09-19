def compare_floats(a, b, c):
    """
    This function compares minus of 2 floating-point numbers sensibly with EPSILON

    :param a: 1st floating number
    :param b: 2nd floating number
    :param c: EPSILON
    :return: Boolean values
    """
    result = abs(a-b)
    if result < c:
        return True

    else:
        return False

def main():
    EPSILON = 0.000000001
    compare_floats(0.00000000000000000001, 0.0000000000000000002, EPSILON)
    compare_floats(0.0002, 0.0000002, EPSILON)


if __name__ == "__main__":
    main()
