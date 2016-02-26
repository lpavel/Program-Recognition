from subprocess import call
from subprocess import check_call
from subprocess import check_output
import random

class Simulation:
    def __init__(self, program = None, platform = None, properties = None):
        if program == None:
            print("Need to specify the program")
        elif platform == None:
            print("Need to specify the platform")
        elif properties == None:
            print("Need to specify properties")
        else:
            if platform == "ARM":
                self.platform = 'build/ARM/gem5.opt --debug-flags=Cache configs/example/se.py'
            elif platform == "X86":
                self.platform = 'build/X86/gem5.opt --debug-flags=Cache configs/example/se.py'
            else:
                print("You have the wrong platform")    

            if program == 'simon':
                if platform == 'ARM':
                    self.program = " --cmd=programs/SimonCipher/simon"
                else:
                    self.program = " --cmd=programs/SimonCipher/simonx"

            if program == 'matrixMult':
                if platform == 'ARM':
                    self.program = " --cmd=programs/MatrixMult/matrixmult"
                else:
                    self.program = " --cmd=programs/MatrixMult/matrixmultx"

            if program == 'binarySearch':
                if platform == 'ARM':
                    self.program = " --cmd=programs/BinarySearch/binarysearch"
                else:
                    self.program = " --cmd=programs/BinarySearch/binarysearchx"

            #do something related to properties here
            self.properties = ' --cpu-type=TimingSimpleCPU';
            self.properties += ' --options=' + str(random.randrange(60000000))
            (l1d_size, l1i_size, l2_size, l3_size,
            l1d_assoc, l1i_assoc, l2_assoc,
            l3_assoc, cacheline_size) = properties
            self.properties += ' --l1d_size=' + l1d_size;
            self.properties += ' --l1i_size=' + l1i_size;
            self.properties += ' --l2_size='  + l2_size;
            self.properties += ' --l3_size='  + l3_size;
            self.properties += ' --l1d_assoc=' + l1d_assoc;
            self.properties += ' --l1i_assoc=' + l1i_assoc;
            self.properties += ' --l2_assoc='  + l2_assoc;
            self.properties += ' --l3_assoc='  + l3_assoc;
            self.properties += ' --cacheline_size='  + cacheline_size;
            self.properties += ' --caches'


    def run(self, filenameTrace):
        bashGem5Dir = 'cd ~/gem5-stable/' 
        bashString = self.platform + self.program + self.properties
        print(bashString)
        with open(filenameTrace, 'w') as outFile:
            check_call(bashGem5Dir + ' && ' + bashString, shell=True,
                       stdout=outFile)

