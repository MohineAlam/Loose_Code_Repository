# load packages
import csv
import os
from Bio import SeqIO

# define library 
base_sequences = {
        # left ITR
        'B':"AAAACCCCGGGGTTTT",
        'B \'':"AAAACCCCGGGGTTTTGGG",
        'C \'':"AAAACCCCGGGGTTTTAAAACCCCGGGGTTTT",
        'C':"AAAACCCCGGGGTTTTC",
        'D \'':"AAAACCCCGGGGTTTTAAAA",
        'D':"AAAACCCCGGGGTTTTTTT"
}

functioning_sequences = {}

for segment, seq in base_sequences.items():
        functioning_sequences[segment] = [seq[:i] for i in range(len(seq), 4, -1)]

# define sequence identifier function
def seq_identifier(fasta_file,output):                   
                for segment, X_seq_list, in functioning_sequences.items():
                        for X_seq in X_seq_list:
                                for i in range(len(input_sequence) - len(X_seq) + 1):
                                        sub_input_seq = input_sequence[i:i+len(X_seq)]
                                        # check if region has already been matched
                                        if X_seq == sub_input_seq and not any(covered_regions[i:i + len(X_seq)]):
                                                identified_sequence.append(ITR_seq)
                                                total_functioning_seq += 1
                                                X_segment.append(segment)
                                                identified_length.append(len(X_seq))
                                                segment_counts[segment] += 1
                                                # mark matched regions
                                                for j in range(i,i + len(X_seq)):
                                                        covered_regions[j] = True
                                                # break to avoid matches in same region with smaller ITR string
                                                break
                                                # save sequences in the .csv file
                # save the sequences as .csv file
                with open(identified_X_sequences, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows([identified_sequence,X_segment,identified_length])
                segment_count_file = os.path.join(output,"segment_counts_"+ sequence.id + ".csv")
                with open(segment_count_file, mode="a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(["Segment","Counts"])
                        for segment, count in segment_counts.items():
                                writer.writerow([segment, count])
        return identified_sequence, total_functioning_seq, X_segment, identified_length, segment_counts

# user input and call function
#input_sequence = input("Enter your contamination read here: ").strip().upper()
fasta_file = "/home/"
output="/home/"
identified_sequence, total_functioning_seq, X_segment, identified_length, segment_counts = seq_identifier(fasta_file,output)
# print results
print(f"Identified sequence: {identified_sequence}")
print(f"Total functioning sequences: {total_functioning_seq}")
print(f"X segment: {X_segment}")
print(f"Segment counts: {segment_counts}")
