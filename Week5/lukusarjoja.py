def is_even_num_ascending(l):
    """
    print the even numbers in ascending order
    :param l: the biggest number
    :return: list of number in ascending order
    """
    for i in range (0, l, 2):
        print(i)
    return i
def is_even_num_descending(l):
    """
    print the event numbers in descending order
    :param l: the biggest number
    :return: in descending order
    """
    for i in range (l, -1, -2):
        print(i)
    return i

def main():
    is_even_num_ascending(101)
    is_even_num_descending(100)


if __name__ == "__main__":
    main()
