#!/bin/bash
source /miniconda3/conda.sh
conda activate QC

# file output
output_file=$"$HOME/path/to/output/count_reads.txt"
input_file=$"$HOME/path/to/input"
# initialise the output text file
echo -n "Total_Reads" > "$output_file"

# loop through each .bam file in your folder
for bam_file in "$input_file"*.bam; do

	# message to user
	echo "Processing $bam_file"

	#get file name without path
	bam_filename=$(basename "$bam_file" .bam)

	# get total reads
	total_reads=$(samtools view -c "$bam_file")
	echo "$bam_filename total_reads: $total_reads" >> "$output_file"

	# get mapped reads
	mapped_reads=$(samtools view -c -F 4 "$bam_file")
	echo "$bam_filename mapped_reads: $mapped_reads" >> "$output_file"

	# get unmapped reads
	unmaped_reads=$(samtools view -c -f 4 "$bam_file")
	echo "$bam_filename unmapped_reads: $unmapped_reads" >> "$output_file"
done

echo "Processing done. Results are in $output_file"
