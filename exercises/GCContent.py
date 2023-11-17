import sys
import os
from DNAToolkit import Basic


if __name__ == "__main__":
    #use newline here to delimit by '>', a character used in FASTA format
    
    
    f = open("problems/rosalind_gc.txt", mode='r')
    string = f.read()

    #split on the line delimiter '>', also chop off the leading blank space
    lines =  string.split('>')[1:]
    #make a dictionary to store the joined sequence segments
    sequences = {}
    for i in lines:
        #split on newline to get each chunk of the DNA sequence
        temp = i.split('\n')
        #make a dictionary entry with ID as key and sequence as value
        sequences[str(temp[0])] = ''.join(temp[1:])

    max = 0
    maxSeq = ""
    for seq in sequences.keys():
        val = gcContent(sequences.get(seq))
        if val > max:
            max = val
            maxSeq = seq
        
    print(maxSeq)
    print("{:.6f}".format(max))
    
            
    

    f.close()