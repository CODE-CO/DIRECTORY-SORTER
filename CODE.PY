# @CODE_CO :) | TELEGRAM: @CODE_CO | GITHUB: CODE-CO ------------------------------------------------|
import re, os, shutil
PATH = os.getcwd()
INPUT = "@CODE_CO :)"
BASENAME = os.path.basename(__file__)
os.system("CLS" if os.name == "nt" else "clear")
print("| @CODE_CO :) | TELEGRAM: @CODE_CO | GITHUB: CODE-CO |")
#----------------------------------------------------------------------------------------------------|
print("""|____________________________________________________|
|_____________________|COMMANDS|_____________________|
|ENTER '00' OR 'FILES' TO SHOW FILES.                |
|ENTER '01' OR 'LOWER' TO LOWERCASE ALL FILES.       |
|ENTER '02' OR 'UPPER' TO UPPERCASE ALL FILES.       |
|ENTER '03' OR 'REMOVE' TO REMOVE ALL FILES.         |
|ENTER '04' OR 'ADD' TO ADD A TEXT TO FILENAMES.     |
|ENTER '05' OR 'SORT' TO SORT THE FOLDER.            |
|ENTER '06' OR 'SORT FF' TO SORT FILES WITH FOLDERS. |
|ENTER '07' OR 'SORT FOLDER' TO SORT FOLDERS.        |
|ENTER '08' OR 'UPPER FOLDERS' TO UPPERCASE 2 FOLDER.|
|ENTER '09' OR 'CLEAR' TO CLEAR THE SHELL.           |
|ENTER '10' OR 'SELECT' TO SELECT A FILE.            |  
|ENTER '11' OR 'HELP' TO SHOW THE HELP COMMAND AGAIN.|
|ENTER '12' OR 'EXIT' FOR EXIT OF THIS PROGRAM. :)   |
|____________________________________________________|""")
#----------------------------------------------------------------------------------------------------|
while INPUT != "EXIT" and INPUT != "12":
    try:
        INPUT = input("\nINPUT: ").upper()
        FILES = list(os.listdir(PATH))
        FILES.remove(BASENAME)
    except:
        print("\nERROR ! PROGRAM MAY NOT WORK CORRECTLY.")
#----------------------------------------------------------------------------------------------------|  
    if INPUT == "FILES" or INPUT == "0":
        try:
            print()
            COUNTER = 0
            for i in FILES:
                print(str(COUNTER) + "- " + i)
                COUNTER +=1
            COUNTER = 0
            print("\nCOMPLETED.")
            continue
        except:
            print("\nERROR !")
            continue
#----------------------------------------------------------------------------------------------------|
    if INPUT == "LOWER" or INPUT == "1":
        try:
            for i in FILES:
                os.rename(i, i.lower())
            print("\nCOMPLETED.")
            continue
        except:
            print("\nERROR !")
            continue
#----------------------------------------------------------------------------------------------------|
    if INPUT == "UPPER" or INPUT == "2":
        try:
            for i in FILES:
                os.rename(i, i.upper())
            print("\nCOMPLETED.")
            continue
        except:
            print("\nERROR !")
            continue
#----------------------------------------------------------------------------------------------------|
    if INPUT == "REMOVE" or INPUT == "3":
        try:
            CHECK = input("\nARE YOU SURE? (Y/N): ")
            if CHECK == "Y" or "YES":
                for i in FILES:
                    try:
                        os.remove(i)
                    except:
                        os.rmdir(i)
            else:
                if CHECK == "N" or "NO":
                    print("\nOK")
                else:
                    print("\nWRONG INPUT !")
            print("\nCOMPLETED.")
            continue
        except:
            print("\nERROR !")
            continue
