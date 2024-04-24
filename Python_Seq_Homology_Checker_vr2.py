# find homologous sequences between two sequences
def find_matching_regions(seq1, seq2, min_match_length=10):
    matching_regions = []
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)
    
    for i in range(len_seq1 - min_match_length + 1):
        for j in range(len_seq2 - min_match_length + 1):
            match_length = 0
            while (i + match_length < len_seq1 and
                   j + match_length < len_seq2 and
                   seq1[i + match_length] == seq2[j + match_length]):
                match_length += 1
            if match_length >= min_match_length:
                matching_regions.append((i, j, match_length))
    
    return matching_regions

# Sequences
Scrambled_Sequence_1 = ""
Scrambled_Sequence_2 = ""

# Find matching regions
matching_regions = find_matching_regions(Scrambled_Sequence_1, Scrambled_Sequence_2)

# Print the results
if matching_regions:
    print("Matching Regions:")
    for region in matching_regions:
        print("Sequence 1 Start:", region[0], "Sequence 2 Start:", region[1], "Length:", region[2])
        print("Sequence 1:", Scrambled_Sequence_1[region[0]:region[0]+region[2]])
        print("Sequence 2:", Scrambled_Sequence_2[region[1]:region[1]+region[2]])
        print()
else:
    print("No matching regions found.")














