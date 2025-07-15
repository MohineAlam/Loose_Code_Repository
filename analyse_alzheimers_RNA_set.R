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

#========================================= fetch data from GSEO using GSE33000
gse <- getGEO("GSE33000", GSEMatrix = TRUE)

# Check the structure of the data
gse

#========================================== extract expression matrix and metadata
expr <- exprs(gse[[1]])
meta <- pData(gse[[1]])
# show first few rows
head(meta)
head(expr)

#============================================ convert expression matrix to DESeq object
# deseq requires data set to be a count matrix
# if data set is already normalised you can skip this step (TPM/FPKM)
dds <- DESeqDataSetFromMatrix(countData = expr,
                              colData = meta,
                              design = ~ condition)

# Pre-filtering: Remove genes with low counts across all samples
dds <- dds[rowSums(counts(dds)) > 10,]

#======================== normalise datset and check sample wise distribution
# Variance stabilisation (vsd) normalisation
vsd <- vst(dds, blind = FALSE)

# Plot distance matrix
sampleDists <- dist(t(assay(vsd)))
pheatmap(as.matrix(sampleDists), labels_row = meta$condition, main = "Sample-to-Sample Distance")

# PCA plot
plotPCA(vsd, intgroup = "condition") + ggtitle("PCA of Samples")

#============================================= perform differential expression analysis
dds <- DESeq(dds)
res <- results(dds, contrast = c("condition", "AD", "control"))
res <- lfcShrink(dds, coef=2, res=res)

# View results
summary(res)

# volcano plot
res_df <- as.data.frame(res)
res_df$gene <- rownames(res_df)

ggplot(res_df, aes(x=log2FoldChange, y=-log10(padj))) +
  geom_point(alpha=0.4) +
  geom_point(data = subset(res_df, padj < 0.05 & abs(log2FoldChange) > 1),
             aes(x=log2FoldChange, y=-log10(padj)), color = "red") +
  theme_minimal() +
  xlab("log2 Fold Change") + ylab("-log10 adjusted p-value") +
  ggtitle("Volcano Plot")

#======================================= heat map of top genes
# Select top significant genes
topGenes <- head(order(res$padj), 20)
mat <- assay(vsd)[topGenes, ]

# Plot heatmap
pheatmap(mat, scale = "row", annotation_col = meta[, "condition", drop = FALSE],
         show_rownames = TRUE, show_colnames = FALSE, main = "Top 20 DE Genes")

#=================================== pathway enrichment analysis
# Select significant genes
sig_genes <- rownames(subset(res, padj < 0.05 & abs(log2FoldChange) > 1))

# Convert gene symbols to Entrez IDs
gene_ids <- mapIds(org.Hs.eg.db,
                   keys = sig_genes,
                   column = "ENTREZID",
                   keytype = "SYMBOL",
                   multiVals = "first")

#================================= GEO biological process enrichment
ego <- enrichGO(gene         = gene_ids,
                OrgDb        = org.Hs.eg.db,
                keyType      = "ENTREZID",
                ont          = "BP",
                pAdjustMethod = "BH",
                qvalueCutoff  = 0.05,
                readable     = TRUE)

# Barplot for top GO terms
barplot(ego, showCategory=10, title = "GO Biological Process")

#=================================== KEGG pathway enrichment
ekegg <- enrichKEGG(gene = gene_ids,
                    organism = 'hsa',
                    pvalueCutoff = 0.05)

# Barplot for top KEGG pathways
barplot(ekegg, showCategory=10, title = "KEGG Pathways")


