def main():
    first_month = 1
    last_month = 12
    while first_month <= last_month:
        if first_month in (1,3,5,7,8,10,12):
            for i in range(1, 32):
                print(i, ".", end="", sep="")
                print(first_month, ".", sep="")
        if first_month == 2:
            for i in range(1,29):
                print(i, ".", end="", sep="")
                print(first_month, ".", sep="")
        if first_month in (4,6,9,11):
            for i in range(1, 31):
                print(i, ".", end="", sep="")
                print(first_month, ".", sep="")
        first_month += 1

if __name__ == "__main__":
    main()