class Poggyasz:
    def __init__(self,listoftext=[]):
        self.listoftext = listoftext

    def readfile(self,filename):
        luggagefile = open(filename, "r")
        listofluggage = luggagefile.readlines()
        luggagefile.close()
        self.listoftext =listofluggage