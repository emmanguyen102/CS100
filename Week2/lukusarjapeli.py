def main():
    num = int(input("How many numbers would you like to have? "))
    for i in range (1, num+1):
        if (i % 3 == 0 and i % 7 != 0):
            print("zip")
        elif (i % 7 == 0 and i % 3 != 0):
            print("boing")
        elif (i % 3 == 0 and i % 7 == 0):
            print("zip boing")
        else:
            print(i)

if __name__ == "__main__":
    main()