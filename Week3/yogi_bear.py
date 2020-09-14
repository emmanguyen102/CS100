"""
COMP.CS.100 Programming 1
Hang Nguyen, hang.t.nguyen@tuni.fi, student id K429778
The song "Yogi_bear"
"""
def repeat_name(name, reps):
    """
    create a function for repeated line in 3 verses
    :param name: the name of bear.
    :param reps: the repeition of line.
    """
    line = name + ', ' + name + ' Bear' + '\n'
    complete_line=line*int(reps)
    return(print(complete_line, end=''))

def verse(sentence, name):
   """
   :param sentence:
   :param name: name of bear
   """
   print(sentence + '\n' + name + ', ' + name + '\n' + sentence)
   repeat_name(name, 3)
   print(sentence)
   repeat_name(name, 1)
   print()

def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")

if __name__ == "__main__":
    main()
