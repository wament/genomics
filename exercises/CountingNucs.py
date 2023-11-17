import sys
import os
from DNAToolkit.Basic import countNuc

if __name__ == "__main__":    
    
    f = open("exercises/rosalind_ini.txt", mode='r')
    string = f.read().split('\n')[0]

    print(countNuc(string))
            
    

    f.close()