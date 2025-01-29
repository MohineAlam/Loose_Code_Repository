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
import csv
import pandas as pd
import matplotlib.pylot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# command line arguments: input_gene, output ###
args =

#===================================#
# function to fetch the genetic data
#===================================#
def fetch_genetic_data(output,gene_name):
	# define url to retirieve gene data
	url = f"https://rest.ensemble.org/sequence/id/{gene_name}?content-type=application/json"
	response = requests.get(url)
	# create file to save data
	gene_output = os.join.path(output,f"{gene_name}.txt") ###
	# see if request works
	if response == 200: # if request was successfull
		data = response.json()
		with open(gene_output, "a") as file:
			json.dump(data, file, indent = 4)

		print(f"{gene_name} data was fecthed and saved to {gene_output}")
	else:
		print("ERROR: failed to retrieve the data through the API. Try again.")
		return None # does not return data as it will be empty
	return data

gene_data = fetch_genetic_data(output,input_gene) ### input e.g. "BRCA1"

#=====================================#
# function to process genetic variants
#=====================================#
def variants(gene_data):
	df = pd.DataFrame(gene_data)
	return df

if gene_data:
	variants_df = variants(gene_data["Variants"])
	variants_output = os.join.path(output, f"{input_gene}_variants.csv")

	# save variant data to csv file in output
	variants_df.to_csv(variants_output, index=FALSE)
	print(f"Variant data of {input_gene} is save to {variants_output}")

#=============================================#
# visualise SNPs or mutations using matplotlib
#=============================================#
def plot_variant_data(variants_df):
	plt.figure(figsize=(10, 6))
	plt.scatter(df["postion"], df["mutation_type"], colour="b", label="Mutation")
	plt.xlabel("Genomic Position")
	plt.ylabel("Mutation Type")
	plt.title("Genetic Variants")
	plt.show()

if variants_df:
	plot_variant_data(variants_df)

#=========================================#
# integrate machine learning using sciskit - logistic regression
#=========================================#
def train_model(variants_df):
	# gene data set
	x = df.drop("labels", axis=1) # this selects Features (by removing label column) leaving: genetic variants e.g. SNPs, MNPs, indels, insertions
	y = df["labels"] # this selects labels = disease outcome / gene expression of the variant

	# split data into training and testing sets
	# typically you use 70-80% of data to train model - x/y_train
	# x/y_test set is used to simulate how model would perform - testing with known values (test_size=0.2 - 20% data used for testing and 80% used for training)
	# 42 = random seed that ensures reproducibility
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42) # this function splits the data into two sets


	# train model - using logistic regression, a simple model to fine binary results (does this person have this disease yes or no - linear relationship between "features" and probability of target "label")
	# define model
	model = LogisticRegression()
	# input data into model
	model.fit(x_train, y_train)

	# predit outcome of test data set - input x features and predict y labels (disease outcome)
	y_predict = model.predict(x_test)

	# evaluate model - the model outputs probabilities between 0 and 1 (if greater than 0.5, classify as 1)
	accuracy = accuracy_score(y_test, y_predict) # calculates how many predictions were correct by comparing test and prediction sets

	# accuracy
	print(f"Model accuracy is {accuracy * 100:.2f}%")

if variants_df:
	train_model(variants_df)
