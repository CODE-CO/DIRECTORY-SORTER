# @CODE_CO :) | TELEGRAM: @CODE_CO | GITHUB: CODE-CO | FROM '@CODE_CO' IMPORT 'MR PRO' |------------
#---------------------------------------------------------------------------------------------------
import os, re, shutil
#---------------------------------------------------------------------------------------------------
def PRINT_FILES():
    print()
    for i, o in enumerate(FILES, start=0):
        print(str(i) + " - " + o)
#---------------------------------------------------------------------------------------------------
def LOWER():
        list(map(lambda X: os.rename(X, X.lower()), FILES))
        print("\nCOMPLETED.")
#---------------------------------------------------------------------------------------------------
def UPPER():
        list(map(lambda X: os.rename(X, X.upper()), FILES))
        print("\nCOMPLETED.")
#---------------------------------------------------------------------------------------------------
def REMOVE():
    CHECK = input("\nARE YOU SURE THAT YOU WANT TO REMOVE ALL FILES OR FILES THAT YOU SELECTED IN SELECT MODE? (Y/N): ")
    if CHECK == "YES" or "Y":
        for i in FILES:
            try:
                os.remove(i)
            except:
                shutil.rmtree(i, ignore_errors=True)
        print("\nFILES REMOVED.")
    else:
        print("\nOK NO FILES WILL BE REMOVED.")
#---------------------------------------------------------------------------------------------------
def ADD_TEXT():
    TEXT = input("\nPLEASE ENTER YOUR TEXT TO ADD IN FILES NAME: ")
    LOCATION = input("\nOK YOU WANT ADD IT IN 'FIRST' OR 'END' OF THE FILES NAME? ")
    if LOCATION == "FIRST":
        list(map(lambda X: os.rename(X, TEXT + X), FILES))
    elif LOCATION == "END":
        for i in FILES:
            if os.path.isdir(i):
                os.rename(i, i + TEXT)
            else:
                EXTENSION = re.findall(r"(.*)(\..+)", i)
                A, B = EXTENSION[0]
                os.rename(i, A + TEXT + B)
    else:
        print("\nYOU HAVE NOT ENTERED 'FIRST' OR 'END' SO YOUR TEXT WILL NOT ADD !")
    print("\nCOMPLETED.")
#---------------------------------------------------------------------------------------------------
def SORT():
    for i in FILES:
        if os.path.isfile(i):
            try:
                EXTENSION = ((re.findall(r"(.*)(\..+)", i))[0][1][1:]).upper()
                if isinstance(EXTENSION, str):
                    if EXTENSION not in FILES:
                        os.mkdir(EXTENSION)
                        FILES.append(EXTENSION)
                try:
                    shutil.move(i, EXTENSION)
                except:
                    print("\nDUPLICATE FILE !")
            except:
                pass
    print("\nCOMPLETED.")
#---------------------------------------------------------------------------------------------------
def SORT_FF():
    LIST_FOLDERS, LIST_FILES = list(), list()
    for i in FILES:
        if os.path.isdir(i):
            if len(i) > 1:
                LIST_FOLDERS.append(i)
        else:
            LIST_FILES.append(i)
    for i in LIST_FOLDERS:
        for o in LIST_FILES:
            if i.upper() in ((re.findall(r"(.*)(\..+)", o))[0][0]).upper():
                try:
                    shutil.move(o, i)
                except:
                    print("\nDUPLICATE FILE !")
    print("\nCOMPLETED.")
#---------------------------------------------------------------------------------------------------
def SORT_FOLDERS():
    if "FOLDERS" not in FILES:
        os.mkdir("FOLDERS")
    for i in FILES:
        if os.path.isdir(i):
            try:
                shutil.move(i, "FOLDERS")
            except:
                print("\nDUPPLICATE !")
    print("\nCOMPLETED.")