#----------------------------------------------------------------------------------------------------|
    if INPUT == "ADD" or INPUT == "4":
        try:
            ADD = input("\nPLEASE ENTER YOUR TEXT TO ADD IN FILE NAME: ")
            ADD_LOCATION = input("\nOK YOU WANT ADD IT IN FIRST OR END OF FILE NAME? ")
            if ADD_LOCATION == "FIRST":
                for i in FILES:
                    os.rename(i, ADD + i)
            if ADD_LOCATION == "END":
                for i in FILES:
                    BOOLEAN = os.path.isdir(i)
                    if BOOLEAN:
                        os.rename(i, i + ADD)
                    else:
                        try:
                            EXT = re.findall(r"(.*)(\..+)", i)
                            A, B = EXT[0]
                            os.rename(i, A + ADD + B)
                        except:
                            os.rename(i, i + ADD)
                            print("\nWE GOT ERROR FOR THIS FILE ({0}) BUT WE DID THE JOB.".format(i))
            print("\nCOMPLETED.")
            continue
        except:
            print("\nERROR !")
            continue
#----------------------------------------------------------------------------------------------------|  
    if INPUT == "SORT" or INPUT == "5":
        try:
            for i in FILES:
                BOOLEAN = os.path.isdir(i)
                try:
                    EXT = re.findall(r"(.*)(\..+)", i)
                    A, B = EXT[0]
                    B = B[1:].upper()
                except:
                    BOOLEAN = True
                try:
                    if BOOLEAN:
                        pass
                    else:
                        os.mkdir(B)
                        try:
                            shutil.move(i, B)
                        except:
                            print("\nDUPLICATE FILE !")
                except:
                    if BOOLEAN:
                        pass
                    else:
                        try:
                            shutil.move(i, B)
                        except:
                            print("\nDUPLICATE FILE !")
            print("\nCOMPLETED.")
            continue
        except:
            print("\nERROR !")
            continue
#----------------------------------------------------------------------------------------------------|
    if INPUT == "SORT FF" or INPUT == "6":
        try:
            LIST_FOLDERSS = list()
            LIST_FILESS = list()
            for i in FILES:
                BOOLEAN = os.path.isdir(i)
                if BOOLEAN:
                    if len(i) != 1:
                        LIST_FOLDERSS.append(i)
                else:
                    LIST_FILESS.append(i)
            for i in LIST_FOLDERSS:
                for o in LIST_FILESS:
                    if i.upper() in o.upper():
                        shutil.move(o, i)
            print("\nCOMPLETED.")
            continue
        except:
            print("\nERROR !")
            continue
#----------------------------------------------------------------------------------------------------|
    if INPUT == "SORT FOLDERS" or INPUT == "7":
        try:
            for i in FILES:
                BOOLEAN = os.path.isdir(i)
                try:
                    EXT = re.findall(r".*", i)
                    A = [0]
                except:
                    BOOLEAN = False
                try:
                    if BOOLEAN:
                        os.mkdir("FOLDERS")
                        try:
                            shutil.move(i, "FOLDERS")
                        except:
                            print("\nDUPLICATE FILE !")
                    else:
                        pass
                except:
                    if BOOLEAN:
                        try:
                            shutil.move(i, "FOLDERS")
                        except:
                            print("\nDUPLICATE FILE !")
            print("\nCOMPLETED.")
            continue
        except:
            print("\nERROR !")
            continue
#----------------------------------------------------------------------------------------------------|
    if INPUT == "UPPER PATH" or INPUT == "8":
        try:
            FOLDERS_PATH = list()
            for i in FILES:
                    os.rename(i, i.upper())
            FILES = list(map(lambda X: X.upper(), FILES))
            for i in FILES:
                FOLDERS_PATH.append(i) if os.path.isdir(i) else None
            for i in FOLDERS_PATH:
                os.chdir(i)
                NEW_FILES = os.listdir(os.getcwd())
                for i in NEW_FILES:
                    os.rename(i, i.upper())
                os.chdir(PATH)
            print("\nCOMPLETED.")
            continue
        except:
            print("\nERROR !")
            continue
#----------------------------------------------------------------------------------------------------|
    if INPUT == "CLEAR" or INPUT == "9":
        try:
            os.system("CLS" if os.name == "nt" else "clear")
            continue
        except:
            print("\nERROR !")
            continue
