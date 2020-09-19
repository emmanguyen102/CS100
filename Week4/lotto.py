"""
Ohjelmointi 1 / Programming 1
Hang Nguyen, hang.t.nguyen@tuni.fi, student id K429778
Lottery probabilities
"""
def subfactorial(b,a):
    """
    Defines the probability function
    :param b: drawn balls
    :param a: total balls
    :return: the probability of chosing b from a
    """
    c = a-b
    test = 1
    for i in range(b+1, a+1):
      test *= i/c
      c=c-1
    return int(test)

def prob(b, a):
    """
    Optimise the function subfactorial
    :param b: drawn balls
    :param a: total balls
    :return: the probability of chosing b from a
    """
    if(a-b)>b:
        return subfactorial(a-b, a)
    else:
        return subfactorial(b,a)

def main():
    total = int(input("Enter the total number of lottery balls: "))
    drawn = int(input("Enter the number of the drawn balls: "))
    if total <= 0:
        print("The number of balls must be a positive number.")
    elif (drawn > total and total > 0):
        print("At most the total number of balls can be drawn.")
    else:
        print("The probability of guessing all ", drawn, " balls correctly is 1/", prob(drawn, total), sep="")

if __name__ == "__main__":
    main()