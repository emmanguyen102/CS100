def convert_grades(list):
    """
    oop over the numbers in the parameter list and replace every grade greater than zero with the value 6
    :param list: a list as parameter
    :return: nothing
    """
    if len(list) == 0:
        pass
    else:
        for i in range(0, len(list)):
            if list[i] > 0:
                list[i] = 6

def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]

if __name__ == "__main__":
    main()
