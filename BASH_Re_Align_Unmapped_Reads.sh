#===========================================================================================#
# process unmapped reads - extract unmapped reads and then realign to new reference
#===========================================================================================#
#!/bin/bash
set -e

# path to input and output
bam_file="$1"
reference_folder="$2"
output_folder="$3"

#---------------------------------------#
# function to check if bam files exist
#---------------------------------------#
check_bam_files() {

        if [[ ! -f "$bam_file" ]]; then
                echo "Error: BAM file $bam_file does not exist."
                exit 1
        else
            echo "Bam file exists."
        fi
}

# call function
check_bam_files "$bam_file"

#----------------------------------------------------------------------------------------#
# align contamiantion references againsts unmapped reads of genome for illumina reads
#----------------------------------------------------------------------------------------#

# loop through for all contamiantion references
for ref in "$reference_folder"/*.fa; do
        # basename extraction
        reference_name=$(basename "$ref" .fa)

        # message to user
        echo "Aligning against $reference_name"

        # extract unmapped reads for single end data into a FASTQ file
        samtools fastq -f 4 -0 "$output_folder"/unmapped_reads.fastq "$bam_file"

        # align reads to the contamination maps
        bwa-mem2 index "$ref" > "$reference_folder"/"$reference_name"
        bwa-mem2 mem -t 8 "$reference_folder"/"$reference_name".fa "$output_folder/unmapped_reads.fastq" > "$output_folder"/"$reference_name"_aligned_reads.sam

        # convert sam to bam and sort
        samtools view -@ 8 -bS "$output_folder"/"$reference_name"_aligned_reads.sam | samtools sort -@ 8 -o "$output_folder"/"$reference_name"_aligned_reads.bam
        # index bam file
        samtools index "$output_folder"/"$reference_name"_aligned_reads.bam > "$output_folder"/"$reference_name"

done

echo "The unmapped reads have been aligned to your references."
echo "The new bam files are saved in  $output_file"

