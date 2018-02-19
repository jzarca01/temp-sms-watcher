import sys, getopt, time, datetime, os
from numberGen import smsreceivefree

global pattern, timeRange
pattern = ''
timeRange = 120

def usage():
  print '\nUsage: \n'
  print 'python '+sys.argv[0]+' --country=usa|canada|united-kingdom fetches a temporary number for specified country'
  print 'python '+sys.argv[0]+' --check=243840389473 watches the given number for incoming sms\n\n'

def main():
    try:                                
        opts, args = getopt.getopt(sys.argv[1:], "hcC", ["help", "country=", "check="])
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)                  
    for opt, arg in opts:
        m = smsreceivefree.generator()
        if opt in ("-c", "--country"):
            m.country = arg
            if not arg:
                m.country = "united-kingdom"
                print "united-kingdom set as default, other options: are usa|canada|united-kingdom"
            number, countryCode = m.getNumber(m.country)
            print countryCode, number
        elif opt in ("-C", "--check"):
            if not arg:
                print "no number given"
                exit()
            else:
                m.number = arg
                m.path = "info/{0}".format(m.number)
                os.system('cls' if os.name == 'nt' else 'clear')
                try:
                    while True:
                        now = datetime.datetime.now()
                        print "Messages to {0} @ {1}\n".format(m.number, now.strftime("%Y-%m-%d %H:%M"))
                        print m.checkSMS(pattern)
                        print("\n")
                        time.sleep(timeRange)
                except KeyboardInterrupt:
                    print('\n\nKeyboard exception received. Exiting.')
                    exit()
        elif opt in ("-h", "--help"):
            usage()
            exit()

if __name__ == "__main__":
  main()
