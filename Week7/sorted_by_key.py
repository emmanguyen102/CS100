PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    new_dict={}
    for value in PRICES:
        new_dict[PRICES[value]] = value
    for price in sorted(new_dict):
        print(new_dict[price], '{:.2f}'.format(price))

if __name__ == "__main__":
    main()
