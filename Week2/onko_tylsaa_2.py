def main():
    word_input = True
    while word_input:
        word = input("Answer Y or N: ")
        if word.lower() == "n":
            print("You answered", word)
            word_input = False
        elif word.lower() == "y":
            print("You answered", word)
            word_input = False
        while word.lower() != "n" and word.lower() != "y":
            print("Incorrect entry.")
            word = input("Please retry: ")
            if word.lower() == "n":
                print("You answered", word)
                word_input = False
            elif word.lower() == "y":
                print("You answered", word)
                word_input = False


if __name__ == "__main__":
    main()
