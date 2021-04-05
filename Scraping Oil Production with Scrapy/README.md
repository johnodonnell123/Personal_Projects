# Scraping Production Data for Oil and Gas Wells and Storing the Results in a RDBS

## Useful Information

Enclosed is a Scrapy project folder containing all of the necessary content used in this project. 
This project uses two spiders to scrape data for ~15,000 oil wells from a government run webpage, and pipeline the results into a relational database (SQLite3)

This is the first in a sequence of mini-projects in which I go on to [query this database](https:linkhere) and [perform EDA](https://linkhere2)

## Problem Statement

We need quick and reliable access to production data avaliable for oil and gas wells in a given area. 
This information is avaliable on a webpage, but there is no easy way to export this data and the format it is currently in is not suitable for analysis. 
The structure of the pages are slighly different between wells, as some wells are missing data and the field is completely omitted.
We are interested in two sets of data, general information on the well (location/name/etc) and the production data (monthly reported volumes through time).

## Methodology

I generated two Scrapy Spiders to collect data for these datasets. 
The website provides a list of file numbers that we can filter down, and then append onto the tail end of a URL to access the webpage.
For the general well information I used xPath notation to determine if the field I wanted to scrape existed on the page, then yield the following sibling nodes text attribute. 
The production information was more straightforward as it existed in a table. I simply iterated through the rows of the table, yielding the relevent data.
Finally, I used two pipelines to create and fill tables in a SQLite3 database for each dataset.

## Result/Value

The result is a local, lightweight database that contains all of the relevent information we need. 
The database houses both of our datasets and allows for quick and easy data querying and analysis of both tables. 
