def main():
    nterms = int(input("How many Fibonacci numbers do you want? "))
    n1, n2 = 1, 1;
    count= 0;
    while count < nterms:
        print(1+count, end="")
        print(".", n1)
        nth = n1 +n2
        n1=n2
        n2=nth
        count +=1

if __name__ == "__main__":
    main()