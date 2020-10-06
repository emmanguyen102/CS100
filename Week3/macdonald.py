def verse_1():
    """print repeated phrases with capital MACDONALD"""
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")

def verse_2():
    """print repeated phrases with lower case MacDonald"""
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")

def print_verse(animal, sound):
    """print repeated phrases with substitued animals and sounds"""
    verse_1()
    print("And on his farm he had a ", animal, "\nE-I-E-I-O", sep='')
    print("With a", sound, sound, "here")
    print("And a", sound, sound, "there")
    print("Here a ", sound, ", there a ", sound, sep='')
    print("Everywhere a", sound, sound)
    verse_2()
    print()

def main():
    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")

if __name__ == "__main__":
    main()
