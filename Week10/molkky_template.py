class Player:
    """
    This class models a player with his/her name
    """
    def __init__(self, name, point = 0, round =0, larger_0 = 0):
        self.__name = name
        self.__point = point
        self.__round = round
        self.__larger_0 = larger_0

    def get_name(self):
        return(self.__name)

    def get_points(self):
        return(self.__point)

    def has_won(self):
        if self.__point == 50:
            return True

    def add_points(self, point):
        self.__point += point
        self.__round += 1
        if point > 0:
            self.__larger_0 += 1
        if self.__point > 50:
            self.__point = 25
            print(self.__name, "gets penalty points!")
        elif self.__point >= 40 and self.__point <= 49:
            print(self.__name, " needs only ", 50 - self.__point,
                  " points. It's better to avoid knocking down the pins "
                  "with higher points.", sep= "")
        return(self.__point)

    def calculate_average_score(self):
        return(self.__point/self.__round)

    def success_percentage(self):
        if self.__larger_0 == 0:
            percent = 0
        else:
            percent = self.__larger_0/self.__round*100
        return "{:.1f}".format(percent)

def main():

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)
        if pts > in_turn.calculate_average_score() \
                and in_turn.get_points() != 25:
            print("Cheers ", in_turn.get_name(), "!", sep ="")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(),
              "p, hit percentage " + player1.success_percentage())
        print(player2.get_name() + ":", player2.get_points(),
              "p, hit percentage " + player2.success_percentage())
        print("")

        throw += 1


if __name__ == "__main__":
    main()
