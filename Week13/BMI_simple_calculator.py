from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()
        self.__mainwindow.title("BMI calculator")

        # Create an Entry-component for the weight.
        self.__weight_text = Label(self.__mainwindow, text="Enter your weight in kg")
        self.__weight_text.pack()
        self.__weight_value = Entry()
        self.__weight_value.pack()


        # Create an Entry-component for the height.
        self.__height_text = Label(self.__mainwindow, text="Enter your height in cm")
        self.__height_text.pack()
        self.__height_value = Entry()
        self.__height_value.pack()

        # Create a Button to calculate BMI
        self.__calculate_button = Button(self.__mainwindow, bg="blue",
                                         text="Calculate",
                                         command = self.calculate_BMI)
        self.__calculate_button.pack()

        # Create a Label that will show the decimal value of the BMI
        # after it has been calculated.
        self.__result_text = Label()
        self.__result_text.pack()

        # Create a Label that will show a verbal description of the BMI
        # after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow)
        self.__explanation_text.pack()

        # Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow, text="Stop",
                                    bg="red", command=self.stop)
        self.__stop_button.pack()


    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """

        try:
            weight=float(self.__weight_value.get())
            height=float(self.__height_value.get())/100

            if weight<=0 or height <=0:
                self.__explanation_text["text"] = "Error: height and weight must be positive."
                self.reset_fields()
            else:
                result = weight/(height**2)
                self.__result_text["text"] = "{:.2f}".format(result)
                if result > 25:
                    self.__explanation_text["text"] = "You are overweight."
                elif result < 18.5:
                    self.__explanation_text["text"] = "You are underweight."
                else:
                    self.__explanation_text["text"] = "Your weight is normal."
        except ValueError:
            self.__explanation_text["text"] = "Error: height and weight must be numbers."
            self.reset_fields()


    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """
        self.__weight_value.delete(0, END)
        self.__height_value.delete(0, END)


    def stop(self):
        """
        Ends the execution of the program.
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
