# Basic DNA Analysis 
# Author: William(Willow) Ament
# Date 9/21/2023
# I'm starting to work on some bioinformatics to break out of this depression I've been in.
# I'm using rebelScience's bioinfomatics course on youtube as a guide for some specialized problems.

# I also need to refresh myself before I get a job. 

import collections

# Base Pairs for DNA    A <-> T  |  C <-> G
Nucleotides = ["A", "C", "G", "T"]

NucComplement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

#dna_seq is a dirty input, 
# we want to validate that it's a real DNA seq
def validateSeq(dna_seq):
    """Checks for invalid characters in the DNA sequence.

    Args:
        dna_seq (string): A string of characters A,C,G,T 

    Returns:
        _type_: _description_
    """
    seq = dna_seq.upper()
    for nuc in seq:
        if nuc not in Nucleotides:
            print("\nThe sequence contains an invalid char{} ",nuc)
            return False
    print("Valid Sequence")
    return seq

def countNuc(seq):
    return dict(collections.Counter(seq))

def invertDNA(seq):
    return seq.reverse()

def DNAtranscription(seq):
    return seq.replace("T","U")