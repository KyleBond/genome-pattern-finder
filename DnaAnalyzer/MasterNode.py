'''
Created on Jul 7, 2013

@author: kyle
'''
import timing
from mpi4py.MPI import ANY_SOURCE

import numpy
from datetime import datetime

def prepareCsvMatchFile(csvMatches):
    open(csvMatches, 'w').close()
    csvMatchFile = open(csvMatches, 'a')
    csvMatchFile.write("cpuName,rank,dnaPattern,pattern#,match#,startIndex,endIndex")
    csvMatchFile.flush()
    return csvMatchFile

def prepareLogFile(outputFileName):
    open(outputFileName,'w').close()
    outputFile = open(outputFileName,'a')
    outputFile.write("DNA Analysis -- Started on {0}\n\n".format(datetime.now))
    return outputFile

def recordFeedback(recv_buffer, outputFile):
    createOutput(recv_buffer, outputFile)

def recordMatch(recv_buffer, csvMatches):
    
    output = recv_buffer
    csvMatches.write(output)
    csvMatches.flush() 
    
    
def receiveSlaveFeedback(comm, outputFile, csvMatchFile):
    slavesFinished = 0
    while slavesFinished < 4:
        print("Waiting...")
        recv_buffer = numpy.zeros(3000, dtype=numpy.dtype(str))
        comm.recv(recv_buffer, mpi4py.MPI.ANY_SOURCE)
        
        firstedit = ''.join(recv_buffer).strip()
        case = firstedit[4:(len(firstedit)-3)]
        
        if case.startswith("Feedback"):
            recordFeedback(case,outputFile)
        elif case.startswith("WorkComplete"):
            slavesFinished += 1
        elif case.startswith("Match"):
            recordMatch(case, csvMatchFile)

def createOutput(text,outputFile):
    timing.log(text, outputFile)

def startMasterNode(comm, outputFileName, csvMatches):
    outputFile = prepareLogFile(outputFileName)
    createOutput("Start Program", outputFile)
    csvMatchFile = prepareCsvMatchFile(csvMatches)
    receiveSlaveFeedback(comm, outputFile, csvMatchFile)
    