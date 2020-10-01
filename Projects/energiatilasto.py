"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name:       Hang Nguyen
Email:      hang.t.nguyen@tuni.fi
Student Id: K429778

A program to output a logarithmic histogram
of energy consumption measurements.
"""

def main():
    print("Enter energy consumption data.")
    print("End by entering an empty line.")
    print()

    user_list = []
    while True:
        try:
            user_input = int(input("Enter energy consumption (kWh): "))
            if user_input < 0:
                print("You entered: ", user_input, ". Enter non-negative numbers only!", sep="")
            else:
                user_list.append(user_input)
        except ValueError:
            break

    if len(user_list) == 0:
        print("Nothing to print. Done.")
    else:
        print_histogram(user_list)

# I chose class_number starting from 1 instead of 0, that's why I have to deduce 1 as can be
# seen from the function class_minimum_value below
def class_minimum_value(class_number):
    """
    Find the minimum value of a class number
    :param class_number: a random class number
    :return: the minimum value of that class number
    """
    # the if/else was used as if following the function (10 ** (class_number - 1)), the smallest
    # value of class number 1 would be 1 instead of 0
    if class_number == 1:
        return 0
    else:
        return (10 ** (class_number - 1))

def class_maximum_value(class_number):
    """
    Find the maximum value of a class number
    :param class_number: a random number
    :return: the maximum value of that class number
    """
    return (10 ** class_number - 1)

def find_largest_class_num(list):
    """
    Find length of digits of the biggest value in a list
    :param list: a random list
    :return: the length of digits of the biggest value in that list (e.g the biggest value is 234 then the fucntion returns value 3)
    """
    return len(str(max(list)))

def find_frequency_each_class(class_number, list):
    """
    Find the frequency of values in a list in each class class_number (in given range for each class number)
    :param class_number: a random class number
    :param list: a random list
    :return: the count of appearance of values in list (an integer)
    """
    count =0
    min_val = class_minimum_value(class_number)
    max_val = class_maximum_value(class_number)
    for val in list:
        if min_val <= val <= max_val:
            count += 1
    return count


def print_single_histogram_line(class_number, count, largest_class_number):
    """
    Print a single line of the histogram
    :param class_number: a random class number
    :param count: total amounts of value in the given list that in range of the above mentioned class number
    :param largest_class_number: the biggest class number of the given list
    :return: a single formatted line of the histogram
    """
    min_value = class_minimum_value(class_number)
    max_value = class_maximum_value(class_number)
    range_string = f"{min_value}-{max_value}"
    largest_width = 2 * largest_class_number + 1
    print(f"{range_string:>{largest_width}}: {'*' * count}")

def print_histogram(list):
    """
    Print the histogram from a list
    :param list: a random list
    :return: print the whole histogram
    """
    largest_class_num = find_largest_class_num(list)
    class_num = 1
    for class_num in range (1, largest_class_num+1):
        count = find_frequency_each_class(class_num, list)
        print_single_histogram_line(class_num, count, largest_class_num)

if __name__ == "__main__":
    main()
