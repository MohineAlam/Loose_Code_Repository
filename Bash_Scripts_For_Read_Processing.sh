# bash scripts for sequence processing
#==============================================================#
# looped_count_reads.sh count total, mapped, and unmapped reads
#==============================================================#
#!/bin/bash

# output folder
output_file=$"$HOME/"
input_file="$HOME/"
# initialise count_reads.txt file
echo "Reads" > "$output_file"

# loop through all .bam files
for bam_file in "$input_file"/*.bam; do

        # message to user
        echo "Running read counts for $bam_file"

        # extract names of bam files
        bam_file_name=$(basename "$bam_file" .bam)
        # find total reads of bam files
        total_reads=$(samtools view -c "$bam_file")
        # find mapped reads of bam files
        mapped_reads=$(samtools view -c -F 4 "$bam_file")
        # find unmapped reads of bam files
        unmapped_reads=$(samtools view -c -f 4 "$bam_file")

        # save total reads to count_reads.txt file
        echo "$bam_file_name Total_Reads: $total_reads" >> "$output_file"
        # save mapped reads to count_reads.txt file
        echo "$bam_file_name Mapped_Reads: $mapped_reads" >> "$output_file"
        # save unmapped reads to count_reads.txt file
        echo "$bam_file_name Unmapped_Reads: $unmapped_reads" >> "$output_file"
done

echo "Processing of the bam files has finished. You can find your data saved in $input_file"



#=============================================#
# count_MappedReadLength.sh Mapped Read Length 
#==============================================#
# Activate conda to use Samtools
#!/bin/bash

#----------------------#
# input and output
#----------------------#
input_folder="$HOME/"
output_folder="$HOME/"

#------------------------------------------------------#
# loop through bam files to extract mapped read lengths
#------------------------------------------------------#

for bam_file in "$input_folder"/*.bam; do
        # extract name of bam file
        bam_file_name=$(basename "$bam_file" .bam)
        # message to user
        echo "Proessing $bam_file_name."
        # make .txt file for mapped read lengths
        samtools fastq -F 4 "$bam_file" |awk 'NR % 4 == 2' |awk '{print length}' > "$output_folder"/"$bam_file_name"_MappedReadLength.txt
done

echo "Extraction of mapped read lengths is complete."
echo "MappedReadLength.txt files for each bam file has been saved in $output_folder"


#=======================================================================================#
# process_mapped_reads.sh - extract mapped reads, then re align to another reference  
#=======================================================================================#
#!/bin/bash

#--------------------------#
# files and directories
#--------------------------#
input_file=$"HOME/"
output_folder=$"HOME/"
reference_file=$"HOME/"

#--------------------------#
# extract mapped reads
#--------------------------#
# loops through .bam file you want to extract mapped reads from
for bam_file in "$input_file"/*Genome.bam; do
        # extract name of file
        bam_file_name=$(basename "$bam_file" .bam)

        # message to user
        echo "Processing $bam_file_name"

        # extract mapped reads: nanopore is usually single-end reads unlike illumina which is paired-end
        samtools fastq -F 4 -0 "$output_folder"/mapped_reads.fastq "$bam_file"

        # index new reference e.g. ITR map
        bwa-mem2 index "$reference_file"/"$bam_file_name"

        # align read extract to new reference e.g. ITR map
        bwa-mem2 mem -t 8 "reference_file"/"$bam_file_name" "$output_folder/mapped_reads.fastq" > "$output_folder"/"$bam_file_name"_aligned_reads.sam

        # convert sam to bam file
        samtools view -@ 8 -bS "$output_folder"/"$bam_file_name"_aligned_reads.sam | samtools sort -@ 8 -o "$output_folder"/"$bam_file_name"_aligned_reads.bam

        # index the bam file
        samtools index "output_folder"/"bam_file_name"_aligned_reads.bam

        # now you can view your files on IGV
done

echo "Extraction of mapped reads from your bam files have finished."
echo "You can find the processed bam files in $output_folder"


#===========================================================================================#
# process_unmapped_reads.sh - extract unmapped reads and then realign to new reference
#===========================================================================================#
#!/bin/bash

# path to input and output
bam_file=$"$HOME/"
reference_folder=$"$HOME/"
output_folder=$"$HOME/"

#---------------------------------------#
# function to check if bam files exist
#---------------------------------------#
check_bam_files() {

        if [[ ! -f "$bam_file" ]]; then
                echo "Error: BAM file $bam_file does not exist."
                exit 1
        fi
}

# call function
check_bam_files "$bam_file"

#------------------------------------------------------------------#
# align contamiantion references againsts unmapped reads of genome
#------------------------------------------------------------------#

# loop through for all contamiantion references
for ref in "$reference_folder"/*Genome.fa; do
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


#==================================================================#
# long read alignment using minimap2 - to be executed by .py file
#==================================================================#
#!bin/bash

# file and folder paths
input_file=$"$1"
output_folder=$"$2"
reference_file=$"$3"

if [[ -z "$input_file" || -z "$output_folder" || -z "$reference_file" ]]; then
        echo "Error: Missing input file/ output folder/ reference file"
        echo "Usage: $0 <input_file> <output_folder> <reference_file>"
        exit 1
fi

# loops through bam files:
for bam_file in "$input_file"/*.bam; do

        # extract bam file name
        bam_file_name=$(basname "$bam_file" .bam)

        # message to user
        echo "Processing $bam_file_name"

        # extract mapped reads
        samtools fastq -F -0 "$output_folder"/"$base_name_file"_mapped_reads_step2.fastq "$bam_file"

        # index reference file
        minimap2 -d "$output_folder"/ref.mmi "$reference_file"

        # align read extract to new reference, VA_RNA.fa map
        minimap2 -a -x map-ont "$reference_file" "$output_folder"/"$base_name_file"_mapped_reads_step2.fastq > "$output_folder"/"$bam_file_name"_aligned_reads.sam

        # convert sam file to bam
        samtools view -@ 8 -bS "$output_folder"/"$bam_file_name"_aligned_reads.sam > samtools sort -@ 8 -o "$output_folder"/"$bam_file_name"_aligned_reads.bam


#====================================================#
# extract subset of mapped reads from large bam file
#====================================================#

#!/bin/bash

# define folders and files
input_file="$HOME/"
output_folder="$HOME/"
reference_file="$HOME/"

for bam_file in "$input_file"/*.bam; do
        bam_file_name=$(basename "$bam_file" .bam)
        echo "Processing $bam_file"
        samtools fastq -F 4 -0 "$output_folder"/"$bam_file_name"_subset_mapped_reads_step1.fastq "$bam_file"
        seqtk sample -s100 "$output_folder"/"$bam_file_name"_subset_mapped_reads_step1.fastq 10,000,000 > "$output_folder"/"$bam_file_name"_small_subset.fastq
        bwa-mem2 index "$reference_file"
        bwa-mem2 mem -t 8 "$reference_file" "$output_folder"/"$bam_file_name"_small_subset.fastq > "$output_folder"/"$bam_file_name"_small_subset_aligned_reads.sam
        samtools view -@ 8 -bS "$output_folder"/"$bam_file_name"_small_subset_aligned_reads.sam | samtools sort -@ 8 -o "$output_folder"/"$bam_file_name"_small_subset.bam
        samtools index "$output_folder"/"$bam_file_name"_small_subset_aligned_reads.bam
done
        # index bam file
        samtools index "$output_folder"/"$bam_file_name"_aligned_reads.bam

        # message to user
        echo "Processing of $bam_file_name finished."
done

echo "Bam files have been processed."

