'''
Created on Jul 7, 2013

@author: kyle
'''
import string
import numpy
from mpi4py import MPI

def sendMasterFeedback(comm, text):
    
    arrayToSend = "Feedback:{0}".format(text)
    comm.send(arrayToSend)
    

def sendMasterMatch(comm, name, rank, currentPattern, i, index, j, baseCount):
    output = "{7}::name:{0},rank:{1},currentPattern:{2},patternStartIndex{3},matchNumber:{4},matchStartIndex:{5},matchEndIndex:{6}\n".format(name, rank, currentPattern, i, index, j, (j+baseCount),"Match")
    arrayToSend = output
    comm.send(arrayToSend)
    return;

def sendMasterWorkComplete(comm):
    arrayToSend = ["WorkComplete"]
    comm.send(arrayToSend)
    
def startSlaveNode(comm, rank, mpisize, name, inputFile, baseCount):
    dnafile = open(inputFile,'r')
    dnafile.readline()
    index = 0
    currentSequence = ""
    for line in dnafile.readlines():
        if not 'N' in line:
            wholeline = str.strip(line)
            currentSequence += str(wholeline)
            
    genomeLength = len(currentSequence)
    dataSize = genomeLength//mpisize
    localstart = rank*dataSize
    localend = rank*dataSize + dataSize
    
    if rank == mpisize - 1:
        localend += (genomeLength % mpisize)
    
    i = localstart
    if(rank == 1): 
        sendMasterFeedback(comm, "Genome Length, without N: {0}".format(genomeLength))
        
    while i < localend+1:
        currentPattern = currentSequence[i:i+baseCount]
        sendMasterFeedback(comm, "{2}, rank {3}, starting sequence {0}: {1}".format(i, currentPattern, name, rank))
        j = 0
        while j < genomeLength:
            if currentSequence[j:j+baseCount] == currentPattern and j != i:
                index += 1
                output = "*** Match Found -- Name: {0}, Rank: {1} \nPattern # {2} {3}\n Number: {4}, Found at index {5} to index {6} ***".format(name, rank, currentPattern, i, index, j, (j+baseCount)) 
                sendMasterFeedback(comm,output)
                sendMasterMatch(comm, name, rank, currentPattern, i, index, j, baseCount)
                
            j += 1
        i += 1
    sendMasterWorkComplete(comm)
