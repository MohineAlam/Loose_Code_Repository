# load packages
import csv
import os
from Bio import SeqIO

# define library 
base_sequences = {
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
# define sequence identifier function
def seq_identifier(fasta_file,output):
        # separate sequences in fasta file and define variables to return and reference
        for sequence in SeqIO.parse(fasta_file, "fasta"):
                input_sequence = str(sequence.seq)
                identified_sequence = []
                total_functioning_seq = 0
                x_segment = []
                identified_length = []
                functioning_order = ["C","D\'","D","B\'","B","C","C\'"]
                covered_regions = [False] * len(input_sequence) # stop returning overlapping sequences in one region
                segment_counts = {seg: 0 for seg in base_sequences} #track occurence of each segment
                segment_order = ["X"] * len(input_sequence)
                # create file to save sequence data
                identified_x_sequences = os.path.join(output,"identified_x_seq_"+ sequence.id + ".csv")
                with open(identified_x_sequences, mode='w', newline='') as file:
                        writer = csv.writer(file)
                # loop through library and extract individual x sequences
                for segment, x_seq_list, in functioning_sequences.items():
                        for x_seq in x_seq_list:
                                for i in range(len(input_sequence) - len(x_seq) + 1):
                                        sub_input_seq = input_sequence[i:i+len(x_seq)]
                                        # check if region has already been matched
                                        if x_seq == sub_input_seq and not any(covered_regions[i:i + len(x_seq)]):
                                                identified_sequence.append(x_seq)
                                                total_functioning_seq += 1
                                                x_segment.append(segment)
                                                identified_length.append(len(x_seq))
                                                segment_counts[segment] += 1
                                                # mark matched regions
                                                for j in range(i,i + len(x_seq)):
                                                        covered_regions[j] = True
                                                        segment_order[j] = segment
                                                # break to avoid matches in same region with smaller x string
                                                break
                # save the sequences as .csv file
                with open(identified_x_sequences, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows([identified_sequence,x_segment,identified_length])
                # create file and save segment count information
                segment_count_file = os.path.join(output,"segment_counts_"+ sequence.id + ".csv")
                with open(segment_count_file, mode="a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(["Segment","Counts"])
                        for segment, count in segment_counts.items():
                                writer.writerow([segment, count])
                # remove X from segment count list
                while "X" in segment_order:
                        segment_order.remove("X")
                # remove consecutive repeats of segment list
                m = 0
                while m < len(segment_order) - 1:
                        if segment_order[m] == segment_order[m+1]:
                                del segment_order[m]
                        else:
                                m = m + 1
                # return sequence with flagged segment order in csv file with sequence id
                flagged_segment_order = os.path.join(output,"flagged_segment_order_" + sequence.id + ".csv")
                if segment_order == functioning_order:
                        with open(flagged_segment_order, mode='a', newline="") as file:
                                writer = csv.writer(file)
                                writer.writerows([segment_order])
                        print(f"FOUND!!!")
                        print(f"Full functioning segment order found in sequence: {sequence.id}")
                        print(f"Segment order: {segment_order}")
                # print results to terminal for each sequence
                print(f"Sequence ID: {sequence.id}")
                print(f"Total functioning sequences: {total_functioning_seq}")
                print(f"Segment counts: {segment_counts}")
                #print(f"Identified sequence: {identified_sequence}")
                #print(f"x segment: {x_segment}")
                print("-" * 40)
        return identified_sequence, total_functioning_seq, x_segment, identified_length, segment_counts, segment_order


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
