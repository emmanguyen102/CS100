"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Project: accesscontrol, program template
"""

DOORCODES = {'TC114': ['TIE'], 'TC203': ['TIE'], 'TC210': ['TIE', 'TST'],
             'TD201': ['TST'], 'TE111': [], 'TE113': [], 'TE115': [],
             'TE117': [], 'TE102': ['TIE'], 'TD203': ['TST'], 'TA666': ['X'],
             'TC103': ['TIE', 'OPET', 'SGN'], 'TC205': ['TIE', 'OPET', 'ELT'],
             'TB109': ['OPET', 'TST'], 'TB111': ['OPET', 'TST'],
             'TB103': ['OPET'], 'TB104': ['OPET'], 'TB205': ['G'],
             'SM111': [], 'SM112': [], 'SM113': [], 'SM114': [],
             'S1': ['OPET'], 'S2': ['OPET'], 'S3': ['OPET'], 'S4': ['OPET'],
             'K1705': ['OPET'], 'SB100': ['G'], 'SB202': ['G'],
             'SM220': ['ELT'], 'SM221': ['ELT'], 'SM222': ['ELT'],
             'secret_corridor_from_building_T_to_building_F': ['X', 'Y', 'Z'],
             'TA': ['G'], 'TB': ['G'], 'SA': ['G'], 'KA': ['G']}

class Accesscard:
    """
    This class models an access card which can be used to check
    whether a card should open a particular door or not.
    """

    def __init__(self, id, name):
        """
        Constructor, creates a new object that has no access rights.

        :param id: str, card holders personal id
        :param name: str, card holders name
        """
        self.__id = id
        self.__name = name
        self.__access = str()


    def info(self):
        """
        The method has no return value. It prints the information related to
        the access card in the format:
        id, name, access: a1,a2,...,aN
        """
        print(f"{self.__id}, {self.__name}, access: {self.__access}")


    def get_name(self):
        """
        :return: Returns the name of the accesscard holder.
        """
        return self.__name


    def get_id(self):
        """
        :return: Returns the id of the Accesscard holder
        """
        return self.__id


    def get_access(self):
        """
        :return: Returns the access right of the Accesscard holder
        """
        return self.__access


    def add_access(self, new_access_code):
        """
        The method adds a new accesscode into the accesscard according to the
        rules defined in the task description.

        :param new_access_code: str, the accesscode to be added in the card.
        """
        if len(self.__access) == 0:
            self.__access += new_access_code
        else:
            self.__access += ', ' + new_access_code


    def check_if_room_in_area(self, code_check):
        """
        This method check whether a room belongs to an area in
        the code check.
        :param code_check: list, a list contains a series of code
        to be checked
        :return new_var: list, a list of unnecessary variables
        """
        new_var = list()

        for code in code_check:
            if code in DOORCODES:
                areas = DOORCODES[code]
                for area in areas:
                    if area in code_check:
                        new_var.append(code)

        return new_var


    def check_access(self, door):
        """
        Checks if the accesscard allows access to a certain door.

        :param door: str, the doorcode of the door that is being accessed.
        :return: True: The door opens for this accesscard.
                 False: The door does not open for this accesscard.
        """
        access_areas = self.__access.split(", ")
        if door in access_areas:
            return True

        for area in DOORCODES[door]:
            if area in access_areas:
                return True

        return False


    def sort_access(self):
        """
        This method will sort the access code from the Accesscard object
        """
        access_area = self.__access.split(", ")
        separator = ", ".join(sorted(access_area))
        self.__access = separator


    def remove_access(self, access):
        """
        This method will remove the access code
        :param access: str, accesscode needed to be removed
        """
        access_area = self.__access.split(", ")

        while access in access_area:
            access_area.remove(access)

        separator = ", ".join(sorted(access_area))
        self.__access = separator


    def merge(self, card):
        """
        Merges the accesscodes from another accesscard to this accesscard.

        :param card: Accesscard, the accesscard whose access rights are added to this card.
        """
        self.__access += card.__access


    def __lt__(self, other):
        """
        This method will compare variable .__id from 1 object to another
        (larger than)
        Use for list command below, for method 'sorted'
        """
        return self.__id < other.__id


    def __eq__(self, other):
        """
        This method will compare variable .__id from 1 object to another
        (equal to)
        Use for list command below, for method 'sorted'
        """
        return self.__id == other.__id


def main():

    input_file = "accessinfo.txt"
    file = open(input_file, mode="r")
    content = file.readlines()

    # initiate data structures
    card_list = list()
    id_list = list()
    unique_area = set()

    for room in DOORCODES:
        areas = DOORCODES[room]
        for area in areas:
            unique_area.add(area)

    # add Accesscard objects into card_list
    for row in content:
        row = row.rstrip().split(";")
        print(row)
        card_holder = Accesscard(row[0], row[1])

        # rearrange the access right of Accesscard object
        access_right = row[-1].split(",")
        separator = ", ".join(sorted(access_right))
        card_holder.add_access(separator)
        unnecessary = card_holder.check_if_room_in_area(sorted(access_right))
        for item in unnecessary:
            card_holder.remove_access(item)

        # append to list
        card_list.append(card_holder)


    for item in sorted(card_list):
        ids = item.get_id()
        id_list.append(ids)


    while True:
        line = input("command> ")

        if line == "":
            break

        strings = line.split()
        command = strings[0]

        if command == "list" and len(strings) == 1:
            for item in sorted(card_list):
                item.info()


        elif command == "info" and len(strings) == 2:
            card_id = strings[1]

            if card_id not in id_list:
                print("Error: unknown id.")
            else:
                # get the index to iterate over sorted list
                right_index = id_list.index(card_id)
                sorted(card_list)[right_index].info()


        elif command == "access" and len(strings) == 3:
            card_id = strings[1]
            door_id = strings[2]

            if card_id not in id_list:
                print("Error: unknown id.")
            elif door_id not in DOORCODES:
                print("Error: unknown doorcode.")
            else:
                right_index = id_list.index(card_id)
                check_access = sorted(card_list)[right_index]\
                    .check_access(door_id)
                name = sorted(card_list)[right_index].get_name()

                if check_access == True:
                    print(f"Card {card_id} ( {name} ) "
                          f"has access to door {door_id}")
                else:
                    print(f"Card {card_id} ( {name} ) "
                          f"has no access to door {door_id}")


        elif command == "add" and len(strings) == 3:
            card_id = strings[1]
            access_code = strings[2]

            if card_id not in id_list:
                print("Error: unknown id.")

            # Since it is hard to read when combining conditioning of
            # both area code and room code, I split them into 2 different
            # elif conditioning, easier to read and understand!
            elif access_code in DOORCODES:
                right_index = id_list.index(card_id)
                access = sorted(card_list)[right_index].get_access()
                access_splt = access.split(", ")

                # check if the added room is already there in the access right
                # if it's already there, not adding anything to access right
                if access_code not in access_splt:
                    after_add = sorted(card_list)[right_index]\
                        .add_access(access_code)
                    after_sort = sorted(card_list)[right_index]\
                        .sort_access()

                    areas = DOORCODES[access_code]
                    for area in areas:
                        if area in access_splt:
                            removed_room = sorted(card_list)[right_index]\
                                .remove_access(access_code)

            elif access_code in unique_area:
                right_index = id_list.index(card_id)
                access = sorted(card_list)[right_index].get_access()
                access_splt = access.split(", ")

                if access_code not in access_splt:
                    for area in access_splt:
                        # get the room
                        if area not in unique_area:
                            area_list = DOORCODES[area]
                            if access_code in area_list:
                                removed_room = sorted(card_list)[right_index]\
                                    .remove_access(area)

                    after_add = sorted(card_list)[right_index]\
                        .add_access(access_code)
                    after_sort = sorted(card_list)[right_index]\
                        .sort_access()

            else:
                print("Error: unknown accesscode.")


        elif command == "merge" and len(strings) == 3:
            card_id_to = strings[1]
            card_id_from = strings[2]

            if card_id_to not in id_list or card_id_from not in id_list:
                print("Error: unknown id.")
            else:
                card_id_to_index = id_list.index(card_id_to)
                card_id_from_index = id_list.index(card_id_from)

                access_to = sorted(card_list)[card_id_to_index].get_access()
                access_to_list = access_to.split(", ")
                access_from = sorted(card_list)[card_id_from_index].get_access()
                access_from_list = access_from.split(", ")

                for access in access_to_list:
                    if access in access_from_list:
                        sorted(card_list)[card_id_to_index].remove_access(access)

                after_add = sorted(card_list)[card_id_to_index]\
                    .add_access(access_from)
                after_access_code = sorted(card_list)[card_id_to_index].get_access()
                after_check = sorted(card_list)[card_id_to_index] \
                    .check_if_room_in_area(after_access_code)

                for item in after_check:
                    sorted(card_list)[card_id_to_index].remove_access(item)

                after_sort = sorted(card_list)[card_id_to_index] \
                    .sort_access()


        elif command == "quit":
            print("Bye!")
            return
        else:
            print("Error: unknown command.")

    file.close()


if __name__ == "__main__":
    main()
