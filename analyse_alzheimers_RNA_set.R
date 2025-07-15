#======================== download RNA seq data from GEO
install.packages("GEOquery")
install.packages("limma")

library(GEOquery)
library(DESeq2)
library(ggplot2)
library(pheatmap)
library(clusterProfiler)
library(org.Hs.eg.db)
library(enrichplot)
library(dplyr)

# fetch data from GSEO using GSE33000
gse <- getGEO("GSE33000", GSEMatrix = TRUE)

# Check the structure of the data
gse

# extract expression matrix and metadata
expr <- exprs(gse[[1]])
meta <-
