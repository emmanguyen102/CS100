from tkinter import *

class Counter:
    def __init__(self):
        self.__main_window = Tk()
        self.__var = StringVar()
        self.__value=0

        self.__current_value = Label(self.__main_window, textvariable=self.__var)
        self.__var.set(self.__value)
        self.__current_value.grid(row=1, columnspan=5)

        self.__reset_button = Button(self.__main_window, text="Reset",
                                     command=self.reset)
        self.__reset_button.grid(row=2, column=1, rowspan=2)

        self.__increase_button = Button(self.__main_window,
                                        text="Increase",
                                        command=self.increase)
        self.__increase_button.grid(row=2, column=2, rowspan=3)

        self.__decrease_button = Button(self.__main_window,
                                        text="Decrease",
                                        command=self.decrease)
        self.__decrease_button.grid(row=2, column=3, rowspan =3)

        self.__quit_button = Button(self.__main_window,
                                    text="Quit", command=self.lopeta)
        self.__quit_button.grid(row=2, column=4, rowspan =2)

        self.__main_window.mainloop()

    def reset(self):
        self.__value = 0
        self.__var.set(self.__value)

    def lopeta(self):
        self.__main_window.destroy()

    def increase(self):
        self.__value += 1
        self.__var.set(self.__value)

    def decrease(self):
        self.__value -= 1
        self.__var.set(self.__value)


def main():
    Counter()


if __name__ == "__main__":
    main()
