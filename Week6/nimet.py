def reverse_name(str):
    """
    Return a string that does not have a comma in between names
    and in order: First_name Last_name
    :param str: a random string
    :return: a new formatted string without comma and in revers order
    """
    if ',' not in str:
        return(str)
    else:
        str=str.split(",")
        if str[0] == "":
            return str[1]
        elif str[1] == "":
            return str[0]
        elif str[0] == "" and str[1] == "":
            return ""
        else:
            str = str[1].strip() + " " + str[0].strip()
            return(str)


