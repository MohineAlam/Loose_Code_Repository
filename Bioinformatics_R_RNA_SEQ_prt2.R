# Encompasses tutorial 5-8
# run same code using set two data
library(ggplot2)

# Volcano plot touch ups ####
# add colour to the top 10 gene names
ggp_volcano = ggplot(master,aes(x=log2fold,y=mlog10p))+
  geom_point(data=master, colour="black")+
  geom_point(data=sig_up_reg_genes,colour="red")+
  geom_point(data=sig_down_reg_genes,colour="blue")+
  geom_hline(yintercept = -log10(0.05),linetype="dashed",colour="grey",size=0.5) + 
  geom_vline(xintercept=1,linetype="dashed") + geom_vline(xintercept=-1,linetype="dashed") +
  labs(title="Volcano Plot",x="log2 fold",y="-log10 p") + 
  theme_bw() + xlim(-20,20) + ylim(0,1000)+
  geom_text(data=top_5_up_reg, aes(label=row.names(top_5_up_reg), colour="blue"), show.legend=FALSE)+
  geom_text(data=top_5_down_reg,aes(label=row.names(top_5_down_reg), colour="red"), show.legend=FALSE)
  
# Making MA plot ####
ggp_MA = ggplot(master,aes(x=mean_expression,y=log2fold)) +
  geom_point(data=master, colour="black") +
  geom_point(data=sig_up_reg_genes, colour="red") +
  geom_point(data=sig_down_reg_genes, colour ="blue")+
  scale_colour_manual(values=c("red","blue"))+
  geom_hline(yintercept = 1,linetype="dashed",colour="grey",size=0.5)+
  geom_hline(yintercept = -1,linetype="dashed",colour="grey",size=0.5)+
  labs(title="MA plot",x="log10 mean expression",y="log2 fold")+
  theme_bw()+ 
  geom_text(data=top_5_down_reg,aes(label=row.names(top_5_down_reg), colour="Up regulated"),show.legend=FALSE)+
  geom_text(data=top_5_up_reg, aes(label=row.names(top_5_up_reg), colour="Down regulated"),show.legend=FALSE)


# Making PCA plots #################

# make PCA coordinates
# make PCA table, make gene_expression table a matrix of numerics
as.matrix(sapply(all_gene_expression_scaled,as.numeric))

pca = prcomp(t(all_gene_expression_scaled))
pca_coordinates = data.frame(pca$x)

# adding percentage variable
vars = apply(pca$x, 2, var)
prop_x = round(vars["PC1"] / sum(vars),4) * 100
prop_y = round(vars["PC2"] / sum(vars),4) * 100
x_axis_label = paste("PC1 ", " (",prop_x, "%)",sep="")
y_axis_label = paste("PC2 ", " (",prop_y, "%)",sep="")

# update gpca_coordinates table, add the sample column: Load sample sheet - 
sample_sheet = read.table("C:/Users/malam/Downloads/sample_sheet (1).csv",header=TRUE,sep="\t")

# add the sample column to the table
pca_coordinates$sample = sample_sheet$SAMPLE

# making PCA plot
library(ggplot2)
pca_plot = ggplot(pca_coordinates,aes(x=PC1, y=PC2, colour = sample_sheet$SAMPLE_GROUP)) + 
  geom_point() + 
  scale_color_manual(values=c("orange","blue","red")) +
  geom_text(aes(label=sample_sheet$SAMPLE), show.legend = FALSE) +
  labs(title="PCA plot, PC1 vs PC2",x="PC1 57.49%",y="PC2 18.96%",colour="Groups") + 
  theme_bw()

# Faceting #############
# Make expression density plot for each gene across samples 
# use facet function

# install and load reshape library
install.packages("reshape2")
library(reshape2)


# melt em table to gain two columns
gene_expression_m = melt(gene_expression)

# make plot
facet_plot = ggplot(gene_expression_m, aes(x=(log10(value+0.01)))) +
  facet_wrap(~variable, ncol=9) +
  geom_density(size=0.5,alpha=0.5) +
  theme_bw()
