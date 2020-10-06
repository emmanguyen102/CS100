result = int(input("How do you feel? (1-10) "))
def main():
    if result == 1:
        print("A suitable smiley would be :'(")
    elif result == 10:
        print("A suitable smiley would be :-D")
    elif result > 7 and result < 10:
        print("A suitable smiley would be :-)")
    elif result < 4 and result > 1:
        print("A suitable smiley would be :-(")
    elif result > 10 or result < 1:
        print("Bad input!")
    else:
        print("A suitable smiley would be :-|")
    return

main()
