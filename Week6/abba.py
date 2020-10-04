def count_abbas(str):
    """
    Count the occurence of string "abba" in <str> parameter

    :param str: str, a random string
    :return: the count of occurence of string "abba" in given string
    """
    i = 0
    count = 0
    for i in range(0, len(str)):
        if str.startswith("abba", i):
            count += 1
    return count



