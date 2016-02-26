from subprocess import call
from subprocess import check_call
from subprocess import check_output
from CacheParser import CacheParser
from Simulation import Simulation
import random

if __name__ == '__main__':
    random.seed()
    l1d_size = '64kB'
    l1i_size = '64kB'
    l2_size  = '256kB'
    l3_size  = '2MB'
    l1d_assoc = '8'
    l1i_assoc = '8'
    l2_assoc  = '16'
    l3_assoc  = '16'
    cacheline_size = '64'

    properties = (l1d_size, l1i_size, l2_size, l3_size,
                  l1d_assoc, l1i_assoc, l2_assoc, l3_assoc, cacheline_size)


    simulationsList = []
    totalSim = 30
    for i in range(totalSim):
        if i < (totalSim/3):
            simulation = Simulation("matrixMult", "ARM", properties)
            simulationsList.append((simulation, "mm", i))
        elif i < 2*totalSim/3:
            simulation = Simulation("simon", "ARM", properties)
            simulationsList.append((simulation, "simon", i % (totalSim/3)))
        else:
            simulation = Simulation("binarySearch", "ARM", properties)
            simulationsList.append((simulation, "binarySearch", i % (totalSim/3)))

            
    for (simulation, program, counter) in simulationsList:
        filename = program + str(counter)
        filenameTrace = '/home/lpavel/gem5-stable/m5out/' + filename + 'Trace.txt'
        filenameOut = '/home/lpavel/gem5-stable/m5out/' + filename + 'Output.txt' 
        simulation.run(filenameTrace)
        #after simulation runs, parse the output form stats.txt
        parser = CacheParser(filenameTrace, filenameOut)
        parser.parse()
