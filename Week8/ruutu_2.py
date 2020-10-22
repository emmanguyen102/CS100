def print_box(a, b, c):
    """
    The function prints
    :param a: int, random number
    :param b: int, random number
    :param c: int, random number
    :return: nothing, but print the matrix of a*b
    """
    for i in range(0, int(b)):
        for j in range(0, int(a)):
            print(c, end='')
        print()

def read_input(sentence):
    """
    :param sentence: the phrase for user input
    :return: the number
    """
    while True:
        num = input(sentence)
        try:
            num = int(num)
            if num > 0:
                break
            else:
                continue
        except:
            continue
    return num

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()
    print_box(width, height, mark)

if __name__ == "__main__":
    main()
