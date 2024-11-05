# Playing around with dictionaries

TF_motif = {'SP1': 'atgatgatg', 'NF2': 'tgtgagtc'}
TF_motif ['AP-1'] = 'tgctgcaaa'
print(TF_motif)

TF_motif['AP-1'] = 'atgtg(g/c)acg'
print(TF_motif)

del TF_motif['SP1']
print(TF_motif)

TF_motif.update({'NK-2':'atgatgcgcga', 'NF2':'tgtgagtc'})
print(TF_motif)

print(len(TF_motif))

print(list(TF_motif.keys())) # same applies to .values

# if and else statements + decision making 
# conditions are boolean expression either true or false

dna = 'atctctctctaaacacgatNcgctgc'
if 'n' in dna:
    nbases = dna.count('n')
    print ("dna sequence has %d undefined bases" % nbases)
elif 'N' in dna:
    print("dna has undefined bases")
else: 
    print ("dna has no undefined bases")

dna = 'atctctctctaaacacgnatNcgctgc' 
if 'n' or 'N' in dna: #can use and, or, not logical operators
    nbases = dna.count('n') + dna.count('N')
    print ("dna sequence has %d undefined bases" % nbases)
else: 
    print ("dna has no undefined bases")

# in and not in operators, comparision operators etc
motif = 'gtccc'
print(motif in dna )

# WHILE and FOR loops
dna_1 = 'gtagatgatgatgcccctagtcgatgcgtaaaagctgtccaa'
pos = dna_1.find('gt', 0) #position of splice donor site

while pos>-1 :
    print ("donor splice site candidate at position %d" %pos)
    pos = dna_1.find('gt', pos+1)

motifs  = ['atcttctctct', 'atg', 'ctatatata']

for m in motifs:
    print (m, len(m))

for i in range(4): #the range() function for numerical values
    print(i)

for i in range (1, 10, 2):
    print(i)

# Problem: Find if all characters in a protein sequence are valid amino acids

protein = 'SDVIHRYKUUPAKSHWGYVCJRSRFTWMVWWRFSCRA'

for i in range(len(protein)):
    if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ':
        print("protein contains invalid amino acid %s at position %d" %(protein[i], i))

protein = 'SDVIHRYKUUPAKSHWGYVCJRSRFTWMVWWRFSCRA'

for i in range(len(protein)):
    if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ':
        print('this is not a valid protein sequence')
        break #closes the nearest loop and returns a result

protein = 'SDVIHRYKUUPAKSHWGYVCJRSRFTWMVWWRFSCRA'
corrected_protein = ''
for i in range(len(protein)):
    if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ':
        continue #does not stop the loop and continues to the next line
    corrected_protein = corrected_protein + protein[i]

print("the corrected protein sequence is: %s" %corrected_protein)

# Problem: Find all prime numbers smaller than a given integer

N = 10
for y in range (2, N):
    for x in range (2, y):
        if y % x == 0:
            print(y, 'equals', x ,'*', y//x)
            break
        else:
            print(y, 'is a prime number')






