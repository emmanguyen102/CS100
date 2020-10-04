"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name:       Hang Nguyen
Email:      hang.t.nguyen@tuni.fi
Student Id: K429778

A function return a string written with each word
starting in upper case but rest in lower case
"""

def capitalize_initial_letters(str):
    """
    return the string in given format: Upper case for first letter,
    lower case for the rest of the string
    :param str: a random string
    :return: formatted string
    """
    str = str.title()
    return str
