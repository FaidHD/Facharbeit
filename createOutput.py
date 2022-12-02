class Output:

    def __init__(self, string):
        self.printstring = string

    def printString(self):
        print("") #leerzeilen um alte Ausgabe weiter nach oben zu schieben
        print("")
        print("")
        print("")
        print("")
        print("------------------------------")
        for i in self.printstring: # jeder String im Array wird einzeln geprinted
            print(i)
        print("------------------------------")
        print("")
        print("")
        print("")
        print("")
        print("")