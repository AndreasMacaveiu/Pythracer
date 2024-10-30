import random
import time
import sys

#OPTIONS
controloptions = {"r":"Try again", "q":"Quit"}
difficultyoptions = {"easy":"Very basic", "medium":"complex", "hard":"Very complex"}
stats = {"Time":"","Typo(s)":"","Wpm":""}
choiceoptions = {"y": "Yes", "n": "No"}
gamemode_options = {"normal":"A predetermined text from a chosen library","random":"A sequence of words randomly put together"}


#Normal game mode
easy = ["Atomic bent chetler är den bästa skidan","Rosignol sender free 110 är också bra","Coolaste skidåkaren är Sammy"]
medium = ["sju sjö sjuka sjömen skjöt sjutton sjuka barn","Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked. If Peter Piper picked a peck of pickled peppers,Where’s the peck of pickled peppers Peter Piper picked?"]
hard = ["I en känd essä med titeln ”Den moderna pessimismen och dess vedersakare” skriver Karl Vennberg om hur illa människans djupare behov och rikare möjligheter passar ett framstegsideal dikterat av förnuftskult: ”Människan som bihang till framgången, de ekonomiska förändringarna, den psykologiska analysen bar sig ungefär lika bakvänt åt som den gamla människan, som bara var ett bihang till en vidskepelse, en religion eller en idé.” Essän trycktes 1946 i tidskriften 40-tal, men framfördes redan hösten 1945 som en så kallad diskussionsinledning. (Dess ambitionsnivå förstummade möjligen en och annan i auditoriet.) I skuggan av kriget och atombombernas svampmoln försöker Vennberg med hela sin ironiska förvandlingskonst komma bröstgänges med den amorfa frågan om ändamål och medel i samhället och konsten.", "hej", "11111111111111111111111111111111111111I111111111"]

#Random game mode
easyrand = ["springer", "hoppar", "skrattar", "läser", "simmar", "skriver", "sjunger", "bygger", "målar", "dansar", "glad", "vacker", "liten", "stor", "snabb", "mörk", "stark", "tyst", "rolig", "klok", "snabbt", "långsamt", "högt", "lågt", "tyst", "sällan", "ofta", "aldrig", "alltid", "noggrant", "katt", "bil", "bok", "hus", "stol", "fönster", "blomma", "bord", "båt", "penna", "hund", "väska", "park", "stad", "tak", "fågel", "skog", "sjö", "träd", "nyckel"]
mediumrand = ["universitet", "översättning", "höstvind", "skrivbord", "tidning", "resväska", "korridor", "kamera", "bibliotek", "dokument", "analysera", "utforska", "undervisa", "experimentera", "beräkna", "kommunicera", "reflektera", "planera", "förutse", "observera", "ambitiös", "intressant", "utmanande", "komplex", "bekväm", "kreativ", "strategisk", "effektiv", "tålmodig", "modig", "grundligt", "successivt", "snirkligt", "noga", "sällsynt", "plötsligt", "tystlåtet", "omedelbart", "tillfälligt", "noggrant", "fågelsång", "soluppgång", "avtalsbrott", "regnskur", "vänskap", "ledarskap", "känsla", "samtal", "förhandling", "vetenskap", "innovation"]
hardrand = ["kontemplation", "pluralism", "komplexitet", "hierarki", "subvention", "kognitiv", "metaforik", "paradigm", "föreställning", "symbios", "revidera", "konkretisera", "diversifiera", "implementera", "dekonstruera", "kommodifiera", "resonera", "konsolidera", "exemplifiera", "differentiera", "diskret", "oöverträffad", "ambivalent", "mångtydig", "antitetisk", "intrikat", "oförblommerad", "komplicerad", "dekadent", "oscillerande", "parallellt", "gradvis", "ambitiöst", "relativt", "kategoriskt", "analogt", "implicit", "explicit", "diametralt", "hypotetiskt", "formalism", "existentialism", "postmodernism", "institutionalisering", "ideologi", "epistemologi", "desillusion", "retrospektiv", "objektivitet", "perception"]


