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
