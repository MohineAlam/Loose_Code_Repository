import random

# Define the key for amino acids to codons
aa_to_codons = {
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

def aa_to_codon(sequence, aa_to_codons):
    codon_sequence = ""
    last_codon = None
    for aa in sequence:
        if aa in aa_to_codons:
            synonymous_codons = [c for c in aa_to_codons[aa] if c != last_codon]
            if synonymous_codons:
                chosen_codon = random.choice(synonymous_codons)
            else:
                chosen_codon = random.choice(aa_to_codons[aa])
            codon_sequence += chosen_codon
            last_codon = chosen_codon
        else:
            codon_sequence += "???"
            last_codon = None
    return codon_sequence

# Example amino acid sequence:
#sequences = ["LLLMMMLLL"]

file_path = ""
with open(file_path, "r") as file:
    sequences = file.readlines()

for seq in sequences:
    codon_seq = aa_to_codon(seq, aa_to_codons)
    print("Amino Acid Sequence:", seq)
    print("Codon Sequence:", codon_seq)

# Write the sequence to a text file
with open("CODON_SEQ.txt", "w") as file:
    file.write(codon_seq)

print("Sequence with replaced codons has been saved to CODON_SEQ.txt in the current folder")
