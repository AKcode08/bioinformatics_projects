# DNA toolset/Code testing file

# from CountingNucP1 import DNAstring

from DNAtoolkit import *
import random
from utilities import colored

# Creating a random DNA sequence for testing:
rndDNAStr = ''.join([random.choice(Nucleotides)
                    for nuc in range(20)])
                
DNAStr = validateSeq(rndDNAStr)
print(DNAStr)

# Count Nucleotide Freq
print(countNucFrequency(DNAStr))

# Convert DNA->RNA (transcription)
print(transcription(DNAStr))

# print(f'\n Sequence: {DNAStr}\n')
# print(f'[1] + Sequence Length: {len(DNAStr)}\n')
# print(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n') --- gotta make all this work
# print(f'[3] + DNA/RNA Transcription: {transcription(DNAStr)}\n')

print(reverse_complement(DNAStr))

# print(f"[4] + DNA String + Reverse Complement:\n5' {DNAStr} 3'")
# print(f"    {''.join(['|' for c in range(len(DNAStr))])} ")
# print(f"3' {reverse_complement(DNAStr)} 5'\n")
