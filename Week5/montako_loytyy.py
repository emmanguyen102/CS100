def input_to_list(a):
    """
    Reads the numbers from the user and saves them in a list
    :param a: number of integers user needs to enter
    :return: that list
    """
    answers = []
    for i in range (0,a):
        num = int(input())
        answers.append(num)
    return answers

def main():
    answer = int(input("How many numbers do you want to process: "))
    print("Enter", answer, "numbers:")
    b = input_to_list(answer)
    search = int(input("Enter the number to be searched: "))
    if search in b:
        print(search, "shows up", b.count(search), "times among the numbers you have entered.")
    else:
        print(search, "is not among the numbers you have entered.")

if __name__ == "__main__":
    main()