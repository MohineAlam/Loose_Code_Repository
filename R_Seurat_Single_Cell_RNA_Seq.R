# here are 2,700 single cells that were sequenced on the Illumina NextSeq 500
# dependencies
install.packages("curl")
install.packages("openssl")
install.packages("httr")
install.packages("plotly")
# Seurat Object - manipulating single cell data using illumina seq ####

# Day 1 

# load libraries
install.packages("Seurat")
install.packages("patchwork")
install.packages("dplyr")
library(dplyr)
library(Seurat)
library(patchwork)

# The values in this matrix represent the number of molecules for each feature (i.e. gene; row) that are detected in each cell (column)

# load pbmc data (peripheral blood mononuclear cells) ####
# available from 10x genomics
pbmc.data = Read10X(data.dir = "/home/Suerat_practice/pbmc3k_filtered_gene_bc_matrices(1)/filtered_gene_bc_matrices/hg19/")

# create suerat object ####
pbmc = CreateSeuratObject(counts = pbmc.data, project="pbmc3k",min.cells=3, min.features=200)

# stanard preprocessing work flow ####
# filter cells based on QC measurements, data normalisation, and scaling, and detection of variablity

# QC selection ####
# number of unique genes in each cells, 
# total number of molecules detected in each cell,
# percentage of genes that map to mitochondrial genes - looks for genes atrting with MT
pbmc$"percent.mt" = PercentageFeatureSet(pbmc, pattern = "^MT-")

# Visualise unedited data  ####
# Visualise data as table
head(pbmc@meta.data, 5)
# Visualise QC metrics as violinplot
vp = VlnPlot(pbmc, features = c("nCount_RNA","nFeature_RNA","percent.mt"), ncol = 3)

# have a look at the relationship between each variable: var1/var2, var1/var3
# use FeatureScatter graph, it will give you a p value
# we see the percentage of mt genes in all RNA counts and amount of unique genes in all RNA counts
count_feature = FeatureScatter(pbmc, feature1 = "nCount_RNA", feature2 = "nFeature_RNA")
count_MTpercent = FeatureScatter(pbmc, feature1 = "nCount_RNA", feature2 = "percent.mt")
count_feature + count_MTpercent

# subset data ####
# we want to :
# filter cells that have unique feature counts over 2,500 or less than 200
# filter cells that have >5% mitochondrial counts
pbmc = subset(pbmc, subset = nFeature_RNA > 200 & nFeature_RNA < 2500 & percent.mt < 5)

# Normalising the data ####
# normalisation done on featureRNA expression measurment of each cell by total expression
# multiply this by a scale factor
# and log transformation of result
# global scaling relies on the fact that each cell contains the same number of RNA
# there are individual tools e.g SCTransfom() that take this into account, replaces NormalizeData, FindVariableFeatures, or ScaleData

pbmc = NormalizeData(pbmc, normalization.method = "LogNormalize", scale.factor = 10000)
# you can also do this
pbmc = NormalizeData(pbmc)

# identifying highly variable features ####
# catagorise subset feature of high cell to cell variation
# some are high some are lowly expressed, help identify biological signal in single cell dat
# directly models mean variance relationship inherent in single cell data
# this can be used in downstream analysis like PCA
# return 2000 features per data set using variance stabilizing transformation method
# this give us the top variable genes which we can now usue in e.g. clutering, PCA/ dimentionality reduction
pbmc = FindVariableFeatures(pbmc, selection.method = "vst", nfeatures = 2000)

# identify top 10 variable genes
top_10 = head(VariableFeatures(pbmc), 10)
top_10

# plot variable features with and without labels
variable_features = VariableFeaturePlot(pbmc)
variable_features_labels = LabelPoints(plot = variable_features, points = top_10, repel = TRUE)
variable_features + variable_features_labels

# export graph as a png file as the x axis is too large
install.packages("ggplot2")
library(ggplot2)
ggplot2::ggsave("variable_features.png", plot = variable_features, width = 10, height = 10)
ggplot2::ggsave("variable_features_labels.png", plot = variable_features_labels, width = 10, height = 10)

# Scaling the data ####
# pre processing step before PCA, ScaleDate()
# shifts expression of each gene, so mean expression across cell is 0
# scales expression of each gene so variance across cell is 1 (so highly expressed gene dont dominate) e.g. 1,1,1,2,3,3 = 1,2,3
# stored as "RNA"scaled.data . by default only variable features are scaled
# you can specify the feature in scaled.feature argument to specify more features
all_genes = rownames(pbmc)
pbmc_scaled = ScaleData(pbmc, features = all_genes)

# now you can plot based on z-scored 

# you can regress data (that produces noise) -remove its unwanted effects/variation on the data
# high expression of MT RNA is indication of e.g apoptosis or cell stress, skewing gene expression, or bad sample prep (e.g. cyotplasm RNA not removed)
pbmc = ScaleData(pbmc_scaled, vars.to.regress = "percent.mt")

# perform linear dimensional reduction ####
# we can now perform PCA on scaled data (with most variable gene sets - previously defined)
# outputs genes of most of most positive or negative loading, representing modules of genes that exhibit correlations across single cells in data set
pbmc_PCA = RunPCA(pbmc, features = VariableFeatures(object = pbmc))

# now you can use the pbmc_PCA file to visualise the data set as it contains the principle component score
# PCA scores is used to reduce dimentionality and identify patterns while still retaining most of its variability in genes
# remember the dendrogram and its sorting by identifying a sort of mean between each gene then rewriting the p values in sorted significance

# visualise both cells and features that define PCA scores ####
DimPlot(pbmc_PCA)
DimHeatmap(pbmc_PCA)

# visualise PCA results different ways ####
print(pbmc[["pca"]], dims = 1:5, nfeatures = 5)

#
VizDimLoadings(pbmc, dims=1:2,reduction="pca")
