#!/bin/bash
source ~/.bashrc

# command line argument
input="$1"

# exit if a command fails
set -e

# check if pathway exists
if [[ ! -d "$input" ]]; then
        echo "ERROR: input pathway does not exist."
        exit 1
else
        echo "Input pathway exists."
fi

# loop through bam files and convert them to .bed
for bamfile in "$input"/*.bam; do

        # basename
        basename=$(basename "$bamfile" .bam)

        # message to user
        echo "Processing $basename into bed file."

        # convert bam to bed file
        bedtools bamtobed -i "$bamfile" > "$input"/"$basename".bed

        # add an additional text file
        bedtools bamtobed -i "$bamfile" > "$input"/"$basename".txt

        # message to user
        if [[ $? == 0 ]]; then
                echo "Finished processing $basename"
        fi
done
