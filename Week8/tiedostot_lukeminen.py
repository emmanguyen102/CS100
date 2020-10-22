def main():
    filename = input("Enter the name of the file: ")
    try:
        file = open(filename, mode ="r")

    except OSError:
        print(f"Error: opening the file '{filename}' failed!")
        return

    a = 0
    for file_line in file:
        file_line = file_line.rstrip()
        print(str(a + 1)+' '+file_line)
        a = a + 1

    file.close()

if __name__ == "__main__":
    main()