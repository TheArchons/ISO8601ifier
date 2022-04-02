import sys


class get():
    def getArgs():
        try:
            if sys.argv[1] == '-h' or sys.argv[1] == '--help':  # print help
                return '-h'

            # get date and time
            date = []
            try:
                index = 1
                # get all arguments
                while True:
                    date.append(sys.argv[index])
                    index += 1
            except IndexError:
                pass

        except IndexError:
            return '-h'

    def printWelcome():
        print("welcome to isoify.py! Print -h for help.")

    def printHelp():
        print("isoify.py converts your time and date to ISO 8061 format.")
        print("-h or --help prints this message.")
        print("anything else will be interpreted as a time and date.")


def main():
    get.printWelcome()  # prints welcome message
    cmd = get.getArgs()
    if cmd == "-h" or cmd == "--help":
        get.printHelp()
    else:
        get.getDate()  # TODO make this a function


main()
