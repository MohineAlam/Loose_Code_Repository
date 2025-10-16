
#=======================================================================================#
# process mapped reads - extract mapped reads, then re align to another reference  
#=======================================================================================#
#!/bin/bash
set -e

#--------------------------#
# files and directories
#--------------------------#
input_file="$1"
output_folder="$2"
reference_file="$3"

#--------------------------#
# extract mapped reads
#--------------------------#
# loops through .bam file you want to extract mapped reads from
for bam_file in "$input_file"/*.bam; do
        # extract name of file
        bam_file_name=$(basename "$bam_file" .bam)

        # message to user
        echo "Processing $bam_file_name"

        # extract mapped reads: nanopore is usually single-end reads unlike illumina which is paired-end
        samtools fastq -F 4 -0 "$output_folder"/mapped_reads.fastq "$bam_file"

        # index new reference 
        minimap2 -d "$output_folder"/ref.mmi "$reference_file"/"$bam_file_name"

        # align read extract to new reference 
        minimap2 -a -x map-ont "$output_folder"/ref.mmi "$output_folder"/mapped_reads.fastq > "$output_folder"/"$bam_file_name"_aligned_reads.sam

        # convert sam to bam file
        samtools view -@ 8 -bS "$output_folder"/"$bam_file_name"_aligned_reads.sam | samtools sort -@ 8 -o "$output_folder"/"$bam_file_name"_aligned_reads.bam

        # index the bam file
        samtools index "output_folder"/"bam_file_name"_aligned_reads.bam

        # now you can view your files on IGV
done

echo "Extraction of mapped reads from your bam files have finished."
echo "You can find the processed bam files in $output_folder"
