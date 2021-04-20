# Using SQL and Plotly in Python to explore production data in the Williston Basin of North Dakota

## Useful Information

Enclosed is a Jupyter Notebook with all of the SQL statements and the functions I used to plot the production. I cannot provide the raw dataset as it is dervied from a website with a paid subscription, however I do cover the project where I scraped this data [here](https://github.com/johnodonnell123/Personal_Projects/tree/master/Scraping%20Oil%20Production%20with%20Scrapy). A more thorough walkthrough can be found [here](https://johnodonnell123.github.io/pages/page_EDA.html).

## Problem Statement 
Data for 15,000 oil and gas wells in the Williston Basin is avaliable for analysis via our SQL database. We would like to explore the dataset for high level summary statistics and also view the production of wells through time. 

## Methodology
SQL is used to retrieve data from two separate but related tables. One table contains general well information while the other contains prouction volumes through time for each well (time-series).`JOIN` statements combine these two tables and `GROUP BY` statements are used to aggregate oil production by several different variables. Production is aggregated for different operators (companies) and different parts of the basin (indicative of the geologic influence of the area). Two DataFrames are created from each table and functions are defined to create plots drawing from each of them. Simple production plots are created as well as more complex views that allow us to average the time-series data when binned by other features.

## Unique Challanges and Solutions:
1. Working with tabular and time-series data has unique challenges, outright joining them creates an very large DataFrame that becomes unweildy
2. Production Data is reported in months, with number of producing days for each month. The best representation of producing time is to create an array of the cumulative producing days, however this makes averaging across different wells difficult. Linear interpolation is used to generate "monthly" values every 30.4 days which are then used for averaging. 

## Result / Value
The result of this workflow yields an insighful view into the oil production state of the Williston Basin. Top operators in terms of oil production and asset development efficiency are identified. Production is viewed for several wells, and strong trends with depth and well vintage are highlighted. Oil production is plotted spatially and the influence of geology becomes clearly visible. 
