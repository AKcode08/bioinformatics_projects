# Functions
#GC percentage

def gc(dna):
    "this function computes the GC percentage of a dna sequence"
    nbases = dna.count('n')+dna.count('N')
    gcpercent = float(dna.count('c')+ dna.count('C')+ dna.count('g')
    + dna.count('G'))*100.0/(len(dna)-nbases)
    return gcpercent

print(gc('AAGTNNAGTCC'))

help(gc) #prints the string at the start of the function

#Boolean functions
#Program to check if a given DNA sequence contains an in-frame stop codon

dna_1 = 'atgagcggccggct'

def has_stop_codon(dna_1, frame=1):
    "This function checks if given dna sequence has in frame stop codon."
    stop_codon_found = False
    stop_codons = ['tga', 'tag', 'taa']
    for i in range(frame, len(dna_1), 3) :
        codon = dna_1[i:i+3].lower()
        if codon in stop_codons :
            stop_codon_found = True
            break
    return(stop_codon_found)

print(has_stop_codon(dna_1))

if (has_stop_codon(dna_1)) :
    print("input seuqnece has an in frame stop codon")
else :
    print("input sequence has no in frame stop codons")

#Reverse compliment function

dna_1 = 'atgagcggccggct'

def reverse_string(seq):
    return seq[: : -1] #empty slice and using (-1) step to start the slice from the other direction

dna_2 = reverse_string(dna_1)

def complement(dna_2):
    "Return the complementary sequence string"
    basecomplement = {'A':'T', 'C':'G', 'G':'C', 'T':'A', 'N':'N', 'a':'t', 'c':'g', 'g':'c', 't':'a', 'n':'n'}
    letters = list(dna_2) #list operation to create a list
    letters = [basecomplement[base] for base in letters] #list comprehension operation
    return ''.join(letters) #can use split method to split a string into a list -> can specify a seperator argument ()

print (complement(dna_2))
