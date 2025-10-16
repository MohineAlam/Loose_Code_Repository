########### This code demonstrate python used for different applications in molecular biology, sorting through data ############

from zlib import Z_FULL_FLUSH


first_10_bp = 'gggtgcgacg'
second_10_bp = "attcattgtt"
gene = first_10_bp + second_10_bp

print('The first 20 bp of BRAC2 gene are', gene)

print("%15s %10s %10s" % ("Amino acid", "1-letter", "codon"))
# print('format' % (values))

# get your sequence here
ncbi_sequence = input('Enter your NCBI sequence number here:')
print(ncbi_sequence)
print('Your NCBI sequence number is:', ncbi_sequence)

starting_index = input('Please type a starting index here:')
print(starting_index)
ending_index = input('Please type an ending index here:')
print(ending_index)
print('I will compute the number of bps in this region...')

number_of_bps = int(starting_index) - int(ending_index)
print('The number of bps are:', number_of_bps)
#


#

Restriction_enzymes = { 'EcoRI': 'gaattc', 'AluI': 'AGCT','NotI':'GCGGCCGC', 'TaqI':'TCGA'

}

print(Restriction_enzymes)
print()

keys = list(Restriction_enzymes.keys())
print('Keys as a list:', keys)

#string manipulation: length

zika_DNA = 'AGTTGTTGATCT'
zika_DNA_length = len(zika_DNA)
print('The first', zika_DNA_length, 'nucleotides','of Zika virus DNA are', zika_DNA)

# ifELse statements

DNA_segment = 'ATGACATGA'
codon_1 = DNA_segment[0:3]
if(codon_1 == 'ATG'):
    print('Codon', codon_1, 'is a start codon.')
else:
    print('Codon', codon_1, 'is not a start codon.')
print('Done!')

# Translate
# change sequence into input() for user to use any DNA seq

zika_DNA_sequence = 'AGTTGTTGATCTGTGTGAATCAG'
print("Direct strand:       5' ", zika_DNA_sequence, " 3' ")

complements = zika_DNA_sequence.maketrans('acgtACGT','tgcaTGCA') #maketrans maps each characters in the intab string to into characters as the same position as the outab string
complements_seq = zika_DNA_sequence.translate(complements) #returns copy of the string that has been translated using a table (maketrans function)

bonds = " "*25 + "|"*len(zika_DNA_sequence)
print(bonds)

print("complementary strand: 3' " + complements_seq +"  5'")
print(len(zika_DNA_sequence))

#slice (reverse)

human_mitochondria = 'TTCTTTCATGGGGAAGCAGATTTGGGTACCACCCAAGTATTGACTTACCCATCAACAACCGCTATGTATT'
print('Human D-loop:', human_mitochondria)

my_codon = 'CAT'

index_mycodon = human_mitochondria.find(my_codon)
print('First', my_codon, 'index :', index_mycodon)

first_codon = human_mitochondria[index_mycodon + 3: index_mycodon + 6]
print('First codon after', my_codon, ':', first_codon)

second_codon = human_mitochondria[index_mycodon + 6 : index_mycodon + 9]
print('Second codon after', my_codon, ':', second_codon)

next_to_last_codon = human_mitochondria[-6:-3]
print('next to last codon:', next_to_last_codon)

last_codon = human_mitochondria[-3:]
print(last_codon)

# Find

Troglodyte_mitochondria = 'GTACCACCTAAGTACTGGCTCATTCATTACAACCGGTATGTACTTCGTACATTACTGCCAGTCACCATGA'
print('Troglodyte D-loop:', Troglodyte_mitochondria)

codon = 'CAT'

is_in = codon in Troglodyte_mitochondria
print('Is codon', codon, 'in Troglodyte mitochondrial DNA?', is_in)

how_many = Troglodyte_mitochondria.count(codon)
print('How many times does', codon, 'appear in the Troglodyte mitochondrial DNA? :', how_many, 'times')

first_index = Troglodyte_mitochondria.find(codon)
print('first', codon, 'index :', first_index)

second_index = Troglodyte_mitochondria.find(codon, first_index + len(codon))
print('Second', codon, 'index :', second_index)

third_index = Troglodyte_mitochondria.find(codon, 27, 55)
print('Third', codon, 'index:', third_index)

last_index = Troglodyte_mitochondria.rfind(codon)
print('Last', codon, 'index:', last_index)

# Concatenation
GFP_seq = 'MSKGEELFTG...HGMDELYK'
print('Green fluorescent sequence:', GFP_seq)

M_codon = 'AUG'
S_codon = 'UCA'
K_codon = 'AAA'
G_codon = 'GGU'

RNA_seq = M_codon
RNA_seq = RNA_seq + S_codon
print('RNA sequence:',RNA_seq)

RNA_seq = RNA_seq + K_codon + G_codon
print(RNA_seq, 'could code amino acid sequence:',GFP_seq)

# Tuple
Histidine = ('H','CAC','CAT')
Lysine = ('K','AAA','AAG')
Arginine = ('R', 'CGT', 'CGC', 'CGA', 'CGG', 'AGA')

print('Histidine:',Histidine)
print('Lysine:',Lysine)
print('Arginine:',Arginine)

