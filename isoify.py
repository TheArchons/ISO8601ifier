import sys
from word2number import w2n

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

class conversion():
    def date(s):
        dates = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
        return ['date', dates[s]]


    def day(s):
        days = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}
        return ['weekday', days[s]]

    def timezone(s):
        pass  # TODO implement this

    def UTC(s):
        if '+' in s:
            s = s.split('+')[1]
        elif '-' in s:
            s = s.split('-')[1]
        else:
            return ['timezone', 0]
        
        if ':' in s:
            s = s.split(':')
            try:
                return ['timezone', int(s[0]) * 3600 + int(s[1]) * 60]
            except ValueError:
                pass
        elif '.' in s:
            s = s.split('.')
            try:
                return ['timezone', int(s[0]) * 3600 + int(s[1]) * 60]
            except ValueError:
                pass
        else:
            try:
                return ['timezone', int(s) * 3600]
            except ValueError:
                pass
        
        return ['timezone', 0]

    def year(s):
        return ['year', int(s)]   

    def month(s):
        return ['month', int(s)]

    def date(s):
        return ['date', int(s)]
    
    def time(s):
        return ['time', s]  # Do not convert to int because it may be colon seperated

def Isoify(data):
    times = {
        'dates': {'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'},
        'days': {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'},
        'timezones': {'acdt', 'acst', 'act', 'act', 'acwst', 'adt', 'aedt', 'aest', 'aet', 'aft', 'akdt', 'akst', 'almt', 'amst', 'amt', 'amt', 'anat', 'aqtt', 'art', 'ast', 'ast', 'awst', 'azost', 'azot', 'azt', 'bnt', 'biot', 'bit', 'bot', 'brst', 'brt', 'bst', 'bst', 'bst', 'btt', 'cat', 'cct', 'cdt', 'cdt', 'cest', 'cet', 'chadt', 'chast', 'chot', 'chost', 'chst', 'chut', 'cist', 'ckt', 'clst', 'clt', 'cost', 'cot', 'cst', 'cst', 'cst', 'ct', 'cvt', 'cwst', 'cxt', 'davt', 'ddut', 'dft', 'easst', 'east', 'eat', 'ect', 'ect', 'edt', 'eest', 'eet', 'egst', 'egt', 'est', 'et', 'fet', 'fjt', 'fkst', 'fkt', 'fnt', 'galt', 'gamt', 'get', 'gft', 'gilt', 'git', 'gmt', 'gst', 'gst', 'gyt', 'hdt', 'haec', 'hst', 'hkt', 'hmt', 'hovst', 'hovt', 'ict', 'idlw', 'idt', 'iot', 'irdt', 'irkt', 'irst', 'ist', 'ist', 'ist', 'jst', 'kalt', 'kgt', 'kost', 'krat', 'kst', 'lhst', 'lhst', 'lint', 'magt', 'mart', 'mawt', 'mdt', 'met', 'mest', 'mht', 'mist', 'mit', 'mmt', 'msk', 'mst', 'mst', 'mut', 'mvt', 'myt', 'nct', 'ndt', 'nft', 'novt', 'npt', 'nst', 'nt', 'nut', 'nzdt', 'nzst', 'omst', 'orat', 'pdt', 'pet', 'pett', 'pgt', 'phot', 'pht', 'phst', 'pkt', 'pmdt', 'pmst', 'pont', 'pst', 'pwt', 'pyst', 'pyt', 'ret', 'rott', 'sakt', 'samt', 'sast', 'sbt', 'sct', 'sdt', 'sgt', 'slst', 'sret', 'srt', 'sst', 'sst', 'syot', 'taht', 'tha', 'tft', 'tjt', 'tkt', 'tlt', 'tmt', 'trt', 'tot', 'tvt', 'ulast', 'ulat', 'utc', 'uyst', 'uyt', 'uzt', 'vet', 'vlat', 'volt', 'vost', 'vut', 'wakt', 'wast', 'wat', 'west', 'wet', 'wib', 'wit', 'wita', 'wgst', 'wgt', 'wst', 'yakt', 'yekt'}
    }

    output = {}
    
    for s in data:
        try:
            s = int(s)
        except ValueError:
            pass
        
        try:
            s = int(s.replace("th", "").replace("st", "").replace("nd", "").replace("rd", ""))
        except:
            pass

        try:
            s = int(w2n.word_to_num(s))
        except:
            pass

        if type(s) == str:
            s = s.lower()
            if s in times['dates']:
                out = conversion.date(s)
                output[out[0]] = out[1]
            elif s in times['days']:
                out = conversion.day(s)
                output[out[0]] = out[1]
            elif s in times['timezones']:
                out = conversion.timezone(s)
                output[out[0]] = out[1]
            elif 'UTC' in s:  # if it is a time relative to UTC
                out = conversion.UTC(s)
                output[out[0]] = out[1]
            elif ':' in s:
                isTime = input(f'Is ${s} a time? (y/n)')
                if isTime.lower() == 'y':
                    out = conversion.time(s)
                    output[out[0]] = out[1]

        elif type(s) == int:  # if it is a number
            if s > 31:
                output.append(conversion.year(s))
            elif s > 24:
                yearOrDate = input(f"Is ${str} a year or a day? (y/d) ")
                if yearOrDate == 'y':
                    out = conversion.year(s)
                    output[out[0]] = out[1]
                elif yearOrDate == 'm':
                    out = conversion.date(s)
                    output[out[0]] = out[1]
            else:
                yearOrDateOrTime = input(f"Is ${str} a year, a day, or a time? (y/d/t) ")
                if yearOrDateOrTime == 'y':
                    out = conversion.year(s)
                    output[out[0]] = out[1]
                elif yearOrDateOrTime == 'd':
                    out = conversion.date(s)
                    output[out[0]] = out[1]
                elif yearOrDateOrTime == 't':
                    out = conversion.time(s)
                    output[out[0]] = out[1]

    return output
            

def printISO(data):
    pass # TODO print in correct iso 8601 format
        

def main():
    get.printWelcome()  # prints welcome message
    cmd = get.getArgs()
    if cmd == "-h" or cmd == "--help":
        get.printHelp()
    else:
        printISO(Isoify(cmd))


main()
