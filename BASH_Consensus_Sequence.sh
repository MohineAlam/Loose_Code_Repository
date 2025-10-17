# after alignment extact reads from bam file to create a consensus sequence
#!/bin/bash


input="$1"
#ref="$2"

# exit command execution if one command fails
set -e

#### create output folder
#output="$input"/Read_Counts

#if [[ ! -d "$output" ]]; then
#       echo "Output folder does not exist. Creating output folder."
#       mkdir "$output"
#else
#       echo "Output foler exists."
#fi

# check if paths exist
if [[ -z "$input" ]]; then
        echo "ERROR: input path does not exist."
        exit 1
else
        echo "All pathways exist."
fi

for bamfile in "$input"/*.bam; do

        # basename
        basename=$(basename "$bamfile" .bam)
        # message to user
        echo "Creating consensus sequence for $basename"
        # execute bcftools to extract read information and convert to fastq format
#       bcftools mpileup -f "$ref" "$bamfile" -B | bcftools call -c | vcfutils.pl vcf2fq > "$input"/"$basename"_consensus.fastq
        # convert the fastq to a fasta format, adjust quality score to 64 and change bases with Q20 score to "N"
#       seqtk seq -aQ64 -q20 -n N "$output"/"$basename"_consensus.fastq > "$input"/"$basename"_consensus.fasta
        samtools consensus -f fasta "$bamfile" -o "$input"/"$basename"_cns.fa

done
