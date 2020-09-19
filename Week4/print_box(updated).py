def print_box(width, height, border_mark="#", inner_mark=" "):
    """
    Print box with patterns
    :param width: width of box
    :param height: height of box
    :param border_mark: mark for the outside
    :param inner_mark: mark for the inside
    :return: box
    """
    i = 0
    for i in range(0, int(height)):
        if i == 0 or i == int(height) - 1:
            print(border_mark * int(width))
        else:
            print(border_mark + inner_mark*(int(width-2))+border_mark)

    print()
def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)

if __name__ == "__main__":
    main()
