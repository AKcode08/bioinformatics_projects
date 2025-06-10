# DNA toolkit 
import collections
from Structures import *

 
# Check the sequence to make sure it is a DNA string
def validateSeq (dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq       

# Count Nucleotide Freq
def countNucFrequency(seq):
    tmpFreqDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict 
    # return dict(collections.Counter(seq))

def transcription(seq):
    # DNA --> RNA Transcription
    return seq.replace('T', 'U')

def reverse_complement(seq):
    return ''.join([DNA_ReverseCompliment[nuc] for nuc in seq])[::-1]
