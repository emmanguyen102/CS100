def main():
    answers=[]
    print("Give 5 numbers:")
    for i in range (0,5):
        num= int(input("Next number: "))
        answers.append(num)
    print("The numbers you entered, in reverse order: ")
    length = len(answers)
    for i in range(0, length):
        print(answers[length-i-1])

if __name__ == "__main__":
    main()