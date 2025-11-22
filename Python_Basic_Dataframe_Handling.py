
#------------- creating a data frame
import pandas as pd

data = {
	"sample" : ["A", "B", "C"],
	"value" : [10, 35, 22],
	"type" : ["illumina", "ont", "illumina"]
}

df = pd.DataFrame(data)

#------------ reading and writing a csv
df = pd.read_csv("file.csv") # read
df.to_csv("output.csv", index=False) # write

#------------ inspect dataframe
print(df.head()) # first five rows
print(df.tail()) # last five rows
print(df.info()) # column types and nulls
print(df.describe()) # summary statistics for numeric columns

#----------- select column
values = df["value"] # single column
subset = df[["sample", "value"]] # multiple columns

#----------- filtering rows
filtered = df[df["value"] > 20] # all values bigger than 20
illumina_only = df[df["type"] == "illumina"] # string match
filtered2 = df[(df["value"]) > 20 & (df["type"] == "illumina")]

#---------- adding or modifying columns
df["value_squared"] = df["value"] ** 2
df["category"] = df["value"].apply(lambda x : "high" if x > 20 else "low")


#---------- dropping coluns / rows
df = df.drop(columns="value_squared")
df = df.drop(index=[0,2])

#--------- sorting
df_sorted = df.sort_values(by="value", ascending=False)

#--------- groupby + aggregations
grouped = df.groupby("type")["value"].mean()

stats = df.groupby("type").agg(
	mean_value=("value", "mean"),
	max_value=("value", "max"),
	count=("value", "count")
)


#-------- merge data frame
meta = pd.DataFrame({
	"sample": ["A", "B", "C"],
	"host": ["human", "cow", "human"]
})

merged = df.merge(meta, on="sample", how="right")


#-------- pivot tables
df_long = pd.DataFrame({
	"sample": ["A", "A", "B", "B"],
	"metric": ["coverage", "quality", "coverage", "quality"],
	"value": [20,35,18,40]
})

#print(df_long)

pivot = df_long.pivot_table(
    index="sample",
    columns="metric",
    values="value",
    aggfunc="mean"
)

#print(pivot)
#-------- melting (long format)
long = pivot.reset_index().melt(
	id_vars="sample",
	var_name="type",
	value_name="value"
)


#---------- handling missing data
df["value"] = df["value"].fillna(0) # fille NA values with 0
df = df.dropna() # drop NA values


#---------- Reading dates, converting types
df["date"] = pd.to_datetime(df["date"])
df["value"] = df["value"].astype(float)


#--------- Applying functions row wise
def label_row(row):
	return f"{row['sample']}_{row['type']}"

df["label"] = df.apply(label_row, axis=1) # axis 1 = apply across columns, axis 0 = apply down columns

#print(df)
