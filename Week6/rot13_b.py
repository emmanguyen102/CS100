def read_message():
    """
    Read the input entered
    by the user, saves the rows in a list, and returns the list.

    :return: list, the list contains user input
    """
    user_list = []
    while True:
        try:
            user_input = str(input())
            if user_input == "":
                break
            else:
                user_list.append(user_input)
        except ValueError:
            break
    return user_list

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    for word in msg:
        word = word.upper()
        print(word)

if __name__ == "__main__":
    main()