#---------------------------------------------------------------------------------------------------
def SELECT():
    global FILES, INPUT
    INDEX, FILE = str(), list()
    print("\nUNTILL YOU HAVE NOT ENTERED 'END' WE WILL ASK YOU TO ENTER FILES NUMBER.")
    PRINT_FILES()
    print()
    while INDEX != "END":
        INDEX = input("ENTER THE FILE NUMBER: ").upper()
        if INDEX != "END":
            FILE.append(FILES[int(INDEX)])
    FILES = list(dict.fromkeys(FILE))
    if FILES == []:
        print("\nYOU HAVE NOT SELECTED ANY FILES SO THERE IS NO OPTION TO SELECT !")
    else:
        print("""\n|_______________________|COMMANDS|________________________|\n|ENTER '1' OR 'LOWER' TO LOWERCASE SELECTED FILES.        |\n|ENTER '2' OR 'UPPER' TO UPPERCASE SELECTED FILES.        |\n|ENTER '3' OR 'REMOVE' TO REMOVE ALL SELECTED FILES.      |\n|ENTER '4' OR 'ADD' TO ADD A TEXT TO SELECTED FILES NAME. |\n|_________________________________________________________|""")
        INPUT = input("\nINPUT FOR SELECTED FILES: ").upper()
#---------------------------------------------------------------------------------------------------
def HELP():
    print("""|_____________________|COMMANDS|_____________________|\n|ENTER '00' OR 'FILES' TO SHOW FILES.                |\n|ENTER '01' OR 'LOWER' TO LOWERCASE ALL FILES.       |\n|ENTER '02' OR 'UPPER' TO UPPERCASE ALL FILES.       |\n|ENTER '03' OR 'REMOVE' TO REMOVE ALL FILES.         |\n|ENTER '04' OR 'ADD' TO ADD A TEXT TO FILES NAME.    |\n|ENTER '05' OR 'SORT' TO SORT THE CURRENT FOLDER.    |\n|ENTER '06' OR 'SORT FF' TO SORT FILES WITH FOLDERS. |\n|ENTER '07' OR 'SORT FOLDER' TO SORT FOLDERS.        |\n|ENTER '08' OR 'SELECT' TO SELECT FILES FROM LIST.   |\n|ENTER '09' OR 'HELP' TO SHOW THE HELP COMMAND.      |\n|ENTER '10' OR 'CLEAR' TO CLEAR THE SHELL.           |\n|ENTER '11' OR 'EXIT' TO EXIT OF THIS PROGRAM. :)    |\n|____________________________________________________|""")
#---------------------------------------------------------------------------------------------------
def CLEAR():
    os.system("CLS" if os.name == "nt" else "clear")
#---------------------------------------------------------------------------------------------------
CLEAR(), HELP()
#---------------------------------------------------------------------------------------------------
while True:
    INPUT = input("\nINPUT: ").upper()
    FILES = list(os.listdir(os.getcwd()))
    FILES.remove(os.path.basename(__file__))
#---------------------------------------------------------------------------------------------------
    if INPUT == "SELECT" or INPUT == "8":
        SELECT()
    if INPUT == "FILES" or INPUT == "0":
        PRINT_FILES()
    if INPUT == "LOWER" or INPUT == "1":
        LOWER()
    if INPUT == "UPPER" or INPUT == "2":
        UPPER()
    if INPUT == "REMOVE" or INPUT == "3":
        REMOVE()
    if INPUT == "ADD" or INPUT == "4":
        ADD_TEXT()
    if INPUT == "SORT" or INPUT == "5":
        SORT()
    if INPUT == "SORT FF" or INPUT == "6":
        SORT_FF()
    if INPUT == "SORT FOLDERS" or INPUT == "7":
        SORT_FOLDERS()
    if INPUT == "HELP" or INPUT == "9":
        HELP()
    if INPUT == "CLEAR" or INPUT == "10":
        CLEAR()
    if INPUT == "EXIT" or INPUT == "11":
        break
#---------------------------------------------------------------------------------------------------
print("\nBYE :)\n")
