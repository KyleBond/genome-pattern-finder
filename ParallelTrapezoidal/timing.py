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
    outputFile.write(line)
    print(secondsToStr(clock()), '-', s)
    outputFile.write(secondsToStr(clock()), '-', s)
    print(line)
    outputFile.write(line)
    print()

def endlog():
    end = clock()
    elapsed = end-start
    log("End Program", secondsToStr(elapsed))

def now():
    return secondsToStr(clock())

start = clock()
atexit.register(endlog)

        