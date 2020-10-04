ef encrypt(char):
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



