# libraries installed and loaded
#BiocManager::install("GEOquery")
#BiocManager::install("limma",force=TRUE)
#install.packages("pheatmap")
#BiocManager::install("clusterProfiler")
#library(GEOquery)
#library(DESeq2)
library(ggplot2)
library(pheatmap)
#library(clusterProfiler)
#library(enrichplot)
#library(tidyverse)
#library(dplyr)
#library(org.Hs.eg.db)
library(limma)

#==================== fetch data from GSEO using GSE33000
# data downloaded
#==================== extract expression matrixt and meta data
file <- readLines("GSE33000.txt")
start_line <- grep('^"ID_REF"', file)
end_line <- grep("^!series_matrix_table_end", file)
expr_data <- read.table("test.txt", skip = start_line - 1, nrows = end_line - start_line - 1, header = TRUE, sep = "\t", quote = "", comment.char = "", row.names = 1)
#head(expr_data)
meta_data <- grep("^!Sample_", file, value = TRUE)
meta_list <- strsplit(meta_data, "\t")
#head(meta_data)


#============================= Extract metadata field names (removing "!" and keeping only the base name)
field_names <- c()
for (line in meta_list) {
        if (grep("!Sample_",line)) {
                field_name <- sub("!Sample_", "", strsplit(line, " ")[[1]][1])
                field_names <- c(field_names, field_name)
        }
}


#============================== Transpose the metadata so that each sample is a row
meta_matrix <- do.call(rbind, lapply(meta_list, function(x) x[-1]))
rownames(meta_matrix) <- field_names
meta_df <- as.data.frame(meta_matrix, stringsAsFactors = FALSE)
meta_df <- as.data.frame(t(meta_df), stringsAsFactors = FALSE)
# extract relevant columns for analysis "geo_accession", "disease.state", "age", "sex", "ethnicity", "organism"
meta_clean <- meta_df[, c("geo_accession", "characteristics_ch1.8", "characteristics_ch1.11", "characteristics_ch1.9", "characteristics_ch1.6", "characteristics_ch1.2")]
# clean quotes and unwanted characters
meta_clean[] <- lapply(meta_clean, function(x) gsub("^\"|\"$", "", x))  # Remove quotes
meta_clean[] <- lapply(meta_clean, function(x) gsub("Â", "", x))
rownames(meta_clean) <- meta_clean[,"geo_accession"]
# remove extra geo column
meta_clean <- meta_clean[,c("characteristics_ch1.8", "characteristics_ch1.11", "characteristics_ch1.9", "characteristics_ch1.6", "characteristics_ch1.2")]
meta_clean[] <- lapply(meta_clean, function(x) {
  if (is.character(x)) {
    x <- gsub("Â", "", x)  # Remove unwanted characters (like "Â")
    x <- toupper(x)  # Convert text to uppercase
  }
  return(x)
})

# change condition column names into more simple labels for alzheimer and control
meta_clean$condition <- gsub("DISEASE STATE: ", "", meta_clean$characteristics_ch1.8)
meta_clean$condition <- trimws(meta_clean$condition)

# save conditions as factor - telling limma, these are discrete groups, not numeric values
#meta_clean$condition <- factor(meta_clean$condition, levels = c("ALZHEIMER'S DISEASEÂ", "NORMALÂ"), labels = c("disease", "control"))

#======================== save row names of expr_data same as metadata - sample name
# convert expression data as matrix and ensure its numeric to be able to use with limma
expr_matrix <- as.matrix(expr_data, stringsAsFactors = FALSE)
mode(expr_matrix) <- "numeric"

#expr_matrix <- t(expr_matrix)
# clean up data frame
colnames(expr_matrix) <- gsub("^X.", "", colnames(expr_matrix))  # Remove leading "X"
colnames(expr_matrix) <- gsub("\\.$", "", colnames(expr_matrix))  # Remove trailing "."
rownames(expr_matrix) <- gsub("^\"|\"$", "", rownames(expr_matrix))  # Remove leading and trailing quotes

# save tables of expression and meta
write.csv(meta_clean,file.path("~/x/","meta_clean.csv"))
write.csv(expr_matrix,file.path("~/x/","expr_matrix.csv"))

#=============================== create design matrix - predict value of dependant variable based on independent variable. (predict disease variable based on linear model that explains the data)
# specify linear model - find gene expression based on control and disease condtion - fits intro formual ~ y = control avrg + disease avrg * (condition status) + random noise
design <- model.matrix(~ condition, data = meta_clean)

#================================== fit linear model
# normalise library size #### already done by MAS5

# log scale
expr_log2 <- log2(expr_matrix + 1)

fit <- lmFit(expr_log2, design)

# t-test (find significantly expressed genes - log value above 1 and p value below 0.05)
fit <- eBayes(fit)
write.csv(fit,file.path("~/x/","fit.csv"))

