def are_all_members_same(list):
    """
    Check whether all the members contained by the list are the same.
    :param list:
    :return: Boolean value
    """
    if len(list) == 0:
        return True
    else:
        first = list[0]
        for element in list:
            if element != first:
                return False
                break
        return True




