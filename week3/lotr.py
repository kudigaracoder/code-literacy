import os
import time
from art import *
from termcolor import colored, cprint

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def header():
    tprint('''
                Lord
                of
                the
               Rings''',font='graffiti',chr_ignore=True)

    # Using cprint & blink attr to make the text blink - The keyboardInterrupt fires
    # cprint('Press Enter to continue...','red',attrs=['blink'])

    raw_input("Press ENTER to continue...")


def chooseCharacter():
    charChoiceFlag = False


    defaultHeader("Before we embark on this adventure...")
    defaultHeader("You will have to choose a character!")

    clear_console()

    frodo = text2art("1. Frodo Baggins")
    gandalf = text2art("2. Gandalf the Grey")
    sam = text2art("3. Samwise Gamgee")

    defaultHeader(frodo)
    defaultHeader(gandalf)
    defaultHeader(sam)
    defaultHeader("Select from one above")
    charChoice = int(raw_input())

    clear_console()

    while not charChoiceFlag:
        defaultHeader("You have chosen")

        if charChoice == 1:
            print(frodo)
        elif charChoice == 2:
            print(gandalf)
        else:
            print(sam)

        defaultHeader("Continue (Y/N)")

        proceedFlag = raw_input()

        if proceedFlag == 'Y' or proceedFlag == 'y':
            charChoiceFlag = True
            clear_console()
            prologue()
        else:
            charChoiceFlag = False
            chooseCharactor(True)

def graffitiHeader(headerText):
    clear_console()
    header = text2art(headerText, font='graffiti',chr_ignore=True)
    print(header)
    time.sleep(2)

def doomHeader(headerText):
    header = text2art(headerText, font='doom',chr_ignore=True)
    print(header)
    time.sleep(2)

def defaultHeader(headerText):
    header = text2art(headerText)
    print(header)
    time.sleep(2)

def prologue():
    clear_console()

    defaultHeader("The  world  is  changing")
    defaultHeader("I  feel  it  in  the  water")
    defaultHeader("I  feel  it  in  the  earth")
    defaultHeader("I  feel  it  in  the  air")
    defaultHeader("Much  that  once  was  is  lost...")
    defaultHeader("...for   none  now  live  who remember  it!")

    clear_console()

    doomHeader("The  forging  of  the  Great  Rings")
    doomHeader("Three  were  given  to  the  Elves..")
    doomHeader("Seven  to  the  Dwarf-Lords..")
    doomHeader("Nine  to  the  race  of  Men..")
    doomHeader("..who  above  all  else  desire  power")

    clear_console()

    doomHeader("For  within  these  rings...")
    doomHeader("was  bound  the  strength  and  will...")
    doomHeader("...to  govern  each  race")

    clear_console()

    doomHeader("But  they  were  all  deceived...")
    doomHeader("..for  another  ring  was  made!")

    clear_console()

    doomHeader("Deep  in  the  land  of  Mordor...")
    doomHeader("..in  the  fires  of  Mount  Doom..")
    doomHeader("..the  Dark  Lord  Sauron  forged..")
    doomHeader("...A  Master  Ring")

    clear_console()

    doomHeader("..and  into  this  ring  he  poured..")
    doomHeader("...his  cruelty,  his  malice...")
    doomHeader("...his  will  to  dominate  life")

    clear_console()

    graffitiHeader("""              One    ring    to    rule    them    all""")

    clear_console()

    doomHeader("One  by  one...")
    doomHeader("..the  free  lands  of  Middle  Earth  fell..")
    doomHeader("to the power of the  Ring.")

    clear_console()

    doomHeader("There  were  some  who  resisted")
    doomHeader("A  last  alliance  of  men  &  elves...")
    doomHeader("..marched  against  Mordor.")
    doomHeader("On  the  sloped  of  Mount  Doom..")
    doomHeader("..they  fought  for  their  freedom")

    clear_console()

    doomHeader("Victory  was  near,  but...")
    doomHeader("..The  power  of  the  ring...")
    doomHeader("..could  not  be  undone!")
    doomHeader("At this moment, when all hope faded..")

    clear_console()

    doomHeader("Isildur,  eldest  son  of  Elendil...")
    doomHeader("defeated  Sauron")
    doomHeader("The  ring  passed  to  Isildur...")
    doomHeader("..who  had  the  one  chance...")
    doomHeader("..to  destroy  the  ring  forever!")

    clear_console()

    doomHeader("The  hearts  of  men...")
    doomHeader("..are  easily  corrupted")
    doomHeader("The  ring  has  a  will  of  its  own!")
    doomHeader("It  betrays  Isildur  to  his  death")

    clear_console()


    print("And some things that should not have been forgotten were lost. History became legend. Legend became myth. And for two and a half thousand years, the ring passed out of all knowledge. ")
    raw_input("")
    print("Until, when chance came, it ensnared another bearer.")
    raw_input("")
    print("It came to the creature Gollum, who took it deep into the tunnels of the Misty Mountains. And there it consumed him. The ring gave to Gollum unnatural long life. For five hundred years it poisoned his mind, and in the gloom of Gollum's cave, it waited. ")
    raw_input("")
    print("Darkness crept back into the forests of the world. Rumor grew of a shadow in the East, whispers of a nameless fear, and the Ring of Power perceived its time had come. It abandoned Gollum, but then something happened that the Ring did not intend.")
    raw_input("")
    print("It was picked up by the most unlikely creature imaginable: a hobbit, Bilbo Baggins, of the Shire.")
    raw_input("")
    Chapter1()

def Chapter1():
    doomHeader("Chapter    1")
    graffitiHeader("A    long    Expected    Party")

    clear_console()

    tprint('''Bilbo is celebrating
    his Eleventy-first birthday''')


def Chapter2():
    clear_console()
    graffitHeader("The Shadow of the Past")


def Chapter3():
    clear_console()
    graffitiHeader("Three is Company")

def main():
    clear_console()
    header()
    prologue()
    # chooseCharacter()

main()
