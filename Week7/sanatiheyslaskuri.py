def main():
    print("Enter rows of text for word counting. Empty row to quit.")
    words_list = []
    while True:
        user_input = str(input())
        if user_input.strip() == "":
            break
        words_list += user_input.lower().split(" ")
    words = {}
    for word in words_list:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    for element in sorted(words):
        print(element, " : ", words[element], " times", sep ="")

if __name__ == "__main__":
    main()