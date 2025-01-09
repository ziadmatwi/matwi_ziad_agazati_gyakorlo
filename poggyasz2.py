class Poggyasz:
    def __init__(self,listoftext=[],lista=[],listb=[],listc=[],listm=[]):
        self.listoftext = listoftext

    def readfile(self,filename):
        luggagefile = open(filename, "r")
        junk:str = luggagefile.readline()
        listofluggage = luggagefile.readlines()
        luggagefile.close()
        for i in range(len(listofluggage)):
           listofluggage[i] = listofluggage[i].strip("\n")
        self.listoftext =listofluggage
        for i in range (len(listofluggage)):
            listofluggage[i].split("#")