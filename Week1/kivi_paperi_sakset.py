player_1 = str(input("Player 1, enter your choice (R/P/S): "))
player_2 = str(input("Player 2, enter your choice (R/P/S): "))
def main():
    if ((player_1 == "R" and player_2 == "R") or
        (player_1 == "P" and player_2 == "P") or
        (player_1 == "S" and player_2 == "S")):
        print("It's a tie!")
    elif((player_1 == "R" and player_2 == "S") or
        (player_1 == "P" and player_2 == "R") or
        (player_1 == "S" and player_2 == "P")):
        print("Player 1 won!")
    elif((player_1 == "R" and player_2 == "P") or
        (player_1 == "P" and player_2 == "S") or
        (player_1 == "S" and player_2 == "R")):
        print("Player 2 won!")
    return

main()