# joining numbers in a 'list' using the combine function 
phone <- c(44,123,4567)

# conditionals
message <- "I change based on a condition."
if (TRUE) {
  message <- 'I execute this when true!'
} else {
  message <- 'I execute this when false!'
  }

print(message)

###################

# logical operators & (and), | (or), ! (not)
---
title: "Introduction to R Syntax"
output: html_notebook
---
```{r}

message <- 'Should I pack an umbrella?'
weather <- 'cloudy'
high_chance_of_rain <- TRUE

if (weather == 'cloudy' & high_chance_of_rain
) {
  message <- "Pack umbrella!"
} else {
  message <- "No need for umbrella!"
}

print(message)

#############
#unique values operator, gives back unique value wihtout repeats
data <- c(120,22,22,31,15,120)
unique_vals <- unique(data)
print(unique_vals)

# sqrt() = square root, ceiling() = round up, floor() = round down
olution <- sqrt(49)
print(solution)

round_down <- floor(3.14)
round_up <- ceiling(3.14)
print(round_down,round_up)

########
## you can look up packages at CRAN (comprehensive R archive network). use library() to import

## Calculating population change over time
```{r error=TRUE}
calculate_annual_growth <- function(year_one,year_two,pop_y1, pop_y2,city) {
  annual_growth <- (((pop_y2 - pop_y1) / pop_y1) * 100) / (year_two-year_one)
  message <- paste("From", year_one, "to", year_two, "the population of", city, "grew by approximately", annual_growth, "% each year.")
  return(message)
}

cit_name <- c("Istanbul, Turkey")
pop_year_one <- 691000
pop_year_two <- 15029231
pop_change <- pop_year_two - pop_year_one
percentage_gr <- ((pop_change/pop_year_one)*100)
annual_gr <- percentage_gr/(2017-1927)
print(annual_gr)
# calling function above
calculate_annual_growth(1927, 2017, pop_year_one, pop_year_two, cit_name)


```
# loading libraries for data manipulation
library(readr)
library(dplyr)

#tibble are moderm versions of data frames
#saving csv file into variable
file < read_csv('file.csv')
write_csv(file,'new_csv_file.csv')

#piping data frames
# inspect data frame with pipe
artists %>%
  head()

#select columns
# select multiple columns

group_info <- artists %>%
 select(group,spotify_monthly_listeners,year_founded)
group_info

#selectdf_cols_removed <- artists %>%
 select(-genre,-spotify_monthly_listeners,-year_founded)
df_cols_removed

#filtering multiple groups
opular_rock_groups <- artists %>%
  filter(genre == 'Rock', spotify_monthly_listeners > 20000000)
popular_rock_groups

 filter rows with or
korea_or_before_2000 <- artists %>%
 filter(country == 'South Korea' | year_founded < 2000)
korea_or_before_2000


# filter rows with not !
not_rock_groups <- artists %>%
 filter(!(genre == 'Rock'))
not_rock_groups

#ascending and descending arrangements
group_asc <- artists %>%
 arrange(group)
group_asc


# arrange rows in descending order
youtube_desc <- artists %>%
 arrange(desc(youtube_subscribers))
youtube_desc

# REVIEW
artists <- artists %>%
 select(-country,-year_founded,-albums) %>%
 filter(spotify_monthly_listeners > 20000000, genre != 'Hip Hop') %>%
 arrange(desc(youtube_subscribers))

artists %>%
 head()

# adding a column
# load data frame
dogs <- read_csv('dogs.csv')

# inspect data frame
head(dogs)

# add average height column
dogs <- dogs %>%
 mutate(avg_height = (height_low_inches+height_high_inches)/2)

head(dogs)

# adding multiple columns: add average height, average weight and rank change columns
dogs <- dogs %>%
  mutate(avg_height = (height_low_inches + height_high_inches)/2, avg_weight = (weight_low_lbs+weight_high_lbs)/2, rank_change_13_to_16 = (rank_2016 - rank_2013))
head(dogs)

# update the function call to drop all existing columns
dogs <- dogs %>%
  transmute(breed = breed, avg_height = (height_low_inches + height_high_inches)/2,
         avg_weight = (weight_low_lbs + weight_high_lbs)/2,
        rank_change_13_to_16 = rank_2016 - rank_2013)
head(dogs)

#rename columns
original_col_names <- dogs %>%
 colnames()
original_col_names
```

```{r}
# rename data frame columns
dogs <- dogs %>%
 rename( avg_height_inches = avg_height,avg_weight_lbs = avg_weight, popularity_change_13_to_16 = rank_change_13_to_16)
dogs

new_col_names <- dogs%>%
 names()