# load libraries
library(ggplot2)

# load data
genome_data <- read.csv("~/mapping_rates_percentage.csv")
contamination_data <- read.csv("~/contamination_mapping_rates_percentage.csv")

# extract genome mapped data
genome_data <- genome_data[,-1]
mapped_to_genome <- genome_data[genome_data$Categories == "Genome",]
head(mapped_to_genome)
unmapped_genome_percentage <- mapped_to_genome[,"Unmapped_Percentage"]
head(unmapped_genome_percentage)

# extract mapped contaminant data
contamination_data <- contamination_data[,-1]
mapped_contamination_percentage <- contamination_data[,"Mapped_Percentage"]
head(mapped_contamination_percentage)
mapped_contamination_names <- contamination_data[,"Categrories"] # FIX NAME
head(mapped_contamination_names)

# Calculate percentage of un-mapped reads that map back to contamination
# (unmapped_genome_percentage * mapped_contamination_percentage) / 100
new_mapped_contamination_percentage <- c()
for (data in mapped_contamination_percentage) {
  mapped_contamination_percentage_value <- (unmapped_genome_percentage * data) / 100
  new_mapped_contamination_percentage <- c(new_mapped_contamination_percentage,mapped_contamination_percentage_value)
}
#head(mapped_contamination_percentage)
#head(new_mapped_contamination_percentage) # new calculated values - contamination % that maps back to unmapped genome %

# message to the user of contamiants mapped
print("Percentage contamination mapping back to unmapped genome reads:")
zip <- function(...){ Map(list,...)}
print2 <- function(...){do.call(cat,c(list(...),"\n"))}
for (item in zip(new_mapped_contamination_percentage, mapped_contamination_names)) {
    print2("contaminant:",item[[2]],item[[1]], "%")
}

# create data frame to plot contamiantion data
# Genome data
Genome <-c(unmapped_genome_percentage)
# contamination data
MappedTo <- c(mapped_contamination_names,"Genome")
Percentage <- c(new_mapped_contamination_percentage,Genome)
contamination_table <- data.frame(
  Mapped_To = MappedTo,
  Percentage = Percentage
)

#head(MappedTo) # names of variables - genome and contaminants
#head(Percentage) # percentage of mapped genome and percentage of mapped reads to unmapped reads

# create graph
custom_colours <- c("black","lightblue","orange") # CHANGE DEPENDING ON VARIABLE NUMBER
contamiantion_plot <- ggplot(contamination_table, aes(x = Mapped_To, y = Percentage, fill = Mapped_To)) +
  theme_classic() +
  geom_bar( stat = "identity") +
  geom_text(aes(label = round(Percentage, 2)), vjust = -0.5, size = 3, color = "black")+
  theme(legend.position = "none", plot.title = element_text(size = 16, hjust = 0.5)) +
  labs(title = "Mapping Rates Contamiantion", x = "Mapped To", y = "Contamiantion Rate %") +
  scale_fill_manual(values = custom_colours)
plot(contamiantion_plot)

output.path <- "~/directory/path"
ggsave(filename = file.path(output.path, "mapping_rates_contamination.png"),
       plot = contamiantion_plot, device = "png", units = "in", width = 8, height = 4, dpi = 350)
