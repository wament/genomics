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
        string: Valid or Invalid
    """
    seq = dna_seq.upper()
    for nuc in seq:
        if nuc not in Nucleotides:
            print("\nThe sequence contains an invalid char{} ",nuc)
            return False
    return seq

def countNuc(seq):
    dict = {"A":0, "C":0, "G":0, "T":0}
    for nuc in seq:
        dict[nuc] +=1
    return dict
    #return dict(collections.Counter(seq))

def revComplementDNA(seq):
    """Find the reverse complement of an input sequence

    Args:
        seq (string): Input DNA sequence A,C,G,T
    Returns:
        string: complementary DNA transcription
    """
    
    #very cute piece of code here. Start with an empty string literal "".
    # .join on it and use a list literal and reference the NucComp dict
    # then [::-1] will reverse the string after the join is finished
    return "".join([NucComplement[nuc] for nuc in seq])[::-1]
    


def DNAtranscription(seq):
    """Generates a complementary RNA sequence from a DNA sequence input

    Args:
        dna_seq (string): A string of characters A,C,G,T 

    Returns:
        string: complementary RNA transcription
    """
    return seq.replace("T", "U")

def gcContent(seq):
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)

def gcContentSubset(seq, k):
    res = []
    
    
    for i in range(0, len(seq) - k + 1, k):
        subset = seq[i:i+k]
        res.append(gcContent(subset))

    if len(seq) % k != 0:
        reverse_seq = seq[::-1]
        rest_seq = reverse_seq[0 : (len(seq)%k)]
        res.append(gcContent(rest_seq))
    return res

