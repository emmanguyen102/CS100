def main():
    # The flag variable is initialized to True to start the loop.
    read_words = True

    # Read words while the value of the flag variable is True.
    while read_words:
        word = input("Bored? (y/n) ")
        # Flip the flag value to end the loop.
        if word == "y":
            read_words = False
            print("Well, let's stop this, then.")

if __name__ == "__main__":
    main()