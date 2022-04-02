from get import *

def main():
    printWelcome() #prints welcome message #TODO: make this a function
    cmd = getCmd() #TODO make this a function
    if cmd == "-h" or cmd == "--help":
        printHelp() #TODO make this a function
    else:
        getDate() #TODO make this a function
