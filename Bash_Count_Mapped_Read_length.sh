# input needs a bam file - created after alignment with reference.
#!/bin/bash
set -e

# command line arguments
input="$1"

# check if pathways exist
if [[ ! -d "$input" ]]; then
        echo "ERROR: input pathway does not exist."
        exit 1
else
        echo "Input pathway exists."
fi

# create new folder to save output file
output="$input"/Read_Counts

if [[ ! -d "$output" ]]; then
        echo "Output folder does not exist. Creating $output"
        mkdir "$output"
else
        echo "Output folder exists."
fi

# loop through bam files and extract read lengths
for bamfile in "$input"/*.bam; do

        # basename
        basename=$(basename "$bamfile" .bam)
        # message to user
        echo "Processing $basename. Extracting read length of each mapped reads."
        # extract mapped read length data - exclude any unmapped, supplementary, and not primary (secondary) reads
        samtools fastq -F 2308 "$bamfile" | awk "NR % 4 == 2" | awk "{print length}" > "$output"/"$basename"_MappedReadLength.txt
        # message to user
        echo "Finished processing $basename."
done

if [[ $? == 0 ]]; then
        echo "All commands executed successfully."
fi
