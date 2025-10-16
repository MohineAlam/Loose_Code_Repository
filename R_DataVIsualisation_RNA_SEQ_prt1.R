# run same code using data set two
# encompasses tutorial 2 - 4

# load data ####
gene_statistical_data = read.table("C:/Downloads/DE_Senes_vs_Prolif.csv",header=TRUE,row.names=1,sep="\t")
gene_expression = read.table("C:/Downloads/EM (1).csv",header=TRUE,row.names=1,sep="\t")
gene_background = read.table("C:/Downloads/Human_Background_GRCh38.p13.csv",header=TRUE,row.names=1,sep="\t")

# MAKE - master table ####
# change the name of gene background symbol to gene_names
new_names = c("SYMBOL","chromosome","start","stop","Sequence_type")
names(gene_background) = new_names
# join tables together
master_pre = merge(gene_expression,gene_background,by.x=0,by.y=0)
master = merge(master_pre,gene_statistical_data,by.x=1,by.y=0)
# save ensemble names
ENSEMBL = master[,1]
# change first column position as header
row.names(master) = master[,8]
# remove repeated column of row.names
master = master[,-1]
# change header to gene names and remove extra column of gene names/SYMBOLS
master$ENSEMBL = ENSEMBL

# change em table header to genes rather the ensemble numbers but using master table
# this will show your gene expression across samples on their own
gene_expression_symbols = master[,1:6]


# CLEAN + ORDER - master ####
# clean and order master table
# remove any N/A results from p value - values too low to calculate
master = na.omit(master)
# sort order by p value
sorted_order_p = order(master[,"p"], decreasing = FALSE)
master = master[sorted_order_p,]

# SORT - by all p + log in master ####
# sort table by significance, add pre processing columns
# add mean expression of all the genes across samples in a column
mean_expression = rowMeans(master[,1:6])
master$mean_expression = mean_expression
# add -log10p column
master$mlog10p = -log10(master$p)
# add column that flags significant genes
# based on p value smaller than 0.05 and log2 fold bigger than 1
master$sig = as.factor(master$p < 0.05 & abs(master$log2fold > 1.0))

# SCALE - all gene expression data ####
# scale your gene expression data 
# making a scaled expression matrix
gene_expression_symbols_scaled = data.frame(t(scale(t(gene_expression_symbols))))
all_gene_expression_scaled = na.omit(gene_expression_symbols_scaled)

# SORT - by p + log and find significant genes ####
# make a list of significant genes from master
#master_ensembl = master
#master_ensembl$SYMBOL = ENSEMBL
significant_genes = subset(master,p.adj < 0.05 & abs(log2fold > 1.0))
# extract names of significant genes from new table
sig_gene_names = row.names(significant_genes)

# SCALE - significant gene expression ####
# make scaled expression table of significant genes only
significant_genes_expression_scaled = all_gene_expression_scaled[sig_gene_names,]

# SAVE - all tables
write.table(all_gene_expression_scaled, file= "C:/Course_data_two/table1.csv",sep="\t")
write.table(significant_genes_expression_scaled, file= "C:/Course_data_two/table1.csv",sep="\t")

#---------------------------------------------------------------------------------------
# MAKING PLOTS ####

#install ggplot2
install.packages("ggplot2")
library(ggplot2)

# make tables for significantly up regulated and downregulated genes
sig_up_reg_genes = subset(master, p.adj < 0.05 & abs(log2fold > 1.0))
sig_down_reg_genes = subset(master, p.adj < 0.05 & abs(log2fold < -1.0))
# Volcano plot with intercepts, adjusted scale, and labels
ggp_volcano = ggplot(master,aes(x=log2fold,y=mlog10p))+
  geom_point(data=master, colour="black")+
  geom_point(data=sig_up_reg_genes,colour="red")+
  geom_point(data=sig_down_reg_genes,colour="blue")+
  geom_hline(yintercept = -log10(0.05),linetype="dashed",colour="grey",size=0.5) + 
  geom_vline(xintercept=1,linetype="dashed") + geom_vline(xintercept=-1,linetype="dashed") +
  labs(title="Volcano Plot",x="log2 fold",y="-log10 p") + 
  theme_bw() + xlim(-20,20) + ylim(0,500)
# now add names of the top 10 genes to the plot to easily recognize them
top_5_up_reg = sig_up_reg_genes[1:5,]
top_5_down_reg = sig_down_reg_genes[1:5,]
# add it alll together
ggp_volcano = ggplot(master,aes(x=log2fold,y=mlog10p))+
  geom_point(data=master, colour="black")+
  geom_point(data=sig_up_reg_genes,colour="red")+
  geom_point(data=sig_down_reg_genes,colour="blue")+
  geom_hline(yintercept = -log10(0.05),linetype="dashed",colour="grey",size=0.5) + 
  geom_vline(xintercept=1,linetype="dashed") + geom_vline(xintercept=-1,linetype="dashed") +
  labs(title="Volcano Plot",x="log2 fold",y="-log10 p") + 
  theme_bw() + xlim(-20,20) + ylim(0,1000)+
  geom_text(data=top_5_down_reg,aes(label=row.names(top_5_down_reg)))+
  geom_text(data=top_5_up_reg, aes(label=row.names(top_5_up_reg)))
ggp_volcano

# CLEAN UP ####
# save plots as png
install.packages("ggrepel")
library(ggrepel)
png("C:/Course_data_two/plot.png", height = 400, width = 400)
print(ggp_volcano)
dev.off()  
