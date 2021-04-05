# Scraping Production Data for Oil and Gas Wells and Storing the Results in a RDBS

## Useful Information

Enclosed is a Scrapy project folder containing all of the necessary content used in this project. 
This project uses two spiders to scrape data for ~15,000 oil wells from a government run webpage, and pipeline the results into a relational database (SQLite3)

This is the first in a sequence of mini-projects in which I go on to [query this database](https:linkhere) and [perform EDA](https://linkhere2)

## Problem Statement

We need quick and reliable access for data on Oil and Gas wells in a given region. 
This information is avaliable on a government run website, but there is no way to export this data, making an analysis over thousands of wells impossible.
Our goal is to take this data and store it in a database that is more suitable for querying and analysis, a common first step in projects.

## Methodology

Two Scrapy Spiders are generated and used to crawl a differnt dataset. One will retrieve headers (general info) and the other production data (volumes through time).
Scrapy pipelines will be used to store these datasets into a local, lightweight database (SQLite 3)

## Unique Challanges and Solutions:
  1. The website requres authentication: Default request headers are overwritten and basic credentials are provided with base64 encoding
  2. Links to other pages are not found on any page: Python list compregensions are used to create a list of URLs to crawl, concatenating query strings
  3. We have time series data as well as traditional: Two spiders are used with two pipelines to populate two tables in a relational database that share a key
  4. The fields are not always in the same order on each page: xPath expressions are used to be very specific and select nodes by text, then get thier following-sibling nodes/attributes
  5. Chrome inserted <td> tags into the HTML in the developer tools, causing many queries to return nothing: These tags were replaced with "/?

## Result/Value

The result is a local, lightweight database that contains all of the relevent information we need. 
The database houses both of our datasets and allows for quick and easy data querying and analysis of both tables. 
