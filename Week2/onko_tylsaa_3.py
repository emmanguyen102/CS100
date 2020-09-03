def main():
    word_input = True
    while word_input:
        word = input("Bored? (y/n) ")
        if word.lower() == "n":
            continue
        if word.lower() == "y":
            print("Well, let's stop this, then.")
            word_input = False
        while word.lower() != "y":
            print("Incorrect entry.")
            word = input("Please retry: ")
            if word.lower() == "y":
                print("Well, let's stop this, then.")
                word_input = False
            elif word.lower() == "n":
                break
                word = input("Bored? (y/n) ")
                word_input = True


if __name__ == "__main__":
    main()