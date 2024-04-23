<<<<<<< HEAD
# define function to convert codons into amino acids using key above

def codon_to_aa(sequence, codons_to_aa):
    amino_acid_sequence = ""
    for base in range(0,len(sequence),3):
            codon = sequence[base:base+3]
            for aa, codon_list in codons_to_aa.items():
                  if codon in codon_list:
                        amino_acid_sequence += aa
                        break
    return amino_acid_sequence

=======
>>>>>>> 93d2792f891c6aee0077df20890ba7bd10b0465c
codons_to_aa = {
    'F': ['TTT', 'TTC'],
    'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Y': ['TAT', 'TAC'],
    '*': ['TAA', 'TAG', 'TGA'],
    'C': ['TGT', 'TGC'],
    'W': ['TGG'],
    'P': ['CCT', 'CCC', 'CCA', 'CCG'],
    'H': ['CAT', 'CAC'],
    'Q': ['CAA', 'CAG'],
    'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'I': ['ATT', 'ATC', 'ATA'],
    'M': ['ATG'],
    'T': ['ACT', 'ACC', 'ACA', 'ACG'],
    'N': ['AAT', 'AAC'],
    'K': ['AAA', 'AAG'],
    'V': ['GTT', 'GTC', 'GTA', 'GTG'],
    'A': ['GCT', 'GCC', 'GCA', 'GCG'],
    'D': ['GAT', 'GAC'],
    'E': ['GAA', 'GAG'],
    'G': ['GGT', 'GGC', 'GGA', 'GGG']
}

<<<<<<< HEAD
# your sequence (replace with path)
sequence = ""
=======
# define function to convert codons into amino acids using key above

def codon_to_aa(sequence, codons_to_aa):
    amino_acid_sequence = ""
    for base in range(0,len(sequence),3):
            codon = sequence[base:base+3]
            for aa, codon_list in codons_to_aa.items():
                  if codon in codon_list:
                        amino_acid_sequence += aa
                        break
    return amino_acid_sequence

# your sequence (replace with path)
sequence = "CACATGTACTATAATATGAATAGCACTCCCGGTCGTTGTTCCTTAGGATACCGGCGAGGTTTCCAA"
>>>>>>> 93d2792f891c6aee0077df20890ba7bd10b0465c

# call function
amino_acid_sequence = codon_to_aa(sequence,codons_to_aa)

# write the amino acid sequence into a text file
with open("AMINO_ACID.txt", "w") as file:
      file.write(amino_acid_sequence)

print("Your amino acid sequence is:", amino_acid_sequence[:12],"...")
print("Your complete amino acid sequence has been stored as AMINO_ACID.txt")