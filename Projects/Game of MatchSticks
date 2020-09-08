def stick_left(sticks, player):
  while True:
    if player == 1:
      choice = int(input("Player 1 enter how many sticks to remove: "))
    else:
      choice = int(input("Player 2 enter how many sticks to remove: "))

    if (3 >= choice >= 1):
      if sticks > choice:
        print("There are", sticks-choice, "sticks left")
      else:
        print("Player", player, "lost the game!")
      break
    else:
      print("Must remove between 1-3 sticks!")
      continue
  return sticks - choice


def main():
  STICKS = 21;

  print("Game of sticks\n");

  while STICKS > 0:
      STICKS = stick_left(STICKS, 1)
      if STICKS > 0:
        STICKS = stick_left(STICKS, 2)

if __name__ == "__main__":
    main()
