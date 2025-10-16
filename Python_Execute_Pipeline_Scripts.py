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
A_alignment = './A_Alignment.sh'
B_alignment = './B_Alignment.sh'

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
                A_Alignment_cmd = run_script(A_Alignment,input,output,reference)
                print(A_Alignment_cmd.stdout)
                print(A_Alignment_cmd.stderr)
                if A_Alignment_cmd.returncode != 0:
                        print("Error: A_Alignment.sh script failed.")
                        sys.exit(1)
                B_alignment_cmd = run_script(B_alignment,input,output,reference)
                print(B_alignment_cmd.stdout)
                print(B_alignment_cmd.stderr)
                if B_alignment_cmd.returncode != 0:
                        print("Error: B_Alignment.sh script failed.")
                        sys.exit(1)
        else:
                print("Missing data. Input, output, or reference pathway is not correct.")
                sys.exit(1)

# call function
alignments(argse.input,argse.output,argse.reference)
