# after importing all tools for sequencing (fastqc, multiqc, samtools, faidx)

import os
import subprocess

# Preprocessing - Make directory to store fastqc of fastq files ####
# ------------------------------------------------------------------

# Function to create a directory
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to run FastQC on FASTQ files and output reports to a directory
def run_fastqc_and_output_reports(fastq_files, output_directory):
    for fastq_file in fastq_files:
        # Create the output directory
        create_directory(output_directory)
        # Run FastQC on the FASTQ file
        subprocess.run(['fastqc', fastq_file, '-o', output_directory])


# Run Multiqc on the reports stored in the QC_Report directory - now you can judge quality of reads
# -------------------------------------------------------------------------

# Function to run MultiQC on the QC_Reports directory
def run_multiqc_on_reports(output_directory):
    # Run MultiQC on the QC_Reports directory
    subprocess.run(['multiqc', output_directory])

# Make a Mapping directory to store mapped sequences, index your reference fasta file using samtools faidx
# -------------------------------------------------------------------------

# Function to create a Mapping directory and index the reference FASTA file
def create_mapping_directory_and_index_fasta(reference_fasta, mapping_directory):
    # Create the Mapping directory
    create_directory(mapping_directory)
    # Index the reference FASTA file
    subprocess.run(['samtools', 'faidx', reference_fasta])

# Align the sequence reads to the reference file using bwa mem and store it as a sam file
# --------------------------------------------------------------------------
# Function to align FASTQ sequences to the reference FASTA, store it in the Mapping directory, and convert to SAM inside the mapping directory
def align_fastq_to_fasta_and_convert_to_sam(fastq_files, reference_fasta, mapping_directory):
    # Align FASTQ sequences to the reference FASTA and output to a SAM file
    for fastq_file in fastq_files:
        sam_file = os.path.join(mapping_directory, os.path.splitext(os.path.basename(fastq_file))[0] + '.sam')
        subprocess.run(['bwa', 'mem', reference_fasta, fastq_file], stdout=open(sam_file, 'w'))

# convert the sam file to a bam file using 20 threads
# -----------------------------------------------------------------------
# Function to convert SAM files to BAM files
def convert_sam_to_bam(mapping_directory):
    # Convert SAM files to BAM files
    for sam_file in os.listdir(mapping_directory):
        if sam_file.endswith('.sam'):
            bam_file = os.path.splitext(sam_file)[0] + '.bam'
            subprocess.run(['samtools', 'view', '-b', '-o', os.path.join(mapping_directory, bam_file), os.path.join(mapping_directory, sam_file)])
            subprocess.run(['samtools', 'index', os.path.join(mapping_directory, bam_file)])

# now sort the bam file in the order it was mapped
# ----------------------------------------------------------------------
# Function to sort BAM files
def sort_bam_files(mapping_directory):
    # Sort BAM files
    for bam_file in os.listdir(mapping_directory):
        if bam_file.endswith('.bam'):
            sorted_bam_file = os.path.splitext(bam_file)[0] + '_sorted.bam'
            subprocess.run(['samtools', 'sort', '-@', '10', '-o', os.path.join(mapping_directory, sorted_bam_file), os.path.join(mapping_directory, bam_file)])

# index sorted bam - now you have all files to visualise on IGV
# -----------------------------------------------------------------------
# Function to index sorted BAM files
def index_sorted_bam_files(mapping_directory):
    # Index sorted BAM files
    for bam_file in os.listdir(mapping_directory):
        if bam_file.endswith('_sorted.bam'):
            index_file = bam_file + '.bai'
            subprocess.run(['samtools', 'index', os.path.join(mapping_directory, bam_file), os.path.join(mapping_directory, index_file)])


# Define fastq files and directory 
if __name__ == "__main__":
    # List of FASTQ files
    fastq_files = ['path/to/file1.fastq', 'path/to/file2.fastq']
    # Output directory for FastQC reports
    output_directory = 'QC_Reports'
    # Directory for mapping
    mapping_directory = 'Mapping'
    # Reference FASTA file
    reference_fasta = 'path/to/reference.fasta'

    # Run FastQC on FASTQ files and output reports to the directory
    run_fastqc_and_output_reports(fastq_files, output_directory)

    # Run MultiQC on the QC_Reports directory
    run_multiqc_on_reports(output_directory)

    # Create Mapping directory and index the reference FASTA file
    create_mapping_directory_and_index_fasta(reference_fasta, mapping_directory)

    # Align FASTQ sequences to the reference FASTA and convert to SAM
    align_fastq_to_fasta_and_convert_to_sam(fastq_files, reference_fasta, mapping_directory)

    # Convert SAM files to BAM files
    convert_sam_to_bam(mapping_directory)

    # Sort BAM files
    sort_bam_files(mapping_directory)
    
    # Index sorted BAM files
    index_sorted_bam_files(mapping_directory)

# next step variant calling