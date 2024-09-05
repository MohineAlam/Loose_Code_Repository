# load packages
import os
import subprocess
import argparse
import sys

# input files and directory
parser = argsparse.ArgumentPaser(
        description = "Path to folders and files.")
parser.add_argument('-i','--input',required=True,help='Path to input files')
parser.add_argument('-o','--output',required=True,help='Path to output folder')
parser.add_argument('-r','--reference',required=False,help='Path to reference')
args = parser.parse_args()

# path to your bash script
ITR_alignment = './ITR_Alignment.sh'
RNA_alignment = './RNA_Alignment.sh'

# function to run bash scripts
def run_script(script_path,input,output,reference):
        command = ['bash',script_path,input,output]
        if reference:
                command.append(reference)
        result = subprocess.run(command,capture_output=True,text=True)
        return result

# check path, folder and files exist
def check_directory_file_exist(input,output,reference):
        input_output = os.path.exists(os.path.join(input,output,reference))
        return input_output

# Output the result
def alignments(input,output,reference):
        if check_directory_file_exist(input,output):
                RNA_Alignment = run_script(RNA_Alignment,input,output,reference)
                print(RNA_Alignment.stdout)
                print(RNA_Alignment.stderr)
                if RNA_Alignment.returncode != 0:
                        print("Error: RNA_Alignment.sh script failed.")
                        sys.exit(1)
                ITR_alignment = run_script(ITR_alignment,input,output,reference)
                print(ITR_alignment.stdout)
                print(ITR_alignment.stderr)
                if ITR_alignment.returncode != 0:
                        print("Error: ITR_Alignment.sh script failed.")
                        sys.exit(1)
        else:
                print("Missing data. Input, output, or reference pathway is not correct.")
                sys.exit(1)

# call function
alignments(argse.input,argse.output,argse.reference)
