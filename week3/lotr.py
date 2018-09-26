import os
from art import *

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def header():
    header = text2art('''Lord of the Rings''',font='graffiti',chr_ignore=True)
    print(header)
    raw_input("Press Enter to continue...")

def chooseCharacter():
    charChoiceFlag = False

    choiceofChar = text2art("Before we embark on this adventure...")
    print(choiceofChar)
    raw_input("")
    selectChar = text2art("You will have to choose a character!")
    print(selectChar)
    raw_input("")

    clear_console()

    frodo = text2art("1. Frodo Baggins")
    gandalf = text2art("2. Gandalf the Grey")
    sam = text2art("3. Samwise Gamgee")

    print(frodo)
    print(gandalf)
    print(sam)
    displayChar = text2art("Select from one above")
    print(displayChar)
    charChoice = int(raw_input())

    clear_console()

    while not charChoiceFlag:
        confMessage = text2art("You have chosen")
        print(confMessage)

        if charChoice == 1:
            print(frodo)
        elif charChoice == 2:
            print(gandalf)
        else:
            print(sam)

        proceedMsg = text2art("Continue (Y/N)")
        print(proceedMsg)

        proceedFlag = raw_input()

        if proceedFlag == 'Y' or proceedFlag == 'y':
            charChoiceFlag = True
            clear_console()
            prologue()
        else:
            charChoiceFlag = False


