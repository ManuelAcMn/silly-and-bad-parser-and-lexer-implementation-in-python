import lexers
from io import TextIOWrapper

global fileName
global fileTotalN

line = 0

def getFile(files):
    fileName = files
    line = 0
    fileTotalN = lexers.getTotalLines(files)

    with open(fileName) as fil:
        while line != fileTotalN:
            tx = fil.readline()
            if tx.endswith("\n"):
                tx = tx.replace("\n", "")
            lexers.processLine(tx)
            line+=1
        fil.close()