PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}

def main():
    while True:
        try:
            user_input = str(input("Enter product name: "))
            if user_input.strip() in PRICES:
                print("The price of", user_input.strip(), "is", "{:.2f}".format(PRICES[user_input.strip()]), "e")
            else:
                if user_input.strip() == "":
                    print("Bye!")
                    break
                else:
                    print("Error:", user_input.strip(), "is unknown.")
        except ValueError:
                print("Bye!")
                break



if __name__ == "__main__":
    main()