"""
COMP.CS.100 Ohjelmointi 1

Student: Hang Nguyen
ID: K29778
Email: hang.t.nguyen@tuni.fi

The function creates a dictionary for each of the CSV-file lines.
The information can be accessed from this dict by the title of the CSV-file column.
The function fill store these dicts in another dict where you can access them
by the key presented in the first column of the line.

"""

def read_file(filename):
    """
    The function reads a chosen file and put the info into a nested
    dictionary (dict in dict) and return this dictionary.

    :param filename: str, a chosen string
    :return: dict, a dictionary containing info from each line of CSV file

    """
    f = open(filename, mode ='r+')
    rows = f.readlines()[1:]

    try:
        contacts = {}

        for line in rows:
            line = line.rstrip().split(";")
            if line[-1] == "":
                line.pop(-1)

            key = line[0]
            contacts[key] = {}
            contacts[key]["name"] = line[1]
            contacts[key]["phone"] = line[2]
            contacts[key]["email"] = line[3]

            if len(line) == 5:
                contacts[key]["skype"] = line[4]

        f.close()
        return(contacts)

    except ValueError:
        print("Error: rows were not in the right format.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None

