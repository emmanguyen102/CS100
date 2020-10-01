"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name:       Hang Nguyen
Email:      hang.t.nguyen@tuni.fi
Student Id: K429778

A program that asks a user for a word and tells
how many vowels and consonants the word contains
"""

def main():
    str_input = str(input("Enter a word: "))
    vowel_count=0
    consonant_count=0
    for i in range(len(str_input)):
        if str_input[i] in ['a', 'e', 'i', 'o', 'u']:
            vowel_count +=1
        else:
            consonant_count += 1
    print("The word", str_input, "contains", vowel_count, "vowels and", consonant_count, "consonants")

if __name__ == "__main__":
    main()