#=============================================#
# count_MappedReadLength.sh Mapped Read Length 
#==============================================#
#!/bin/bash
set -e

#----------------------#
# input and output
#----------------------#
input_folder="$1"
output_folder="$2"

# check if pathways exist.
check_path() {
  if [[ ! -e "$1" ]]; then
    echo "Pathway doesn't exist."
    exit 1
  else
    echo "Pathway exists"
  fi
}

check_path "$input_folder"
check_path "$output_folder"
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
