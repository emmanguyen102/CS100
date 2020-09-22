def main():
    answers=[]
    print("Give 5 numbers:")
    num_1 = int(input("Next number: "))
    answers.append(num_1)
    num_2 = int(input("Next number: "))
    answers.append(num_2)
    num_3 = int(input("Next number: "))
    answers.append(num_3)
    num_4 = int(input("Next number: "))
    answers.append(num_4)
    num_5 = int(input("Next number: "))
    answers.append(num_5)
    print("The numbers you entered that were greater than zero were: ")
    for i in answers:
        if i >=0:
            print(i)
if __name__ == "__main__":
    main()