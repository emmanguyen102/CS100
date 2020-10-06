"""
COMP.CS.100 Programming 1
Student ID: K429778
Name: Hang Nguyen
Email: hang.t.nguyen@tuni.fi

A program to implement a simple dictionary to help a tourist while abroad
"""

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            word = str(input("Enter the word to be translated: "))
            if word in english_spanish:
                print(word, "in Spanish is", english_spanish[word])
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            english = str(input("Give the word to be added in English: "))
            spanish = str(input("Give the word to be added in Spanish: "))
            english_spanish[english] = spanish

        elif command == "R":
            word_to_be_removed = str(input("Give the word to be removed: "))
            if word_to_be_removed in english_spanish:
                del english_spanish[word_to_be_removed]
            else:
                print("The word", word_to_be_removed, "could not be found from the dictionary.")

        elif command == "P":
            for word in sorted(english_spanish):
                print(word, english_spanish[word])

        elif command == "T":
            text = str(input("Enter the text to be translated into Spanish: "))
            print("The text, translated by the dictionary:")
            words = text.split(" ")
            translated_text = ""
            for word in words:
                if word in english_spanish:
                    translated_word = english_spanish[word]
                else:
                    translated_word = word
                translated_text += translated_word + " "
            print(translated_text)


        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
