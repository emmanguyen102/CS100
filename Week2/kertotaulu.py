def main():
    read_number = int(input("Choose a number: "))
    for i in range(1,11):
        print(i, "*", read_number, "=", read_number*i)

if __name__ == "__main__":
    main()