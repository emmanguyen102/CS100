
class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    def __init__(self, name, price, percentage = 0):
        self.__name = name
        self.__price = price
        self.__percentage = percentage

    def printout(self):
        print(self.__name)
        print("  price:", "%.2f" % self.__price)
        print("  sale%:", "%.2f" % self.__percentage)

    def set_sale_percentage(self, percentage):
        self.__percentage = percentage

    def get_price(self):
        return(self.__price - self.__price * self.__percentage /100)

def main():

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print("Normal price:", "%.2f" % prod.get_price())

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
