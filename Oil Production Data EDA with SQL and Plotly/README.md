# Using SQL and Plotly in Python to explore production data in the Williston Basin of North Dakota

## Useful Information

Enclosed is a Jupyter Notebook with all of the SQL statements and the functions I used to plot the production. I cannot provide the raw dataset as it is dervied from a website with a paid subscription. A more thorough walkthrough can be found [here](https://johnodonnell123.github.io/pages/page_EDA.html).

## Problem Statement / Value

Interpretation of well log data can be a very time consuming and biased process. It is not uncommon for a petrophysicist to have to interpet thousands of logs all with tens of 
thousands of feet of data. If you ask two people to interpret the same data set you will recieve wildly different results. These interpretations are often used in reservoir 
simlulation and in the forecasting of oil production for wells, making them very important in any corporate model. K-means allows us to make this process faster, more accurate,
and repeatable. There is still room for interpretation, however it is reasonably bounded and arguably easier to explain. 

## Methodology

Log data for one well is imported into a Pandas DataFrame. Irrelevent logs are then removed, and what is left is cleaned. The data is then standardized to remove scaling bias and
a K-Means clustering algorithm is fit to the dataset. The results are viewed in a log plot, and the clusters are interpreted to be distinct rock types.

## Unique Challanges and Solutions:
  1. Rocks are a mixed medium comprised of various proportions of minerals. It is rare to have a homogenous layer that is thick enough to be read by logging tools. This makes the determination of the number of clusters difficult as our groups are rarely easily defined graphically. That being said, the results of using K-Means do represent unique rock types and viewing the results is much more intuitive with a log plot. It is best to approach the workflow iteratively, and modify the number of clusters with an exploration mindset. This requires domain knowledge of the logs and rock types.
 
## Result / Value

The result is a new log comprised of clusters that represent rock types. This information can be used for a host of purposes including:
- Well Planning: When drilling a well we need to know what types of rocks we are going through
- Wellbore Stability: Salt costs operators millions of dollars due to its impact on the integrity of the wellbore
- Reservoir Mapping: Understanding when a facies appears/thickens/changes would cause an M&A team to value some areas more than others
- Reservoir Characterization: Some rock types (clusters) have different properties such a permeability which have a strong influence of production and how we might forecast cash flows from a well