#---------------------------------------------------------------------------------------------
# Boxplot ####
# Making box plots for single gene expressions across the different samples

TSPAN6_expression = gene_expression_symbols["TSPAN6",]
TSPAN6_expression = data.frame(t(TSPAN6_expression))
TSPAN6_expression$sample_group = sample_sheet$SAMPLE_GROUP
names(TSPAN6_expression) = c("expression","sample_group")

# the graph is ordered by levels, to see current levels
levels(TSPAN6_expression$sample_group)
# modify order
TSPAN6_expression$sample_group = factor(TSPAN6_expression$sample_group, levels=c("Prolif","Senes"))
# make the box plot
ggp_box_plot = ggplot(TSPAN6_expression, aes(x=sample_group,y=expression,colour=sample_group))+
  geom_boxplot(size = 0.5, outlier.size = 0, alpha = 0.5, colour=c("red","blue"))
ggp_box_plot

# Violin plot ####
# make a violin plot
ggp_violin_plot = ggplot(TSPAN6_expression, aes(x=sample_group,y=expression,fill=sample_group))+
  geom_violin(width = 0.5, alpha = 0.5, trim=FALSE, show.legend=FALSE)+
  scale_fill_manual(values=c("red","blue"))

# Jitter plot ####
# make a jitter plot
ggp_jitter_plot = ggplot(TSPAN6_expression, aes(x=sample_group,y=expression,fill=sample_group))+
  geom_jitter(width=0.1)

# Make a box plot for 10 genes
gene_1_10 = gene_expression_symbols_scaled[1:10,]
gene_1_10 = data.frame(t(gene_1_10))
gene_1_10$sample_group = sample_sheet$SAMPLE_GROUP
# order samples
gene_1_10$sample_group = factor(gene_1_10$sample_group, levels = c("Prolif","Senes"))
# melt your table to have two columns
library(reshape2)
gene_1_10.m = melt(gene_1_10, id.vars="sample_group")
# make your box plot
ggp_bp_gene1_10 = ggplot(gene_1_10.m, aes(x=variable,y=value,colour=sample_group))+
  geom_boxplot()

# now a multifaceted plot of density graphs
ggp_bp_gene1_10 = ggplot(gene_1_10.m, aes(x=sample_group,y=value,colour=sample_group))+
  geom_boxplot()+
  theme(axis.text.x = element_text(angle = 45, hjust = 1))+
  facet_wrap(~variable, ncol=9)

#------------------------------------------------------------------------

# Heat maps ####

# use significant genes that have been scaled - make matrix
hm_matrix = as.matrix(significant_genes_expression_scaled)
# adjust parameters of matrix
# make colour pallete
colours = c("yellow","blue")
# now cluster data - this orders data in significant groups
# download multidimentional analysis package
install.packages("amap")
library(amap)
# get correlation for each gene
y.dist = Dist(hm_matrix,metho="spearman")
# perform clustering using distances (build dendogram)
y.cluster = hclust(y.dist, method="average")
# extract dendogram
y.dd = as.dendrogram(y.cluster)
# reorder dendrogram
y.dd.reorder = reorder(y.dd,0,FUN="average")
# use new gene order
y.order = order.dendrogram(y.dd.reorder)
# now use new order to make a heat map matrix
hm_matrix_clustered = hm_matrix[y.order,]
# now melt the plot as before
hm_matrix_clustered = melt(hm_matrix_clustered)
# now make heat map
ggp_heat_map = ggplot(hm_matrix_clustered, aes(x=Var2,y=Var1,fill=value))+
  geom_tile()+
  scale_fill_gradientn(colours = colorRampPalette(colours)(100))+
  ylab("Genes") + xlab("Samples") +
  theme(axis.text.y = element_blank(), axis.ticks=element_blank(), legend.title = element_blank(), 
        legend.spacing.x = unit(0.25, 'cm'))

# Rug ###
# make a rug to supplement the heat map

