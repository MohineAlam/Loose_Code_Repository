#=====================================================#
### human diseas - genetics basis - coding project ###
# Project steps:
# decide on specific disease or gene you want to focus on
# gather genetic data-sets
# set up environement: pandas, matplotlib, biopython, seaborn, requests
# data process function - retrieve data set, compare gene sequences, look for genetic markers (statistical tests to assess significance)
# visualise data

#=====================================================#

# librarires
import os
import argapse
import requests #API
import json
import pandas as pd
import matplotlib.pylot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# command line arguments: input_gene, output ###
args =


# function to fetch the genetic data
def fetch_genetic_data(output,gene_name):
	# define url to retirieve gene data
	url = f"https://rest.ensemble.org/sequence/id/{gene_name}?content-type=application/json"
	response = requests.get(url)
	# create file to save data
	gene_output = os.join.path(output,gene_name.txt) ###
	# see if request works
	if response == 200:
		data = response.json()
		with open(gene_output, "a") as file:
			json.dump(data, file, indent = 4)

	else:
		print("ERROR: failed to retrieve the data through the API. Try again.")
	return data

gene_data = fetch_genetic_data(output,input_gene) ### input e.g. "BRCA1"

# function to process genetic variants
def variants(gene_data):
	df = pd.DataFrame(gene_data)
	return df

variants = variants(gene_data["Variants"])
variants_output = os.join.path(output,"Variants" + .txt)
# save variant data to output
with open(variants_output, "a", newline = "") as file:
	writer = csv.writer(file)
	writer.writerows(variant_output)

# visualise SNPs or mutations using matplotlib

# integrate machine learning using sciskit
