def create_an_acronym(name):
    """
    return an acronym from a name, taking a name as a parameter
    :param name: a random string
    :return: formatted string (upper case of each first
    character of each word in name)
    """
    name =name.split(" ")
    i = 0
    new_name=""
    for i in range(0, len(name)):
        first_char = name[i][0].upper()
        new_name += first_char
    return(new_name)