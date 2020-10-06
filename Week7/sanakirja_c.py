def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    while True:
        print("Dictionary contents:")
        seperator = ", "
        print(seperator.join(sorted(english_spanish)))
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        while command == "W":
            word = str(input("Enter the word to be translated: "))
            if word in english_spanish:
                print(word, "in Spanish is", english_spanish[word])
                command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")
                if command == "R":
                    word_to_be_removed = str(input("Give the word to be removed: "))
                    if word_to_be_removed in english_spanish:
                        del english_spanish[word_to_be_removed]
                        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")
                    else:
                        print("The word", word_to_be_removed, "could not be found from the dictionary.")
            else:
                print("The word", word, "could not be found from the dictionary.")

        if command == "A":
            english = str(input("Give the word to be added in English: "))
            spanish = str(input("Give the word to be added in Spanish: "))
            english_spanish[english] = spanish

        elif command == "P":
            print()
            print("English-Spanish")
            for word in sorted(english_spanish):
                print(word, english_spanish[word])
            print()
            print("Spanish-English")
            new_dict = {}
            for word in english_spanish:
                new_dict[english_spanish[word]] = word
            for new_word in sorted(new_dict):
                print(new_word, new_dict[new_word])
            print()
            command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")
            if command == "Q":
                print("Adios!")
                return

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

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()
