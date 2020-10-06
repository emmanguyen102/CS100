purchase = int(input("Purchase price: "))
paid = int(input("Paid amount of money: "))

def main():
    c = int(paid - purchase)
    if (c==0)or(c<0):
        print("No change")
    else:
        print("Offer change:")
        if c//10 != 0:
            print(c//10, "ten-euro notes")
            c = c %10
        if c //5 != 0:
            print(c//5, "five-euro notes")
            c = c% 5
        if c//2 != 0:
            print(c//2, "two-euro coins")
            c = c %2
        if c//1 != 0:
            print(c//1, "one-euro coins")
    return

if __name__ == "__main__":
    main()