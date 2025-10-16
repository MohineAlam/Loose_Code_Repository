#!/bin/bash
set -e

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

# bash scripts for sequence processing
#==============================================================#
# looped_count_reads.sh count total, mapped, and unmapped reads
#==============================================================#
##!/bin/bash
#set -e

# output folder
#output_file="$1"
#input_file="$2"
# initialise count_reads.txt file
#echo "Reads" > "$output_file"

# loop through all .bam files
#for bam_file in "$input_file"/*.bam; do

        # message to user
#        echo "Running read counts for $bam_file"

        # extract names of bam files
#        bam_file_name=$(basename "$bam_file" .bam)
        # find total reads of bam files
#        total_reads=$(samtools view -c "$bam_file")
        # find mapped reads of bam files
#        mapped_reads=$(samtools view -c -F 4 "$bam_file")
        # find unmapped reads of bam files
#        unmapped_reads=$(samtools view -c -f 4 "$bam_file")

        # save total reads to count_reads.txt file
#        echo "$bam_file_name Total_Reads: $total_reads" >> "$output_file"
        # save mapped reads to count_reads.txt file
#        echo "$bam_file_name Mapped_Reads: $mapped_reads" >> "$output_file"
        # save unmapped reads to count_reads.txt file
#        echo "$bam_file_name Unmapped_Reads: $unmapped_reads" >> "$output_file"
#done

#echo "Processing of the bam files has finished. You can find your data saved in $input_file"

