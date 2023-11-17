import sys
import os
from DNAToolkit import Basic

#RNA codons --> amino acids.
#Amino acids connect together to make proteins.
CodonTable = {'UUU': 'F',
              'UUC': 'F',
              'UUA': 'L',
              'UUG': 'L',
              'UCU': 'S',
              'UCC': 'S',
              'UCA': 'S',
              'UCG': 'S',
              'UAU': 'Y',
              'UAC': 'Y',
              'UAA': 'STOP',
              'UAG': 'STOP',
              'UGU': 'C',
              'UGC': 'C',
              'UGA': 'STOP',
              'UGG': 'W',
              'CUU': 'L',
              'CUC': 'L',
              'CUA': 'L',
              'CUG': 'L',
              'CCU': 'P',
              'CCC': 'P',
              'CCA': 'P',
              'CCG': 'P',
              'CAU': 'H',
              'CAC': 'H',
              'CAA': 'Q',
              'CAG': 'Q',
              'CGU': 'R',
              'CGC': 'R',
              'CGA': 'R',
              'CGG': 'R',
              'AUU': 'I',
              'AUC': 'I',
              'AUA': 'I',
              'AUG': 'M',
              'ACU': 'T',
              'ACC': 'T',
              'ACA': 'T',
              'ACG': 'T',
              'AAU': 'N',
              'AAC': 'N',
              'AAA': 'K',
              'AAG': 'K',
              'AGU': 'S',
              'AGC': 'S',
              'AGA': 'R',
              'AGG': 'R',
              'GUU': 'V',
              'GUC': 'V',
              'GUA': 'V',
              'GUG': 'V',
              'GCU': 'A',
              'GCC': 'A',
              'GCA': 'A',
              'GCG': 'A',
              'GAU': 'D',
              'GAC': 'D',
              'GAA': 'E',
              'GAG': 'E',
              'GGU': 'G',
              'GGC': 'G',
              'GGA': 'G',
              'GGG': 'G'
              }


if __name__ == "__main__":    
    
    f = open("exercises/rosalind_prot.txt", mode='r')
    string = f.read().split('\n')[0]

    #check if the input string is divisible by 3
    #print(len(string)%3==0)

    output = ""
    for i in range(0, len(string), 3):
        codon = CodonTable[string[i:i+3]]
        if codon != 'STOP':
            output = output + ''.join(CodonTable[string[i:i+3]])
    
    print(output)
            
    

    f.close()