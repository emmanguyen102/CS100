def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    :param: string, a chosen file
    :return: a dictionary containing series name as key and a list of genres as value
    """

    program = {}

    try:
        file = open(filename, mode="r")

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            program[name]= genres

        file.close()
        return program

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    unique_genres = set()

    for series in genre_data:
        for genre in genre_data[series]:
            unique_genres.add(genre)

    print("Available genres are:", ", ".join(sorted(unique_genres)))

    new_dict = {}

    for series in genre_data:
        for genre in genre_data[series]:
            if genre not in new_dict:
                new_dict[genre] = list()
                new_dict[genre].append(series)
            else:
                new_dict[genre].append(series)


    while True:

        genre = input("> ")

        if genre == "exit":
            return

        if genre in new_dict:
            for series in sorted(new_dict[genre]):
                print(series)
        else:
            pass


if __name__ == "__main__":
    main()