def splash():
    print( "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print( "          Pythracer                   ")
    print( "      TYPE OR DIEEEEEEEE              ")
    print( "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def choosetext (library): #Har viewtext har implementerat momenten med random ur en lista
    x = random.randint (0,len(library)-1)
    currentlist = library[x]
    return currentlist

def maketext(library):
    x = random.sample (library,10)
    selected_list = " ".join(x)
    return selected_list

def typing():
    attempt = input("")
    return (attempt)


def accuracy(text,library):
    facit = library.split(" ")
    test = text.split(" ")
    a = 0
    fel = 0
    if len(test) < len(facit):
        fel += len(facit)-len(test)
    elif len(test) > len(facit):
        test = test[:(len(facit)-len(test))]
    for word in test:
        if word == facit[a]:
            a +=1
        else:
            fel += 1
            a+=1
    return(fel)
    #print (f"Antal felstavade ord: {fel}")

def wpm(timer, text, mistakes):
    list_of_words = text.split(" ")
    if mistakes == "0":
        wpm1 = len(text) / int(timer) * 60
        wpm_final = wpm1 / 5
        return wpm_final
    elif int(mistakes) > 0:
        correct_words = list_of_words[:-int(mistakes)]
        string_words = " ".join(correct_words)
        wpm1 = len(string_words) / int(timer) * 60
        wpm_final = wpm1 / 5
        return wpm_final

def view(description, strings):
    print()
    print(description)
    print()
    for x in strings:
        print(f"    {x})  {strings[x]}")

def menu(title, prompt, options):
    view(title, options)
    action = input(prompt)
    if action in options:
       return action
    else: 
        print(f"{action} is not an option")
    

def select(title, prompt, options,gamemode):
    view(title, options)
    if gamemode == "normal":
        while True:
            diff = input(prompt)
            if diff in options:
                if diff == "easy":
                    return choosetext(easy) 
                elif diff == "medium":
                    return choosetext(medium)
                elif diff == "hard":
                    return choosetext(hard)
            else:
                print(f"{diff} is not an option")
                action = menu("Invalid difficulty", "Option: ", controloptions)
                if action == "q":
                    sys.exit("Quitting")
                elif action == "r":
                    print("ok")
                elif action != "r" or "q": 
                    print("try, try again")
    elif gamemode == "random":
        while True:
            diff = input(prompt)
            if diff in options:
                if diff == "easy":
                    return maketext(easyrand) 
                elif diff == "medium":
                    return maketext(mediumrand)
                elif diff == "hard":
                    return maketext(hardrand)
            else:
                print(f"{diff} is not an option")
                action = menu("Invalid difficulty", "Option: ", controloptions)
                if action == "q":
                    sys.exit("Quitting")
                elif action == "r":
                    print("ok")
                elif action != "r" or "q": 
                    print("try, try again")
                
def select_game(title, prompt, options):
    view(title, options)
    while True:
        diff = input(prompt)
        if diff in options:
            if diff == "normal":
                return ("normal")
            elif diff == "random":
                return ("random")
        else:
            print(f"{diff} is not an option")
            action = menu("Invalid difficulty", "Option: ", controloptions)
            if action == "q":
                sys.exit("Quitting")
            elif action == "r":
                print("ok")
            elif action != "r" or "q": 
                print("try, try again")

def save_highscore(lista,filename="highscore.txt"):
    action = menu("Would you like to be engraved eternally into THE Highscore", "Y/N: ", choiceoptions)
    if action == "y":
        name = input("What name would you like to be remembered as? ")
        with open(filename, "a") as file:
            file.write(name + str(lista)+"\n")
            print("Registered")
    else:
        print("You weren't good enough anyway")
        
def load_highscore(filename="highscore.txt"):
    try:
        with open(filename, "r") as file:
            highscore = file.read()
            return highscore
    except FileNotFoundError:
            return 0



def startgame():
    start_time = time.time()
    current = opt1
    print(current)
    attempt = typing()
    accurate = str(accuracy (attempt,current))
    end_time = time.time()
    final_time = end_time - start_time
    wpm_1 = wpm(final_time, attempt, accurate)
    q = str(round(final_time,2))
    stats["Time"]=q
    stats["Typo(s)"] = accurate
    stats["Wpm"] = wpm_1
    view("Stats; Time, Typo(s)", stats)


    
splash()
gamemode = select_game("Welcome to pythracer! What gamemode would you like to play?", "Gamemode chosen: ", gamemode_options)
opt1 = select(f"You've selected {gamemode}. Please select a Difficulty", "Difficulty selected: ", difficultyoptions,gamemode)
print()
startgame()
save_highscore(stats)
print()
highscore = load_highscore()
print("HIGHSCORES OVER THE YEARS:")
print()
print(f"{highscore}")