basic = [Histidine, Lysine]
basic.append(Arginine)
print('Basic amino acids:', basic)

His = basic[0]
print('His:', His)

His_codons = basic[0][1:]
print('His codons:', His_codons)

His_codon_1 = basic[0][1]
Lysine_codon_2 = basic[1][2]

print('Lysine codon 2:', Lysine_codon_2)
print('Histidine codon 1:', His_codon_1)

codon1, codon2 = His_codons
print('Histidine codon 1:', codon1,'.'' Histidine codon 2:', codon2) #another way to select data in the tuple - e.g. different ways to call histidine codon

Amino_acid_seq = basic[0][0] + basic[1][0] + basic[2][0]
print('Amino acid sequence:', Amino_acid_seq)

# Reverse

Zika_DNA = 'AGTTGTTGATCTGTGTGAAT'
print('Forwards Zika segment\t\t:', Zika_DNA)

Reversed_Zika_DNA = Zika_DNA[::-1]
print('Reverse Zika segment\t\t:', Reversed_Zika_DNA)

# Replace - gets rid of the spaces and numbers with whatever you assign instead
import re

Zika_DNA = '601 acatgtgtga tgccaccatg agctatgaat'
print('Original Zika DNA sequence\t:', Zika_DNA)

Zika_DNA = Zika_DNA.replace(' ','',1)
print('Replace space with nothing\t:', Zika_DNA)

Zika_DNA = Zika_DNA.replace(' ','')
print('Replace spaces with nothing\t:', Zika_DNA)

Zika_DNA = re.sub(r'[1234567890]','', Zika_DNA)
print('Replace numbers with nothing\t:', Zika_DNA)
# List


# While

Ebola_DNA_seq = 'CGGACACACAAAAAGAATGAAGGATTTTGAATCTTTATTGTGTGCGAGTAACTACGAGGAAGATTAAAGA'
print('First line of nucleotides in the Ebola DNA seq\t:', Ebola_DNA_seq)

bp = 'T'
print('Base pair:', bp)
print('Str.count() of T bases in the Ebola DNA sequence:', Ebola_DNA_seq.count(bp))

count = 0
index = 0

while index < len(Ebola_DNA_seq):
    if bp == Ebola_DNA_seq[index]:
        count += 1
    index += 1

print('Our while count:', count)

# For

bases = ['T','C','A','G']

for base in bases:
    print(base)

print('Codons starting with T:')

for second_base in bases:
    print('Codons starting with T:'+second_base)
    for third_base in bases:
        print('T'+second_base+third_base)

# Range
population = [425]
growth_rate = 0.0194
number_of_years = 30

years = range(0, number_of_years + 1, 1)
print(list(years))

#for year in years:
    #next_generation = population[year] + growth_rate*population[year]
    #population.append[next_generation]

#for year in years:
    #print('At year %2d the population is %7.3f' %(year, population[year]))

# Count with Dictionary

Thalassiosira_DNA_seq = 'gggtgcgacgattcattgttttcggacaagtggataggcaaccactaccggtggattgtc'
print('Thalassiosira DNA sequence:\t',Thalassiosira_DNA_seq)

Thalassiosira_seq_length = len(Thalassiosira_DNA_seq)
print()

Number_of_codons = int(Thalassiosira_seq_length/3)

Codon_list = []
for i in range(Number_of_codons):
    Codon_list.append(Thalassiosira_DNA_seq[i*3:i*3+3])

print('List of codons:', Codon_list)
print()

Codon_counter = {}

for codon in Codon_list:
    if codon not in Codon_counter:
        Codon_counter[codon] = 1
    else:
        Codon_counter[codon] =+ 1

print('Codon counter:')
for key, value in Codon_counter.items():
    print(key,':', value)

# ARGV

import sys

if len(sys.argv) == 1:
    print('Please provide a command line arguement!')
    sys.exit()

print('Sys.argv list:', sys.argv)
print('The first argument:', sys.argv[0])
print('The second arguement:', sys.argv[1])

#Codon_list = []
#if i in range(Number_of_codons):
# table
# python script that is querying the data base.
# rap battle

def addition(x,y):
    z = x + y
    print(z)

addition(3,9)

# input

ncbi_sequence = input('Enter your NCBI sequence number here:')
print(ncbi_sequence)
print('Your NCBI sequence number is:', ncbi_sequence)

starting_index = input('Please type a starting index here:')
print(starting_index)
ending_index = input('Please type an ending index here:')
print(ending_index)
print('I will compute the number of bps in this region...')

number_of_bps = int(starting_index) - int(ending_index)
print('The number of bps are:', number_of_bps)

#TRY/except

import sys

stop_codons = ['TAA','TAG', 'TGA']
print('stop codons:', stop_codons)

try:
    index = int(input('Please enter the index of a stop codon to print'))
    print('Your codon is:', stop_codons[index]) 
except ValueError as ve:
    print(ve, 'Try again...')
except IndexError:
    print('Your index', index, 'is out of range. Try again...')
except: 
    print('Unexpected error:', sys.exc_info()[0])
    sys.exit()
else:
    print('Good bye!')

#Function
