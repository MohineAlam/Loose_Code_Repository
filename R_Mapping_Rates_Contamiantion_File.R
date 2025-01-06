# load libraries

# load data in lines of count_reads_of_all_ref.txt
data <- readLines("")

# initialise vectors to store data
categories <- c()
total_reads <- c()
mapped_reads <- c()
unmapped_reads <- c()

# loop through data to parse into vectors ** change category "Total_Reads_*_*_" to accomodate for different named files
for (line in data) {
        if (grepl("Total_Reads", line)) {
                category <- sub("Total_Reads_1245_2_", "", strsplit(line, " ")[[1]][1])
                category <- sub("_.*", "", category)
                read_value <- as.numeric(strsplit(line, " ")[[1]][2])
                categories <- c(categories, category)
                total_reads <- c(total_reads, read_value)
        } else if (grepl("Mapped_Reads", line)) {
                read_value <- as.numeric(strsplit(line, " ")[[1]][2])
                mapped_reads <- c(mapped_reads, read_value)
        } else if (grepl("Unmapped_Reads", line)) {
                read_value <- as.numeric(strsplit(line, " ")[[1]][2])
                unmapped_reads <- c(unmapped_reads,read_value)
        }
}

# check if all data is present and the table is formatted correctly
# then create new data frame
if (length(categories) == length(total_reads) &&
        length(total_reads) == length(mapped_reads) &&
        length(mapped_reads) == length(unmapped_reads)) {
        data_frame <- data.frame(
        Categories = categories,
        Total_Reads = total_reads,
        Mapped_Reads = mapped_reads,
        Unmapped_Reads = unmapped_reads
        )
} else {
        cat("Error! Vectors do not match. There is missing data.\n")
}

# add mapped and unmapped percentage
data_frame$Mapped_Percentage <- (data_frame$Mapped_Reads / data_frame$Total_Reads) * 100
data_frame$Unmapped_Percentage <- (data_frame$Unmapped_Reads / data_frame$Total_Reads) * 100

final_table <- data_frame
# Save the table in output directory
write.csv(final_table, file = "")

# message to user
print(final_table)
print("Table has been created, you can find it in your directory.")
