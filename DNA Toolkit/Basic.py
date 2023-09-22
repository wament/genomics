# Basic DNA Analysis 
# Author: William(Willow) Ament
# Date 9/21/2023
# I'm starting to work on some bioinformatics to break out of this depression I've been in.
# I'm using rebelScience's bioinfomatics course on youtube as a guide for some specialized problems.

# I also need to refresh myself before I get a job. 

import collections

# Base Pairs for DNA    A <-> T  |  C <-> G
Nucleotides = ["A", "C", "G", "T"]

#dna_seq is a dirty input, 
# we want to validate that it's a real DNA seq
def validateSeq(dna_seq):
    seq = dna_seq.upper()
    for nuc in seq:
        if nuc not in Nucleotides:
            print("\nThe sequence contains an invalid char{} ",nuc)
            return False
    return seq

def countNuc(seq):
    counts = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        counts[nuc]+=1
    return counts
    #return dict(collections.Counter(seq))