"""
The program is operated based on the Hangman game with a somewhat 'keyboard'
containing only capital English alphabets (26 letters in bold).
The user has to click the letter on the screen to guess the word.
The given word is "GANODERMA".
The user has 5 chances to guess again if he/she encounters a wrong guess.
If the user guesses the right letter, chances remaining as it is, not being deducted.
But if the user clicked the wrong letter, chances will be eliminated by 1.
A some sort of emotion pictures are also included in the interface, and the emotion
changes according to the chances left. Hand-made pictures is used for copy-right issues.
When chances = 0, a message box appears and tells the user that he/she fails
to guess the right answer. Meanwhile, if chance number is larger than 0, and
the user guesses the word correctly, a message also pops up and congratulates
the user. In both cases, after the message box appears, and the user closes it,
the main program also be deleted.
There are 2 special buttons for user to click: Close and Try again. Close button
is meant for user to exit program immediately, and Try again button let the user
reset the whole program and keep guessing.

"""

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()
        self.__mainwindow.title("Virtual keyboard")
        self.__mainwindow.config(bg="Moccasin")

        # insert picture after every time the user would choose a letter
        self.__chances = 5
        self.__images = ['1.jpg', '6.jpg', '2.jpg', '3.jpg', '5.jpg', '4.jpg']
        self.__img = Image.open(self.__images[5])
        self.__img = self.__img.resize((300,200), Image.ANTIALIAS)
        self.__img = ImageTk.PhotoImage(self.__img)
        self.__emotion = Label(self.__mainwindow, image=self.__img)

        ## Get the name of program
        self.__appName = Label(self.__mainwindow,
                               text= "Are your ready to be hung?",
                               font=("Courier", 18, "bold"),
                               bg="Moccasin", fg="FireBrick")

        ## define the sequence of words (9 characters)
        self.__bt01 = Button(self.__mainwindow, text=" ", bg="PeachPuff",
                       fg="Black", width=3, height=1, font=('Helvetica', '20'))

        self.__bt02 = Button(self.__mainwindow, text=" ", bg="PeachPuff",
                       fg="Black", width=3, height=1, font=('Helvetica', '20'))

        self.__bt03 = Button(self.__mainwindow, text=" ", bg="PeachPuff",
                       fg="Black", width=3, height=1, font=('Helvetica', '20'))

        self.__bt04 = Button(self.__mainwindow, text=" ", bg="PeachPuff",
                      fg="Black", width=3, height=1, font=('Helvetica', '20'))

        self.__bt05 = Button(self.__mainwindow, text=" ", bg="PeachPuff",
                      fg="Black", width=3, height=1, font=('Helvetica', '20'))

        self.__bt06 = Button(self.__mainwindow, text=" ", bg="PeachPuff",
                      fg="Black", width=3, height=1, font=('Helvetica', '20'))

        self.__bt07 = Button(self.__mainwindow, text=" ", bg="PeachPuff",
                      fg="Black", width=3, height=1, font=('Helvetica', '20'))

        self.__bt08 = Button(self.__mainwindow, text=" ", bg="PeachPuff",
                      fg="Black", width=3, height=1, font=('Helvetica', '20'))

        self.__bt09 = Button(self.__mainwindow, text=" ", bg="PeachPuff",
                      fg="Black", width=3, height=1, font=('Helvetica', '20'))


        ## define the keyboards with each letter as a button (26 letters in capital)
        self.__btn1 = Button(self.__mainwindow, text="A", bg="MediumVioletRed",
                      fg="Black", width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: self.clicked("A"))

        self.__btn2 = Button(self.__mainwindow, text="B", bg="MediumVioletRed",
                      fg="Black", width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: self.clicked("B"))

        self.__btn3 = Button(self.__mainwindow, text="C", bg="MediumVioletRed",
                      fg="Black", width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: self.clicked("C"))

        self.__btn4 = Button(self.__mainwindow, text="D", bg="MediumVioletRed",
                      fg="Black",width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: self.clicked("D"))

        self.__btn5 = Button(self.__mainwindow, text="E", bg="MediumVioletRed",
                      fg="Black", width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: self.clicked("E"))

        self.__btn6 = Button(self.__mainwindow, text="F", bg="MediumVioletRed",
                      fg="Black", width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: self.clicked("F"))

        self.__btn7 = Button(self.__mainwindow, text="G", bg="MediumVioletRed",
                      fg="Black", width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: self.clicked("G"))

        self.__btn8 = Button(self.__mainwindow, text="H", bg="MediumVioletRed",
                      fg="Black", width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: self.clicked("H"))

        self.__btn9 = Button(self.__mainwindow, text="I", bg="MediumVioletRed",
                      fg="Black", width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: self.clicked("I"))

        self.__btn10 = Button(self.__mainwindow, text="J", bg="MediumVioletRed",
                       fg="Black", width=3, height=1, font=('Helvetica', '20'),
                       command=lambda: self.clicked("J"))

        self.__btn11 = Button(self.__mainwindow, text="K", bg="MediumVioletRed",
                       fg="Black", width=3, height=1, font=('Helvetica', '20'),
                       command=lambda: self.clicked("K"))

        self.__btn12 = Button(self.__mainwindow, text="L", bg="MediumVioletRed",
                       fg="Black", width=3, height=1, font=('Helvetica', '20'),
                       command=lambda: self.clicked("L"))

        self.__btn13 = Button(self.__mainwindow, text="M", bg="MediumVioletRed",
                       fg="Black", width=3, height=1, font=('Helvetica', '20'),
                       command=lambda: self.clicked("M"))

        self.__btn14 = Button(self.__mainwindow, text="N", bg="MediumVioletRed",
                       fg="Black", width=3, height=1, font=('Helvetica', '20'),
                       command=lambda: self.clicked("N"))

        self.__btn15 = Button(self.__mainwindow, text="O", bg="MediumVioletRed",
                       fg="Black", width=3, height=1, font=('Helvetica', '20'),
                       command=lambda: self.clicked("O"))

        self.__btn16 = Button(self.__mainwindow, text="P", bg="MediumVioletRed",
                       fg="Black", width=3, height=1, font=('Helvetica', '20'),
                       command=lambda: self.clicked("P"))

        self.__btn17 = Button(self.__mainwindow, text="Q", bg="MediumVioletRed",
                       fg="Black", width=3, height=1, font=('Helvetica', '20'),
                       command=lambda: self.clicked("Q"))

        self.__btn18 = Button(self.__mainwindow, text="R", bg="MediumVioletRed",
                       fg="Black", width=3, height=1, font=('Helvetica', '20'),
                       command=lambda: self.clicked("R"))

        self.__btn19 = Button(self.__mainwindow, text="S", bg="MediumVioletRed",
                       fg="Black", width=3, height=1, font=('Helvetica', '20'),
                       command=lambda: self.clicked("S"))

        self.__btn20 = Button(self.__mainwindow, text="T", bg="MediumVioletRed",
                       fg="Black", width=3, height=1, font=('Helvetica', '20'),
                       command=lambda: self.clicked("T"))

        self.__btn21 = Button(self.__mainwindow, text="U", bg="MediumVioletRed",
                       fg="Black", width=3, height=1, font=('Helvetica', '20'),
                       command=lambda: self.clicked("U"))

        self.__btn22 = Button(self.__mainwindow, text="V", bg="MediumVioletRed",
                       fg="Black", width=3, height=1, font=('Helvetica', '20'),
                       command=lambda: self.clicked("V"))

        self.__btn23 = Button(self.__mainwindow, text="W", bg="MediumVioletRed",
                       fg="Black", width=3, height=1, font=('Helvetica', '20'),
                       command=lambda: self.clicked("W"))

        self.__btn24 = Button(self.__mainwindow, text="X", bg="MediumVioletRed",
                       fg="Black", width=3, height=1,
                       font=('Helvetica', '20'),
                       command=lambda: self.clicked("X"))

        self.__btn25 = Button(self.__mainwindow, text="Y", bg="MediumVioletRed",
                       fg="Black", width=3, height=1,
                       font=('Helvetica', '20'),
                       command=lambda: self.clicked("Y"))

        self.__btn26 = Button(self.__mainwindow, text="Z", bg="MediumVioletRed",
                       fg="Black", width=3, height=1,
                       font=('Helvetica', '20'),
                       command=lambda: self.clicked("Z"))

        ## label showing how many chances left after wrong guessing
        self.__label1 = Label(self.__mainwindow, text="Total Chances are : 5",
                       font=("Courier", 14), bg="Moccasin",fg="FireBrick")

        ## close button
        self.__closeButton = Button(self.__mainwindow, text="CLOSE",
                                    font=("Courier", 14), bg="Moccasin",
                                    fg="FireBrick", command =self.stop)

        ## if the user wants to reset the input, here is the button for it
        self.__tryAgainButton = Button(self.__mainwindow, text="TRY AGAIN",
                                    font=("Courier", 14), bg="Moccasin",
                                    fg="FireBrick", command =self.reset)

        ## makeup for the user interface
        self.__appName.grid(column=0, row=0, columnspan=12, pady=20)
        self.__emotion.grid(column=0, row=1, padx=10)
        self.__bt01.grid(column=1, row=1)
        self.__bt02.grid(column=2, row=1)
        self.__bt03.grid(column=3, row=1)
        self.__bt04.grid(column=4, row=1)
        self.__bt05.grid(column=5, row=1)
        self.__bt06.grid(column=6, row=1)
        self.__bt07.grid(column=7, row=1)
        self.__bt08.grid(column=8, row=1)
        self.__bt09.grid(column=9, row=1)
        self.__btn1.grid(column=1, row=2)
        self.__btn2.grid(column=2, row=2)
        self.__btn3.grid(column=3, row=2)
        self.__btn4.grid(column=4, row=2)
        self.__btn5.grid(column=5, row=2)
        self.__btn6.grid(column=6, row=2)
        self.__btn7.grid(column=7, row=2)
        self.__btn8.grid(column=8, row=2)
        self.__btn9.grid(column=9, row=2)
        self.__btn10.grid(column=2, row=3)
        self.__btn11.grid(column=3, row=3)
        self.__btn12.grid(column=4, row=3)
        self.__btn13.grid(column=5, row=3)
        self.__btn14.grid(column=6, row=3)
        self.__btn15.grid(column=7, row=3)
        self.__btn16.grid(column=8, row=3)
        self.__btn17.grid(column=3, row=4)
        self.__btn18.grid(column=4, row=4)
        self.__btn19.grid(column=5, row=4)
        self.__btn20.grid(column=6, row=4)
        self.__btn21.grid(column=7, row=4)
        self.__btn22.grid(column=4, row=5)
        self.__btn23.grid(column=5, row=5)
        self.__btn24.grid(column=6, row=5)
        self.__btn25.grid(column=4,row=6, columnspan=2)
        self.__btn26.grid(column=5, row=6, columnspan=2)
        self.__label1.grid(row=3, column=0)
        self.__closeButton.grid(row=5, column=0)
        self.__tryAgainButton.grid(row=4, column=0)


    def clicked(self, alphabet):
        """
        When the user clicks whatever letter in the 'keyboard',
        if the letter in the answer string then it will be printed
        to the screen, else the chances of guessing will be minus by 1
        every time the wrong letter is clikced.
        If there is no chance left and the string is not yet guessed,
        a message box appears to give user a message.
        The same thing happens when the user guessed the right word
        :param alphabet: str, a random letter
        """
        answer="GANODERMA"

        if alphabet in answer:
            if alphabet == "G":
                self.__bt01['text'] = alphabet
            elif alphabet == "A":
                self.__bt02['text'] = alphabet
                self.__bt09['text'] = alphabet
            elif alphabet == "N":
                self.__bt03['text'] = alphabet
            elif alphabet == "O":
                self.__bt04['text'] = alphabet
            elif alphabet == "D":
                self.__bt05['text'] = alphabet
            elif alphabet == "E":
                self.__bt06['text'] = alphabet
            elif alphabet == "R":
                self.__bt07['text'] = alphabet
            elif alphabet == "M":
                self.__bt08['text'] = alphabet
            if self.__bt01['text'] == "G" \
                    and self.__bt02['text'] == "A" \
                    and self.__bt03['text'] == "N" \
                    and self.__bt04['text'] == "O" \
                    and self.__bt05['text'] == "D" \
                    and self.__bt06['text'] == "E" \
                    and self.__bt07['text'] == "R" \
                    and self.__bt08['text'] == "M" \
                    and self.__bt09['text'] == "A" \
                    and self.__chances > 0:
                self.__img = Image.open(self.__images[5])
                self.__img = self.__img.resize((300, 200), Image.ANTIALIAS)
                self.__img = ImageTk.PhotoImage(self.__img)
                self.__emotion.configure(image=self.__img)
                messagebox.showinfo("Result", "How could you guess it right. Such a genius!!")
                self.stop()

        else:
            self.__chances -= 1
            txt = "Chances remaining: " + str(self.__chances)
            self.__label1.config(text=txt)
            self.__img = Image.open(self.__images[self.__chances])
            self.__img = self.__img.resize((300, 200), Image.ANTIALIAS)
            self.__img = ImageTk.PhotoImage(self.__img)
            self.__emotion.configure(image=self.__img)

            if self.__chances <= 0:
                messagebox.showinfo("Result", "Oh dear, not really lucky this time...")
                self.stop()


    def reset(self):
        """
        Reset everything in the user interface back to the initial interface
        including the guessed sequence of words, pictures and number of chances
        """
        self.__bt01['text'] = ""
        self.__bt02['text'] = ""
        self.__bt03['text'] = ""
        self.__bt04['text'] = ""
        self.__bt05['text'] = ""
        self.__bt06['text'] = ""
        self.__bt07['text'] = ""
        self.__bt08['text'] = ""
        self.__bt09['text'] = ""
        self.__chances = 5
        self.__img = Image.open(self.__images[self.__chances])
        self.__img = self.__img.resize((300, 200), Image.ANTIALIAS)
        self.__img = ImageTk.PhotoImage(self.__img)
        self.__emotion.configure(image=self.__img)
        self.__label1.configure(text="Total Chances are : 5")


    def stop(self):
        """
        Close the program
        """
        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()

