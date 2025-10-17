# execute this script as: ./script ~/path/to/bam/files ~/ref/file/.fa

# activate environment
#!/bin/bash
conda activate conda_myenv

# define input pathways
input="$1"
ref="$2"

# exit if one command fails
set -e

# check if input files exist
if [[ ! -d "$input" ]]; then
        echo "Error input pathway does not exist."
        exit 1
else
        echo "Input pathway exists."
fi

# loop through aligned and sorted bam files in input pathway - extract CNV data
for bamfile in "$input"/*.bam; do
        # extract file basename
        basename=$(basename "$bamfile" .bam)
        # add md tag - which identifies structural variants
        samtools calmd "$bamfile" "$ref" -b > "$input"/"$basename"_md.bam
        # call sniffles tool with tagged bam file
        sniffles --mapq 20 -i "$input"/"$basename"_md.bam -v "$input"/"$basename"_cnv.vcf --threads 35
        # message to user
        if [[ $? == 0 ]]; then
                echo "Finished processing $basename"
        else
                echo "$basename could not be processed."
        fi
done

# finished message if all commands executed
if [[ $? == 0 ]]; then
        echo "Finished processing all files with sniffles."
fi
