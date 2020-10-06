def print_box(a, b, c):
    for i in range (0, int(b)):
        for j in range(0, int(a)):
            print(c, end='')
        print()

def main():
    width = input("Enter the width of a frame: ")
    height = input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