# matrix of your table
group_data = as.matrix(as.numeric(as.factor(sample_sheet$SAMPLE_GROUP)))
group_data = melt(group_data)
# make the heat map
rug_colours = c("yellow","blue")
ggp_hm_rug = ggplot(group_data,aes(x=Var1,y=Var2,fill=value)) +
  geom_tile() +
  scale_fill_gradientn(colours = colorRampPalette(rug_colours)(100))+
# tidy up panel
  theme(plot.margin=unit(c(0,1,1,1), "cm"), 
        axis.line=element_blank(),axis.text.x=element_blank(),axis.title.x=element_blank(),axis.text.y=element_blank(),
        axis.ticks=element_blank(),axis.title.y=element_blank(),legend.position="none",panel.background=element_blank(),panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),plot.background=element_blank())
#--------------------------------------------------------------------- extra
# match rug to variables, use function that gets default gglot colours
gg_color_hue <- function(n) {
  hues = seq(15, 375, length = n + 1)
  hcl(h = hues, l = 65, c = 100)[1:n]
}

# use function to get colours
rug_colours = gg_color_hue(3)

# colours will now be the same used in PCA
rug_colours = c(rug_colours[3],rug_colours[2], rug_colours[1])

#---------------------------------------------------------------------
# Make over representation analysis ####
# dot plot, bar plot, go plot, cnetplot

#install.packages("BiocManager")
#BiocManager::install("clusterProfiler")
#BiocManager::install("org.Mm.eg.db")
library(clusterProfiler)
library(org.Mm.eg.db)

# plot significant gene values
# first convert the name SYMBOLS to ENTREZ
sig_genes_entrez = bitr(sig_gene_names, fromType = "SYMBOL", toType = "ENTREZID", OrgDb = org.Mm.eg.db)
# run over representation analysis ORA
pathway_results = enrichGO(gene = sig_genes_entrez$ENTREZID, OrgDb = org.Mm.eg.db, readable = T, ont = "BP", pvalueCutoff = 0.05, qvalueCutoff = 0.10)
# now plot your graphs
ggp_bp = barplot(pathway_results, showCategory=10)
ggp_dp = dotplot(pathway_results, showCategory=10)
ggp_gp = goplot(pathway_results, showCategory = 10)
ggp_cnp = cnetplot(pathway_results, categorySize="pvalue")

# now run over representation analysis - which tells you which pathways these genes are upregulated or downregulated in
# run in up and down regulated genes to see which pathway they belond to and by how much they are increased
# now run ORA separately on up or down regulated genes ####

# upregulated
name_sig_genes_up = row.names(sig_up_reg_genes)
sig_genes_up_entrez = bitr(name_sig_genes_up, fromType = "SYMBOL", toType = "ENTREZID", OrgDb = org.Mm.eg.db)
pathway_results_up = enrichGO(gene = sig_genes_up_entrez$ENTREZID, OrgDb = org.Mm.eg.db, readable = T, ont = "BP", pvalueCutoff = 0.05, qvalueCutoff = 0.10)

ggp_bp_up = barplot(pathway_results_up, showCategory=10)
ggp_dp_up = dotplot(pathway_results_up, showCategory=10)
ggp_gp_up = goplot(pathway_results_up, showCategory = 10)
ggp_cnp_up = cnetplot(pathway_results_up, categorySize="pvalue")

# down regulated
name_sig_genes_down = row.names(sig_down_reg_genes)
sig_genes_down_entrez = bitr(name_sig_genes_down, fromType = "SYMBOL", toType = "ENTREZID", OrgDb = org.Mm.eg.db)

pathway_results_down = enrichGO(gene = sig_genes_down_entrez$ENTREZID, OrgDb = org.Mm.eg.db, readable = T, ont = "BP", pvalueCutoff = 0.05, qvalueCutoff = 0.10)

ggp_bp_down = barplot(pathway_results_down, showCategory=10)
ggp_dp_down = dotplot(pathway_results_down, showCategory=10)
ggp_gp_down = goplot(pathway_results_down, showCategory = 10)
ggp_cnp_down = cnetplot(pathway_results_down, categorySize="pvalue")


