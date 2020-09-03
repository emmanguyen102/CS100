def main():
    read_number = int(input("Choose a number: "))
    for i in range(1,52):
        mul = i * read_number
        print(i, "*", read_number, "=", read_number*i)
        if mul > 100:
            break

if __name__ == "__main__":
    main()