#===================================================================#
# extract subset of mapped reads from large bam file for long reads
#===================================================================#

#!/bin/bash
set -e

# define folders and files
input_file="$1"
output_folder="$2"
reference_file="$3"

for bam_file in "$input_file"/*.bam; do
        # basename of file
        bam_file_name=$(basename "$bam_file" .bam)
        # message to user
        echo "Processing $bam_file"
        # extract mapped reads from bamfile
        samtools fastq -F 4 -0 "$output_folder"/"$bam_file_name"_subset_mapped_reads_step1.fastq "$bam_file"
        # use seqtk to subset 10M reads from fastq file
        seqtk sample -s100 "$output_folder"/"$bam_file_name"_subset_mapped_reads_step1.fastq 10000000 > "$output_folder"/"$bam_file_name"_small_subset.fastq
        # index reference file
        bwa-mem2 index "$reference_file"
        # align reads against reference files
        bwa-mem2 mem -t 8 "$reference_file" "$output_folder"/"$bam_file_name"_small_subset.fastq > "$output_folder"/"$bam_file_name"_small_subset_aligned_reads.sam
        # convert sam to compressed bam file - sort
        samtools view -@ 8 -bS "$output_folder"/"$bam_file_name"_small_subset_aligned_reads.sam | samtools sort -@ 8 -o "$output_folder"/"$bam_file_name"_small_subset.bam
        # index bam file
        samtools index "$output_folder"/"$bam_file_name"_small_subset.bam

        # remove intermediate files
        if [[ $? == 0 ]]; then
                if [[ -f "$output_folder"/"$bam_file_name"_small_subset_aligned_reads.sam ]]
                        rm  "$output_folder"/"$bam_file_name"_small_subset_aligned_reads.sam && echo "SAM file cleaned."
                else
                        echo "There was an issue with alignment"
        fi
        # message to user
        echo "Processing of $bam_file_name finished."
done

if [[ $? == 0 ]]; then
        echo "Bam files have been processed successfully."
fi
