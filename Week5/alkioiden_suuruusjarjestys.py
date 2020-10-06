def is_the_list_in_order(list):
    """
    Check whether the numbers contained by the list are in an ascending order
    :param list: a list as a parameter
    :return: Boolean values
    """
    if len(list) == 0 or len(list) == 1:
        return True
    else:
        flag=0
        i = 1
        while i < len(list):
            if(list[i] < list[i-1]):
                flag=1
            i += 1

        if (not flag):
            return True
        else:
            return False

