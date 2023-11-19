from io import TextIOWrapper
import parsers

keywords = set([
    'bg',
    'set',
    'bg',
    'random',
    'not',
    'say',
    'change',
    'name'
])
operators = [
    '==',
    '!=',
    '<',
    '>',
    '<=',
    '>='
]

actorNames = [
    'n',
    'p'
]

def getTotalLines(files):
    maxL = 0
    with open(files,'r')as fh:
        for lines in fh.readlines():
            maxL += 1
    return maxL

def bgProcessing(args):
    if args[1]== "set": #set
        print("sets BG called " + args[2])
    if args[1]== "show": #show
        print("shows the BG")
    if args[1]== "hide": #hide
        print("hides the BG")

def actorProcessing(args : list[str]):
    if args[1]== "say": #say
        whatsays = ""
        for i in range(len(args) - 2):
            whatsays += args[i+2] + " "
        print(args[0] + " says: " + whatsays)
        pass
def changesProcessing(args : list[str]):
    if args[1]== "name": #say
        print(args[2] + " new name is: " + args[3])
        pass

def processLine(Line : str):
    args = Line.split(' ')
    if args[0].lower() == "bg":
        bgProcessing(args)
    if args[0].lower() == "change":
        changesProcessing(args)
    if args[0] in actorNames:
        actorProcessing(args)