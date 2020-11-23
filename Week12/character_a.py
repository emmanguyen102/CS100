class Character:
    """
    This class models a Character with his/her items
    """
    
    def __init__(self, character):
        """
        Constructor, creates a new object.

        :param character: str, a chosen character

        """
        self.__character = character
        self.__item = {}


    def give_item(self, item):
        """
        This method will add items to character

        :param item: str, an item
        
        """
        if item not in self.__item:
            self.__item[item] = 1
        else:
            self.__item[item] += 1


    def remove_item(self, item):
        """
        This method removes the items of the character
        :param item: str, the item to be removed

        """
        self.__item[item] -= 1


    def has_item(self, item):
        """
        The method checks if the item in the list items of the
        character
        :param item: str, an item'
        
        """
        if item in self.__item and self.__item[item] != 0:
            return True

        return False


    def printout(self):
        """
        The method prints out lines according to the
        requirement
        
        """
        print(f"Name: {self.__character}")

        if len(self.__item) == 0:
            print("  --nothing--  ")

        for item in sorted(self.__item):
            if self.__item[item] != 0:
                print(f"  {self.__item[item]} {item}")


    def get_name(self):
        """
        This method will get the name of character
        :return: the character
        
        """
        return self.__character


    def how_many(self, item):
        """
        This method will count the amount of a specific item of the
        character

        :param item: str, a chosen item
        :return: the amount of a chosen item
        
        """
        if item not in self.__item:
            return 0
        else:
            return self.__item[item]


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
