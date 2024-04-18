import random

def find_repeated_codons(sequence):
    # Translation table for codons to amino acids
    codon_to_aa = {
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
        'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
        'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
        'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

    # Define the minimum length of repeated codons
    min_repeated_length = 3  # Adjust as needed

    repeated_regions = []

    # Iterate through the sequence
    i = 0
    while i < len(sequence):
        codon = sequence[i:i+3]  # Assuming codons are triplets
        start_index = i
        repeat_count = 1

        # Check for repeated codons
        j = i + 3
        while j < len(sequence) and sequence[j:j+3] == codon:
            repeat_count += 1
            j += 3

        # If repeated length is greater than or equal to min_repeated_length, add to repeated_regions
        if repeat_count >= min_repeated_length:
            amino_acid = codon_to_aa.get(codon, 'Unknown')
            repeated_regions.append((codon, amino_acid, start_index, repeat_count))

            # Replace the repeated codons with synonymous codons
            sequence, i = replace_repeated_codons(sequence, i, repeat_count, codon_to_aa)

        else:
            # Move to the next codon
            i = j

    return sequence, repeated_regions

def replace_repeated_codons(sequence, start_index, repeat_count, codon_to_aa):
    # Find the amino acid for the original codon
    original_codon = sequence[start_index:start_index + 3]
    amino_acid = codon_to_aa.get(original_codon)

    # Find synonymous codons for the amino acid (excluding the original codon)
    synonymous_codons = [codon for codon, aa in codon_to_aa.items() if aa == amino_acid and codon != original_codon]

    # Remove any synonymous codons that are the same as the original codon
    synonymous_codons = [codon for codon in synonymous_codons if codon != original_codon]

    # Choose a replacement codon from the synonymous codons if available, else use the original codon
    if synonymous_codons:
        replacement_codon = random.choice(synonymous_codons)
    else:
        replacement_codon = original_codon

    # Replace the repeated codons with the chosen replacement codon
    sequence = sequence[:start_index] + (replacement_codon[0] * (repeat_count // 2)) + original_codon + \
               (replacement_codon[1] * (repeat_count // 2)) + sequence[start_index + 3 * repeat_count:]

    # Adjust the index after replacing the codons
    start_index += len(original_codon)

    return sequence, start_index

# Example sequence
sequence = "ATGATGATGAGGGGTTTATGTTTTTTTTTGGCGGCGGC"

# Find repeated codons in the sequence and replace them with synonymous codons
modified_sequence, repeated_regions = find_repeated_codons(sequence)

# Print the modified sequence
print("Modified sequence:")
print(modified_sequence)

# Print the repeated regions found
if repeated_regions:
    print("\nRepeated regions found:")
    for codon, amino_acid, start_index, repeat_count in repeated_regions:
        end_index = start_index + (3 * repeat_count) - 1
        print(f"Codon: {codon}, Amino Acid: {amino_acid}, Start Index: {start_index}, End Index: {end_index}")
else:
    print("No repeated regions found.")