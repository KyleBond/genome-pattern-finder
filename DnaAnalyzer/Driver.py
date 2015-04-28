'''
Created on Jul 6, 2013

@author: kyle
'''
import sys
from mpi4py import MPI
import MasterNode
import SlaveNode



    

def main():
    logFileName = sys.argv[3]
    csvMatches = sys.argv[4] 
    inputFile = sys.argv[1]
    baseCount = int(sys.argv[2])
    
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    mpisize = comm.Get_size()
    name = MPI.Get_processor_name()
    
    if rank == 0 and mpisize > 1:
        MasterNode.startMasterNode(comm, logFileName, csvMatches)
    elif rank == 0 and mpisize == 1:
        print("This application requires a minimum of two processes to run.")
    else:
        SlaveNode.startSlaveNode(comm, rank, mpisize, name, inputFile, baseCount)
    
if __name__ == '__main__':
    main()