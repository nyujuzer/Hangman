import os
import secrets
Words_hu = ["piton", "indul", "gyűlölt", "vulkán", "csontváz", "kezdő", "korház","cserél","végpont"]
Words_eng = ["python","launch","hated","vulcano","uniform","default","hospital","rest","replace","node"]


clear = lambda: os.system('cls')
def game_hu(wordlist):
    diff = 0
    print("Hány próbálkozást akarsz?\nsok/elég/kevls")
    choice = input(">>>")

    deathcount = 0
    print(len(wordlist))
    word = secrets.choice(wordlist)
    wordlen = []
    discarded_letters = []
    wrd = []
    for i in word:
        wrd.append(i)
        wordlen.append("_")

    gameover = False
    tries = 0
    while gameover == False:
        clear()#print("\n"*100)
        if choice.upper() == "SOK":
            print("15 próbálkozásod van")
            diff = 15
        elif choice.upper() == "ELÉG":
            print("10 Próbálkozásod van")
            diff = 10
        elif choice.upper() == "KEVÉS":
            print("6 Próbálkozásod van")
            diff = 6
        else:
            print("Nem tudtuk feldolgozni a válaszod, az alap(10) próbával folytatod")
        """
        Testing
        
        print(wrd)
        """
        print("Hátralévő próbálkozásaid száma: "+str(diff-deathcount))
        print("Ezek a betűk nincsenek a szavaidban : " + ",".join(discarded_letters))
        print(".".join(wordlen))
        letter = input("Adj meg egy olyan betűt, ami benne lehet a szóban\n\nEgyszerre csak egy betűt adjon meg")

        if letter in wrd:

            index = wrd.index(letter)
            wordlen[index] = letter
        else:
            print("Ez nem talált")
            discarded_letters.append(letter)

            deathcount += 1


        if deathcount == diff:
            clear()
            print("Sajnálom, de ez nem sikerült")
            print("A szavad a "+"".join(wrd)+" volt."+"\n"+str(tries)+" Próbálkozásod volt")
            ret = input("ismét játszani akarsz?\ni/n>>> ")
            if ret.upper() == "i":
                game_hu()
            else:
                exit()
            gameover = True
        if wrd == wordlen:
            clear()
            print("Gratulálok, sikerült!")
            print("A szavad a "+"".join(wrd)+" volt"+"\n"+str(tries)+" Prábálkozásba telt kitalálnod")
            ret = input("ismét játszani akarsz?\ni/n>>> ")
            if ret.upper() == "I":
                game_hu(Words_hu)
            else:
                exit()
            gameover = True
        tries += 1

def game(wordlist):
    diff = 0
    print("How many chances would you like to have?\nmany/few/little")
    choice = input(">>>")

    deathcount = 0
    print(len(wordlist))
    word = secrets.choice(wordlist)
    wordlen = []
    discarded_letters = []
    wrd = []
    for i in word:
        wrd.append(i)
        wordlen.append("_")

    gameover = False
    tries = 0
    while gameover == False:
        clear()#print("\n"*100)
        if choice.upper() == "MANY":
            print("You have 15 chances")
            diff = 15
        elif choice.upper() == "FEW":
            print("You have 10 chances")
            diff = 10
        elif choice.upper() == "LITTLE":
            print("You have 6 chances")
            diff = 6
        else:
            print("Your answer could not be processed, resorting to default (10) chances")
        """
        Testing
        
        print(wrd)
        """
        print("remaining tries"+str(diff-deathcount))
        print("These letters aren't in the word : " + ",".join(discarded_letters))
        print(".".join(wordlen))
        letter = input("enter one letter you think is in the word\n\nOnly input the word one letter at a time")

        if letter in wrd:
            index = wrd.index(letter)
            wordlen[index] = letter
        else:
            print("you didn't hit it this time")
            discarded_letters.append(letter)

            deathcount += 1


        if deathcount == diff:
            clear()
            print("i'm sorry, but you lost")
            print("The word was "+"".join(wrd)+"\nyou've finished this word in "+str(tries)+" tries")
            ret = input("Would you like to go again?\ny/n>>> ")
            if ret.upper() == "Y":
                game(Words_eng)
                gameover = True
            else:
                exit()
            gameover = True
        if wrd == wordlen:
            clear()
            print("Congratulations, you win!")
            print("The word was "+"".join(wrd)+"\nyou've finished this word in "+str(tries)+" tries")
            ret = input("Would you like to go again?\ny/n>>> ")
            if ret.upper() == "Y":
                game(Words_eng)
                gameover = True
            else:
                exit()  
            gameover = True
        tries += 1


def test(letter, wrd, wordlen):
     if letter in wrd:
            inde = wrd.index(letter)
            wordlen[inde] = letter
            print("nat"+str(inde))
            ref = len(wrd)-inde
            
            for i in range(len(wrd)-inde):#+(index+1)):
                print("inde"+str(len(wrd)-(inde)))
                inde = wrd.index(letter, inde+1)
                wordlen[inde] = letter
            return "ref"+str(ref)+"\nwlen"+str(wordlen)+"\nwrd"+ str(wrd)

lang = input("Milyen nyelvet akar használni?\nwhat of language would you like to use?\nhu/eng >>> ")
if lang.upper() == "HU":
    game_hu(Words_hu)

elif lang.upper() == "ENG":
    print("in eng")
    game(Words_eng)

#game(Words)#//TODO Hangman