#----------------------------------------------------------------------------------------------------|
    if INPUT == "SELECT" or INPUT == "10":
        try:
            print()
            COUNTER = 0
            for i in FILES:
                print(str(COUNTER) + "- " + i)
                COUNTER +=1
            COUNTER = 0
            FILE = FILES[int(input("\nENTER THE FILE NUMBER: "))]
            print("""
|_____________________|COMMANDS|_____________________|
|ENTER '0' OR 'LOWER' TO LOWERCASE THE SELECTED FILE.|
|ENTER '1' OR 'UPPER' TO UPPERCASE THE SELECTED FILE.|
|ENTER '2' OR 'ADD' TO ADD STH TO SELECTED FILENAME. |
|ENTER '3' OR 'REMOVE' TO REMOVE THE SELECTED FILE.  |
|____________________________________________________|""")
            INPUT = input("\nINPUT FOR DO IN THIS FILE: ").upper()
            BOOLEAN = False
#----------------------------------------------------------------------------------------------------|
            if INPUT == "LOWER" or INPUT == "0":
                os.rename(FILE, FILE.lower())
                BOOLEAN = True
#----------------------------------------------------------------------------------------------------|
            if INPUT == "UPPER" or INPUT == "1":
                os.rename(FILE, FILE.upper())
                BOOLEAN = True
#----------------------------------------------------------------------------------------------------|
            if INPUT == "ADD" or INPUT == "2":
                ADD = input("\nPLEASE ENTER YOUR TEXT TO ADD IN FILE NAME: ")
                ADD_LOCATION = input("\nOK YOU WANT ADD IT IN FIRST OR END OF FILE NAME? ")
                if ADD_LOCATION == "FIRST":
                    os.rename(FILE, ADD + "-" + FILE)
                if ADD_LOCATION == "END":
                    BOOLEAN = os.path.isdir(FILE)
                    if BOOLEAN:
                        os.rename(FILE, FILE + ADD)
                    else:
                        try:
                            EXT = re.findall(r"(.*)(\..+)", FILE)
                            A, B = EXT[0]
                            os.rename(FILE, A + ADD + B)
                        except:
                            os.rename(FILE, FILE + ADD)
                            print("\nWE GOT ERROR FOR THIS FILE ({0}) BUT WE DID THE JOB.".format(FILE))
                BOOLEAN = True
#----------------------------------------------------------------------------------------------------|
            if INPUT == "REMOVE" or INPUT == "3":
                CHECK = input("\nARE YOU SURE? (Y/N): ")
                if CHECK == "Y" or "YES":
                    try:
                        os.remove(FILE)
                    except:
                        os.rmdir(FILE)
                else:
                    if CHECK == "N" or "NO":
                        print("\nOK")
                    else:
                        print("\nWRONG INPUT !")
                BOOLEAN = True
#----------------------------------------------------------------------------------------------------|
            if BOOLEAN:
                print("\nCOMPLETED.")
                continue
            else:
                print("\nWRONG INPUT !")
                continue
        except:
            print("\nERROR !")
            continue
    if INPUT == "HELP" or INPUT == "11":
        print("""
|_____________________|COMMANDS|_____________________|
|ENTER '00' OR 'FILES' TO SHOW FILES.                |
|ENTER '01' OR 'LOWER' TO LOWERCASE ALL FILES.       |
|ENTER '02' OR 'UPPER' TO UPPERCASE ALL FILES.       |
|ENTER '03' OR 'REMOVE' TO REMOVE ALL FILES.         |
|ENTER '04' OR 'ADD' TO ADD A TEXT TO FILENAMES.     |
|ENTER '05' OR 'SORT' TO SORT THE FOLDER.            |
|ENTER '06' OR 'SORT FF' TO SORT FILES WITH FOLDERS. |
|ENTER '07' OR 'SORT FOLDER' TO SORT FOLDERS.        |
|ENTER '08' OR 'UPPER FOLDERS' TO UPPERCASE 2 FOLDER.|
|ENTER '09' OR 'CLEAR' TO CLEAR THE SHELL.           |
|ENTER '10' OR 'SELECT' TO SELECT A FILE.            |  
|ENTER '11' OR 'HELP' TO SHOW THE HELP COMMAND AGAIN.|
|ENTER '12' OR 'EXIT' FOR EXIT OF THIS PROGRAM. :)   |
|____________________________________________________|""")
    else:
        if INPUT == "EXIT" or INPUT == "12": 
            pass
        else:
            print("\nWRONG INPUT ! ENTER 'HELP' OR '11' TO SHOW COMMANDS.")
#----------------------------------------------------------------------------------------------------|
print("\nBYE :)\n")