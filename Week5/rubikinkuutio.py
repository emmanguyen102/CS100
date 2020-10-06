def main():
    answers=[]
    for i in range(0,5):
        time_played = float(input(("Enter the time for performance " + str(i+1) + ": ")))
        answers.append(time_played)
    max_list = max(answers)
    min_list = min(answers)
    avg = (sum(answers) - max_list - min_list)/3
    print("The official competition score is ", "{0:.2f}".format(avg), " seconds.", sep="")

if __name__ == "__main__":
    main()