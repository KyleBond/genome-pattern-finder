import timing
import sys
'''
Created on Jul 6, 2013

@author: kyle
'''
def run(upperBound):

    numList = list(upperBound * [True])
    
    numList[0] = False;
    numList[1] = False;
    
    for (i, isprime) in enumerate(numList):
        if isprime:
            
            for n in range(i*i, upperBound, i):
                numList[n] = False
    
    
    primeList = [i for i, x in enumerate(numList) if x == True]

    timing.log("Prime List Completed")
    
    count = len(primeList) + 4
#     for i in range(0, count//5):
#         
#         if not primeList:
#             item0 = 'xxx'
#         else:
#             item0 = primeList.pop(0)
#         
#         if not primeList:
#             item1 = 'xxx'
#         else:
#             item1 = primeList.pop(0)
#         
#         if not primeList:
#             item2 = 'xxx'
#         else:
#             item2 = primeList.pop(0)
#         
#         if not primeList:
#             item3 = 'xxx'
#         else:
#             item3 = primeList.pop(0)
#             
#         if not primeList:
#             item4 = 'xxx'
#         else:
#             item4 = primeList.pop(0)    
#             
#         print("{0}, {1}, {2}, {3}, {4}\n".format(item0, item1, item2, item3, item4))
    print("Total number of primes in range of 2 to {0} is {1}".format(upperBound, count))
    
def tryParseInt(num):
    try:
        return int(num)
    except ValueError:
        return None

if __name__ == '__main__':
    upperBound = sys.argv[1]

    if isinstance(tryParseInt(upperBound), int) and int(upperBound) > 2:
        run(int(upperBound))
    else:
        print("Proper usage: python PrimeNumGen.py <int greater than 2>")