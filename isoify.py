class get():
    def printWelcome():
        print("welcome to isoify.py! Print -h for help.")
    def printHelp():
        print("isoify.py converts your time and date to ISO 8061 format.")
        print("-h or --help prints this message.")
        print("anything else will be interpreted as a time and date.")

def main():
    get.printWelcome() #prints welcome message
    cmd = get.getCmd() #TODO make this a function
    if cmd == "-h" or cmd == "--help":
        get.printHelp()
    else:
        get.getDate() #TODO make this a function
