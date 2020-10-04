"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name:       Hang Nguyen
Email:      hang.t.nguyen@tuni.fi
Student Id: K429778

Implement function longest_substring_in_order, which takes
a string as its parameters´and searches for the longest substring
with its characters in alphabetic order and then returns it
"""

def longest_substring_in_order(str):
    """
    Search for the longest substring in alphabetical order

    :param str: str, a random string
    :return: str, longest substring with its characters in alphabetic order
    """

    if len(str) == 1:
        longest = str
    elif len(str) == 0:
        longest = ""
    else:
        max_str = ""
        longest = ""
        for i in range(len(str)):
            max_str += str[i]
            if len(max_str) > len(longest):
                longest = max_str
            if i > len(str) - 2:
                break
            if str[i] > str[i + 1]:
                max_str = ""

    return longest







