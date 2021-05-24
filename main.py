import os
import PyPDF2
from colorama import Fore, init

# Global variables

# -------------
fileName = ""
strPDF = ""
dirName = ""
# -------------


# Init colorama
init()
# -------------

# Get the input from user
def getInputUser():
    # Read an write Global var
    global fileName
    global dirName

    strSplit = ""
    dirName = "output_folder_txt"

    # Print input
    print(Fore.GREEN + "[!] Insert path to PDF file:" + Fore.RESET)
    inputUser = input()
    # -------------
    if(inputUser == "" or len(inputUser.split("\\"))  == 1):
        print(Fore.RED + "Please put a valid PATH to a file" + Fore.RESET)
    else:
        # Split to get the name of the file, remove its extension and print it
        strSplit = inputUser.split("\\")
        strSplit = strSplit[len(strSplit)-1].split(".")
        fileName = strSplit[len(strSplit)-2]
        print(Fore.GREEN + f"[!] This is the name of the file: {fileName}" + Fore.RESET)

    # Open PDF file
    pdfObj = open(inputUser, "rb")

    # Create output folder if don't exists
    try:
        os.makedirs(dirName)
        print(Fore.GREEN + "[!] Directory " , dirName ,  " Created"+ Fore.RESET)
    except FileExistsError:
        print(Fore.RED + "Directory " , dirName ,  " already exists" + Fore.RESET)


    # call to fun getFilePdf
    initRead(pdfObj)
# -------------

# Read pdf Object
def initRead(strFile):
    # Read an write Global var
    global strPDF
    strPDF = ""

# Reading pdf
    print(Fore.YELLOW + "Reading PDF file" + Fore.RESET)
    pdfobj = PyPDF2.PdfFileReader(strFile)
    print(Fore.GREEN + "READING COMPLETE" + Fore.RESET)


    print(Fore.YELLOW + "Extracting Text"+ Fore.RESET)
    for x in range(pdfobj.numPages):
        strPDF += str(pdfobj.getPage(x).extractText())

    # Call to fun to write the file
    writeFile()

def writeFile():
    file = open(f"{dirName}/{fileName}.txt", "w")
    file.write(strPDF)
    file.close()

getInputUser()