def prologue():
    clear_console()
    line1 = text2art("The world is changing")
    print(line1)
    raw_input("")
    line2 = text2art("I feel it in the water")
    print(line2)
    raw_input("")
    line3 = text2art("I feel it in the earth")
    print(line3)
    raw_input("")
    line4 = text2art("I smell it in the air")
    print(line4)
    raw_input("")
    line5 = text2art("Much that once was is lost...")
    line6 = text2art("..., for none now live who remember it.")
    print(line5)
    print(line6)

    raw_input("")
    clear_console()
    line7 = text2art("The  forging  of  the  Great  Rings", font='doom',chr_ignore=True)
    print(line7)
    raw_input("")
    line8 = text2art("Three were given to the Elves...", font='doom',chr_ignore=True)
    print(line8)
    raw_input("")
    line9 = text2art("Seven to the Dwarf-Lords...", font='doom',chr_ignore=True)
    print(line9)
    raw_input("")
    line9 = text2art("Nine to the race of Men..", font='doom',chr_ignore=True)
    print(line9)
    raw_input("")
    line9 = text2art("...who above all else desire power", font='doom',chr_ignore=True)
    print(line9)
    raw_input("")

    clear_console()

    line10 = text2art("For within these rings...", font='doom',chr_ignore=True)
    print(line10)
    raw_input("")
    line11 = text2art("was bound the strength and will...", font='doom',chr_ignore=True)
    print(line11)
    raw_input("")
    line12 = text2art("...to govern each race", font='doom',chr_ignore=True)
    print(line12)
    raw_input("")

    clear_console()

    line13 = text2art("But  they  were  all  deceived...", font='doom',chr_ignore=True)
    print(line13)
    raw_input("")
    line14 = text2art("..for another ring was made!", font='doom',chr_ignore=True)
    print(line14)
    raw_input("")

    clear_console()

    line15 = text2art("Deep in the land of Mordor...", font='doom',chr_ignore=True)
    print(line15)
    raw_input("")
    line16 = text2art("..in the fires of Mount Doom..", font='doom',chr_ignore=True)
    print(line16)
    raw_input("")
    line16 = text2art("..the Dark Lord Sauron forged..", font='doom',chr_ignore=True)
    print(line16)
    raw_input("")
    line17 = text2art("...A Master Ring", font='doom',chr_ignore=True)
    print(line17)
    raw_input("")

    clear_console()

    line18 = text2art("..and into this ring he poured",font='doom',chr_ignore=True)
    print(line18)
    raw_input("")
    line19 = text2art("...his cruelty, his malice...",font='doom',chr_ignore=True)
    print(line19)
    raw_input("")
    line20 = text2art("...his will to dominate life",font='doom',chr_ignore=True)
    print(line20)
    raw_input("")

    clear_console()

    onering = text2art("""              One    ring    to    rule    them    all""",font='graffiti',chr_ignore=True)
    print(onering)
    raw_input("")

    clear_console()

    line21 = text2art("One by one...", font='doom',chr_ignore=True)
    print(line21)
    raw_input("")
    line22 = text2art("..the free lands of Middle Earth fell..", font='doom',chr_ignore=True)
    print(line22)
    raw_input("")
    line23 = text2art("to the power of the Ring.", font='doom',chr_ignore=True)
    print(line23)
    raw_input("")
    line24 = text2art("There were some who resisted", font='doom',chr_ignore=True)
    print(line24)
    raw_input("")

    clear_console()

    line25 = text2art("A last alliance of men & elves...", font='doom',chr_ignore=True)
    print(line25)
    raw_input("")
    line26 = text2art("..marched against Mordor.", font='doom',chr_ignore=True)
    print(line26)
    raw_input("")
    line27 = text2art("On the sloped of Mount Doom..", font='doom',chr_ignore=True)
    print(line27)
    raw_input("")
    line28 = text2art("..they fought for their freedom", font='doom',chr_ignore=True)
    print(line28)
    raw_input("")

    clear_console()

    line29 = text2art("Victory was near, but...", font='doom',chr_ignore=True)
    print(line29)
    raw_input("")
    line30 = text2art("..The power of the ring...", font='doom',chr_ignore=True)
    print(line30)
    raw_input("")
    line31 = text2art("..could not be undone!", font='doom',chr_ignore=True)
    print(line31)
    raw_input("")
    line32 = text2art("At this moment, when all hope faded...", font='doom',chr_ignore=True)
    print(line32)
    raw_input("")

    clear_console()

    line33 = text2art("Isildur, eldest son of Elendil...", font='doom',chr_ignore=True)
    print(line33)
    raw_input("")
    line34 = text2art("defeated Sauron", font='doom',chr_ignore=True)
    print(line34)
    raw_input("")
    line35 = text2art("The ring passed to Isildur...", font='doom',chr_ignore=True)
    print(line35)
    raw_input("")
    line36 = text2art("..who had the once chance...", font='doom',chr_ignore=True)
    print(line36)
    raw_input("")
    line37 = text2art("..to destroy the ring forever!", font='doom',chr_ignore=True)
    print(line37)
    raw_input("")

    clear_console()

    line37 = text2art("The hearts of men...", font='doom',chr_ignore=True)
    print(line37)
    raw_input("")
    line38 = text2art("..are easily corrupted", font='doom',chr_ignore=True)
    print(line38)
    raw_input("")
    line39 = text2art("The ring has a will of its own!", font='doom',chr_ignore=True)
    print(line39)
    raw_input("")
    line40 = text2art("It betrays Isildur to his death", font='doom',chr_ignore=True)
    print(line40)
    raw_input("")

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
    clear_console()
    chapterTitle = text2art("Chapter 1")
    print(chapterTitle)
    header = text2art("A long Expected Party",font='graffiti',chr_ignore=True)
    print(header)
    raw_input("Press Enter to continue...")

    clear_console()

    paragraph1 = text2art("Bilbo is celebrating his Eleventy-first birthday...")
    print(paragraph1)


def Chapter2():
    clear_console()
    header = text2art("The Shadow of the Past",font='graffiti',chr_ignore=True)
    print(header)
    raw_input("Press Enter to continue...")


def Chapter3():
    clear_console()
    header = text2art("Three is Company",font='graffiti',chr_ignore=True)
    print(header)
    raw_input("Press Enter to continue...")

def main():
    clear_console()
    header()
    # prologue()
    chooseCharacter()


main()
