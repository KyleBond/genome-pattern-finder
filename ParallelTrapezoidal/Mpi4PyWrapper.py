import sys
from mpi4py import MPI
import numpy

'''
Created on Jul 6, 2013

@author: kyle
'''

integral = numpy.zeros(1)

comm = MPI.COMM_WORLD

print("Hello! I'm rank %d from %d running in total, name %s..." % (comm.rank, comm.size, MPI.Get_processor_name()))

comm.Barrier()   # wait for everybody to synchronize _here_
