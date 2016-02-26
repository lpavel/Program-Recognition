from __future__ import print_function
import os

class CacheParser:
    def __init__(self, fileNameTrace, fileNameOut):
        self.fileNameOut = fileNameOut
        self.fileNameIn = fileNameTrace
        
    def parse(self):
        print("printing file: " , self.fileNameOut)
        content = []
        with open(self.fileNameIn, "r") as f:
            content = f.readlines()
            
        with open(self.fileNameOut, 'w') as outFile:
            for line in content:
                cache  = ''
                isRead = True
                isHit  = True
                isMiss = True
                if 'icache' in line:
                    cache = 'icache'
                else:
                    cache = 'dcache'

                if 'Read' in line:
                    isRead = True
                else:
                    isRead = False

                if 'hit' in line:
                    isHit = True
                else:
                    isHit = False
    
                if 'miss' in line:
                    isMiss = True
                else:
                    isMiss = False
                    
                if isMiss == False and isHit == False:
                   continue
               
                splitStr = line.split(":")
                time = splitStr[0]
                 
                print(time + ' ' + cache + ' ' + str(isRead) +
                      ' ' +  str(isHit), # leave only hit because of memory constr
                      file=outFile)
        os.remove(self.fileNameIn)
