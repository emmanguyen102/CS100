def encrypt(char):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param char: str, a character to be encrypted
    :return: str, <char> parameter encrypted using ROT13
    """

    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                     "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]
    new_char = ""
    if char.lower() in regular_chars:
        char_index = regular_chars.index(char.lower())
        new_char = encrypted_chars[char_index]
        if char.isupper():
            return (new_char.upper())
        else:
            return (new_char)
    else:
        return(char)

def row_encryption(str):
    """
    Perform a ROT13 transformation for an entire string

    :param str: str, a random string
    :return: str, <str> parameter encrypted using ROT13
    """
    new_str = ""
    for char in str:
        new_char = encrypt(char)
        new_str += new_char
    return(new_str)

def read_message():
    """
    Read the input entered
    by the user, saves the rows in a list, and returns the list.

    :return: list, the list contains user input
    """
    user_list = []
    while True:
        try:
            user_input = str(input())
            if user_input == "":
                break
            else:
                user_list.append(user_input)
        except ValueError:
            break
    return user_list

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("ROT13:")
    for element in msg:
        element = row_encryption(element)
        print(element)

if __name__ == "__main__":
    main()
