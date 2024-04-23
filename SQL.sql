from multiprocessing import JoinableQueue
from tkinter import BROWSE, ON
import 

# exploring data with sql
SELECT * # selects all database value - it means all columns
FROM BROWSE # from specific column
LIMIT 10; #first 10 variables

# Usage funnels 
SELECT 
 ROUND(100 * COUNT(DISTINCT c.user_id)) / COUNT(DISTINCT b.user_id) AS browse_to_checkout_percentage
 ROUND(100 * COUNT(DISTINCT p.user_id)) / COUNT(DISTINCT c.user_id) AS check_out_to_percentage
FROM browse b #selecting from specific column
LEFT JOIN checkout c # add data into table, left side
ON b.user_id = c.user_id # joining checkout c onto b and c user id data
LEFT JOIN purchase p
ON c.user_id = p.user_id; # join purchase p data to c and p user id

# Determining web traffic atribution
SELECT utm_source, #website/search tool
 COUNT(DISTINCT user_id) AS num_users #giving number of users
FROM page_visits #from this column
GROUP BY 1 #groups variables from page_visits into one column
ORDER BY 2 DESC;#orders into second columnn and describes group 1

# When adding columns into table
# example is database of different restauraunts

SELECT name,
CASE 
WHEN review > 4.5 THEN 'Excellent'
WHEN review > 3 THEN 'Good'
ELSE 'Poor'
END AS 'Review'
FROM 'Nomnom';

# Finding specific cusine in table from the cuisine column

SELECT *
FROM nomnom
WHEN cuisine = 'Chinese';

# Finding null values (empty)

SELECT *
FROM nomnom
WHERE health IS NULL;

# Select specific information from a column to only be shown
SELECT *
FROM nomnom
WHERE neighborhood = 'Midtown'
OR neighborhood = 'Downtown'
OR neighborhood = 'Chinatown';

# Find something that has similar words inside its strings

SELECT *
FROM nomnom
WHERE name LIKE '%meatball%';

# Counting number of values e.g. how many free apps there are in this table of apps
SELECT COUNT(*)
FROM fake_apps
WHERE price = 0;

# give back sum of all those values in that column
SELECT SUM(downloads)
FROM fake_apps;

# Max and minumum - MAX()/MIN() give back most or least values of a column
SELECT MAX(downloads)
FROM fake_apps;

# avg() function takes column name as an argument and gives back average value for that column
SELECT AVG(price)
FROM fake_apps;

#average and round function in one arguement
SELECT ROUND(AVG(price),2)
FROM fake_apps;

# aggregate coding, grouping and counting

SELECT price, COUNT(*)
FROM movies
GROUP BY price