#================== get differential expression results - extract and summarise results (coef = 2, extracts second coefficient which represents log fold change between the two cell types)
results <- topTable(fit, coef = 2, number = Inf, adjust = "BH")
#write.csv(results,file.path("~/Bioinformatics_Projects/Bioinformatics_Projects/","results_linear_model.csv"))

#================= filter significant genes
sig_genes <- results[results$adj.P.Val < 0.05 & abs(results$logFC) > 1, ]
#write.csv(sig_genes,file.path("~/Bioinformatics_Projects/Bioinformatics_Projects/","results_sig_genes.csv"))

#================= volcano plot
# extract log2fold and adjusted p value data
logFC <- results$logFC  # LogFC for alzheimers disease
adj_pval <- results$adj.P.Val  # Adjusted p-values

# Create a data frame for ggplot
volcano_data <- data.frame(
  logFC = logFC,
  adj.P.Val = adj_pval,
  neg_log10_pval = -log10(adj_pval),
  threshold = ifelse(adj_pval < 0.05 & abs(logFC) > 1, "Significant", "Not Significant")
)

# Plot using ggplot2
volcano2 <- ggplot(volcano_data, aes(x = logFC, y = neg_log10_pval, color = threshold)) +
  geom_point(alpha = 0.8, size = 2) +
  scale_color_manual(values = c("Not Significant" = "gray", "Significant" = "red")) +
  labs(
    title = "Volcano Plot",
    x = "Log2 Fold Change (logFC)",
    y = "-Log10 Adjusted P-Value"
  ) +
  geom_hline(yintercept = -log10(0.05), color = "black", linetype = "dashed") +
  geom_vline(xintercept = c(-1, 1), color = "black", linetype = "dashed") +
  theme_minimal() +
  theme(legend.position = "top")
ggsave(filename = file.path("~/x/", "volcano2_plot_ad.png"),
        plot = volcano2, device = "png", units = "in", width = 8, height = 4, dpi = 300)


#============================== top genes
# Subset top 50 significant genes by adjusted p-value
top_genes_20 <- rownames(head(results[order(results$adj.P.Val), ], 20))
# subset expression matrix for these genes
heatmap_data <- expr_log2[top_genes_20, ]
# scale genes for better visulisation
heatmap_data_scaled <- t(scale(t(heatmap_data)))
# create annotation for sample
annotation_col <- data.frame(Condition = meta_clean$condition)
rownames(annotation_col) <- colnames(heatmap_data)

# plot heat map
heatmap <- pheatmap(
  heatmap_data_scaled,
  annotation_col = annotation_col,
  show_rownames = TRUE,
  show_colnames = FALSE,
  cluster_rows = TRUE,
  cluster_cols = TRUE,
  color = colorRampPalette(c("blue","black","yellow"))(100)
)

ggsave(filename = file.path("~/x/", "heatmap.png"),
        plot = heatmap, device = "png", units = "in", width = 8, height = 4, dpi = 300)

#================ run PCA on expression matrix
top_genes_50 <- rownames(head(results[order(results$adj.P.Val), ], 50))
top_genes_100 <- rownames(head(results[order(results$adj.P.Val), ], 100))
pca_50 <- prcomp(t(expr_log2[top_genes_50, ]), scale. = TRUE)
pca <- prcomp(t(expr_log2), scale. = TRUE)
pca_100 <- prcomp(t(expr_log2[top_genes_100, ]), scale. = TRUE)
# create data frame with pca results#
pca_df <- data.frame(
  PC1 = pca$x[, 1],
  PC2 = pca$x[, 2],
  Condition = meta_clean$condition
)

# plot with ggplot
pca_plot <- ggplot(pca_df, aes(x = PC1, y = PC2, color = Condition)) +
  geom_point(size = 4) +
  xlab(paste0("PC1 (", round(summary(pca)$importance[2,1] * 100, 1), "% variance)")) +
  ylab(paste0("PC2 (", round(summary(pca)$importance[2,2] * 100, 1), "% variance)")) +
  scale_color_brewer(palette = "Set1")

ggsave(filename = file.path("~/x/", "pca_1_2.png"),
        plot = pca_plot, device = "png", units = "in", width = 8, height = 4, dpi = 300)

#================== find which genes are the outliers from pca plot with full data set
# Sort the loadings for PC1 and PC2 to find the most influential genes
# Loadings are stored in the 'rotation' component of the PCA result
sorted_pc1 <- sort(abs(pca$rotation[, 1]), decreasing = TRUE)  # Sort PC1 loadings
sorted_pc2 <- sort(abs(pca$rotation[, 2]), decreasing = TRUE)  # Sort PC2 loadings

# View the top 10 genes with the highest loadings for PC1 and PC2
top_genes_pc1 <- names(sorted_pc1)[1:10]
top_genes_pc2 <- names(sorted_pc2)[1:10]

# Print the top contributing genes for PC1 and PC2
cat("Top genes for PC1:\n")
print(top_genes_pc1)
cat("Top genes for PC2:\n")
print(top_genes_pc2)



