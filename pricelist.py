"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: K429778
Name: Hang Nguyen
Email: hang.t.nguyen@tuni.fi

Modify main function in the code template
in a way that the program worrks as folloign
examples
"""

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
                print("The price of milk is", "{:.2f}".format(PRICES[user_input.strip()]), "e")
            else:
                if user_input.strip() == "":
                    print("Bye!")
                    break
                else:
                    print("Error:", user_input.strip(), "is unknown.")
                    break
        except ValueError:
                print("Bye!")
                break



if __name__ == "__main__":
    main()
