import random

easy = ["Atomic bent chetler är den bästa skidan","Rosignol sender free 110 är också bra","Coolaste skidåkaren är Sammy"]

def choosetext (library): #Har viewtext har implementerat momenten med random ur en lista
    x = random.randint (0,len(library)-1)
    currentlist = library[x]
    return currentlist

def typing():
   attempt = input("")
   return (attempt)


def accuracy(text,library):
    facit = library.split(" ")
    test = text.split(" ")
    a = 0
    fel = 0
    for word in test:
        if word == facit[a]:
            a +=1
        else:
            fel += 1
            a+=1
    print (f"Antal felstavade ord: {fel}")
    


current = choosetext(easy)
print(current)

attempt = typing()
accuracy (attempt,current)

