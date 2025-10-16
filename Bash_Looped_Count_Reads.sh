#!/bin/bash

# file output
output="$1"
input="$2"
# initialise the output text file
echo -n "Total_Reads" > "$output"/count_reads.txt

# loop through each .bam file in your folder
for bam_file in "$input"/*.bam; do

	# message to user
	echo "Processing $bam_file"

	#get file name without path
	bam_filename=$(basename "$bam_file" .bam)

	# get total reads
	total_reads=$(samtools view -c "$bam_file")
	echo "$bam_filename total_reads: $total_reads" >> "$output"/count_reads.txt

	# get mapped reads
	mapped_reads=$(samtools view -c -F 4 "$bam_file")
	echo "$bam_filename mapped_reads: $mapped_reads" >> "$output"/count_reads.txt

	# get unmapped reads
	unmaped_reads=$(samtools view -c -f 4 "$bam_file")
	echo "$bam_filename unmapped_reads: $unmapped_reads" >> "$output"/count_reads.txt
done

echo "Processing done. Results are in $output"
