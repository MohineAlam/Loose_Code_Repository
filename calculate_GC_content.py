import os
import argparse
import sys
from Bio import SeqIO
from snapgene_reader import snapgene_file_to_seqrecord

#======= command line argument
parser = argparse.ArgumentParser(
	description = "Input DNA fasta file to calculate the GC content."
)

parser.add_argument("--dna","-i",required=True,help="Fasta file containing the DNA or RNA sequence.")

args = parser.parse_args()

#======= function to calculate GC content
def gc_content(dna):

	"""
	This function calculates the GC content of the DNA sequence provided.

	Parameters:
	fasta - a string representing the DNA sequence

	Output:
	a float - GC content as a percentage

	"""

	#====== convert .dna file into fasta file
	seqrecord = snapgene_file_to_seqrecord(dna)
	sequence = str(seqrecord.seq).upper()

	#====== calculate GC content

	# if no sequence is given
	if len(sequence) == 0:
		return 0.0

	# count the Cystines and Guanidines
	gc_count = sequence.count("G") + sequence.count("C")

	# calculate the percentage
	gc_percent = (gc_count / len(sequence)) * 100

	return round(gc_percent, 2)

if __name__ == "__main__":
	gc_content = gc_content(args.dna)
	print(gc_content)
