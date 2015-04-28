import atexit
import functools
from time import clock

def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % \
        functools.reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],
            [(t*1000,),1000,60,60])

line = "="*40
def log(s, outputFile):
    print(line)
    outputFile.write(line+'\n')
    print("{0} - {1}".format(secondsToStr(clock()), s))
    outputFile.write("{0} - {1}\n".format(secondsToStr(clock()), s))
    print(line)
    outputFile.write(line+'\n')
    outputFile.flush()
    print ("\n")

def endlog():
    end = clock()
    elapsed = end-start
    '''log("End Program -- {0}".format(secondsToStr(elapsed)), None)'''

def now():
    return secondsToStr(clock())

start = clock()
atexit.register(endlog)

        