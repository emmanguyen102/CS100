def main():
    filename = input("Enter the name of the file: ")

    try:
        # To be able to write into file the value of the
        # mode parameter for open must be "w" (write).
        save_file = open(filename, mode="w")

    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return

    print("Enter rows of text. Quit by entering an empty row.")

    a=0
    while True:
        text_line = input()
        if text_line == "":
            break
        print(str(a+1)+' '+text_line, file=save_file)
        a += 1

    save_file.close()

    print(f"File {filename} has been written.")


if __name__ == "__main__":
    main()
