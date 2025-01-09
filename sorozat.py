import random

def random_method(count,list=[]):
    for i in range(count):
        random_number = int(random.random()*(1000+10+1)-10)
        list.append(random_number)
        print(f"{random_number}$", end="")

def random_method_modified(count,list=[]):
    finaltext:str=""
    for i in range(count):
        random_number = int(random.random()*(1000+10+1)-10)
        list.append(random_number)
        finaltext = finaltext + f"{random_number}$"
    finaltext = finaltext.strip("$")
    return finaltext

def paratlanok_szama(list=[]):
    even_count:int = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            even_count+=1
    return even_count

def printout(number):
    finaltext = f"A páratlanok száma: {number}"
    return finaltext

def writeout(text):
    resultfile = open("eredmeny.txt", "w")
    resultfile.write(text)
    

