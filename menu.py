import os
import sys
import saaterstellung as sad


class Menu:

    def __init__(self):
        self.menu()

    def menu(self):
        print("Enter 1 to show currently saved seeds")
        print("Enter 2 to add a new seed to the Database")
        print("Enter 3 to quit program")
        self.command = int(input("Please Enter One of the Numbers: "))

        if self.command == 1:
            self.sven()
        elif self.command == 2:
            sad.create()
        elif self.command == 3:
            sys.quit(0)
        else:
            print("please Enter a Valid Number. Press Enter to try again.")
            input()
