"""
COMP.CS.100 Ohjelmointi 1: Johdatus ohjelmointiin
Student name: Hang Nguyen
Student ID: K429778

A program that helps you add up the scores that
various contestants have obtained in a game.

"""
def main():
    filename = input("Enter the name of the score file: ")

    try:
        file = open(filename, mode="r")

    except OSError:
        print("There was an error in reading the file.")
        return

    check = True
    scores = {}
    for file_line in file:
        file_line = file_line.rstrip()

        if " " not in file_line:
            check = False
            print("There was an erroneous line in the file:")
            b = file_line
            print(b)
            break

        else:
            file_line = file_line.split(" ")
            if file_line[0] not in scores:
                try:
                    file_line[1] = int(file_line[1])
                    scores[file_line[0]] = file_line[1]
                except ValueError:
                    check = False
                    print("There was an erroneous score in the file:")
                    c = file_line[1]
                    print(c)
                    break
            else:
                a = int(file_line[1])
                a += int(file_line[1])
                scores[file_line[0]] = str(a)

    if check:
        print("Contestant score:")
        for k, v in sorted(scores.items()):
            print(k + ' ' + v)

    file.close()
    return

if __name__ == "__main__":
    main()