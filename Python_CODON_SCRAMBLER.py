import random

# Synonymous codons specific to Homo sapiens
synonymous_codons_human = {
    'TTT': ['TTT', 'TTC'],
    'TTC': ['TTT', 'TTC'],
    'TTA': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'TTG': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'CTT': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'CTC': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'CTA': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'CTG': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'TCT': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'TCC': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'TCA': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'TCG': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'AGT': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'AGC': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'TAT': ['TAT', 'TAC'],
    'TAC': ['TAT', 'TAC'],
    'TAA': ['TAA', 'TAG', 'TGA'],
    'TAG': ['TAA', 'TAG', 'TGA'],
    'TGA': ['TAA', 'TAG', 'TGA'],
    'TGT': ['TGT', 'TGC'],
    'TGC': ['TGT', 'TGC'],
    'TGG': ['TGG'],
    'CCT': ['CCT', 'CCC', 'CCA', 'CCG'],
    'CCC': ['CCT', 'CCC', 'CCA', 'CCG'],
    'CCA': ['CCT', 'CCC', 'CCA', 'CCG'],
    'CCG': ['CCT', 'CCC', 'CCA', 'CCG'],
    'CAT': ['CAT', 'CAC'],
    'CAC': ['CAT', 'CAC'],
    'CAA': ['CAA', 'CAG'],
    'CAG': ['CAA', 'CAG'],
    'CGT': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'CGC': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'CGA': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'CGG': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'AGA': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'AGG': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'ATT': ['ATT', 'ATC', 'ATA'],
    'ATC': ['ATT', 'ATC', 'ATA'],
    'ATA': ['ATT', 'ATC', 'ATA'],
    'ATG': ['ATG'],
    'ACT': ['ACT', 'ACC', 'ACA', 'ACG'],
    'ACC': ['ACT', 'ACC', 'ACA', 'ACG'],
    'ACA': ['ACT', 'ACC', 'ACA', 'ACG'],
    'ACG': ['ACT', 'ACC', 'ACA', 'ACG'],
    'AAT': ['AAT', 'AAC'],
    'AAC': ['AAT', 'AAC'],
    'AAA': ['AAA', 'AAG'],
    'AAG': ['AAA', 'AAG'],
    'GTT': ['GTT', 'GTC', 'GTA', 'GTG'],
    'GTC': ['GTT', 'GTC', 'GTA', 'GTG'],
    'GTA': ['GTT', 'GTC', 'GTA', 'GTG'],
    'GTG': ['GTT', 'GTC', 'GTA', 'GTG'],
    'GCT': ['GCT', 'GCC', 'GCA', 'GCG'],
    'GCC': ['GCT', 'GCC', 'GCA', 'GCG'],
    'GCA': ['GCT', 'GCC', 'GCA', 'GCG'],
    'GCG': ['GCT', 'GCC', 'GCA', 'GCG'],
    'GAT': ['GAT', 'GAC'],
    'GAC': ['GAT', 'GAC'],
    'GAA': ['GAA', 'GAG'],
    'GAG': ['GAA', 'GAG'],
    'GGT': ['GGT', 'GGC', 'GGA', 'GGG'],
    'GGC': ['GGT', 'GGC', 'GGA', 'GGG'],
    'GGA': ['GGT', 'GGC', 'GGA', 'GGG'],
    'GGG': ['GGT', 'GGC', 'GGA', 'GGG']
}

def random_synonymous_codon(codon):
    if codon in synonymous_codons_human:
        synonymous_group = synonymous_codons_human[codon]
        return random.choice(synonymous_group)
    else:
        return codon

def generate_random_synonymous_sequence(sequence):
    random_synonymous_sequence = ""
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        random_synonymous_codon_result = random_synonymous_codon(codon)  # Rename variable to avoid conflict
        random_synonymous_sequence += random_synonymous_codon_result
    return random_synonymous_sequence

# User input sequence
input_sequence = input("Enter a sequence of codons: ").upper()
random_synonymous_sequence = generate_random_synonymous_sequence(input_sequence)
print("Generated random synonymous sequence:")
print(random_synonymous_sequence)
