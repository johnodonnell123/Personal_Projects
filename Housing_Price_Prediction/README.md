# Module 2 Final Project

## Introduction
In this project, data for ~20,000 homes in Kings County, Seattle is used to create a linear regression model in the attempt to predict the sale price of a home. 

A blog post about this project can be found [here](https://johnodonnell123.github.io/pages/page_blogpost_2.html)

## Data:
The data was provided by Flatiron School, originally sourced from Kaggle. Features include:
- Sale Price
- Sale Date
- Bedrooms
- Bathrooms
- Sqare footage (living, basement, lot)
- Floors
- Waterfront (Boolean)
- Number of views
- Condition 
- Grade
- Year Built
- Year Renovated
- Zipcode
- Latitiude / Longitude
- Square Footage of 15 nearest neighbors (house/lot)

## Methodology:
I began with a typical workflow in which I cleaned the data, explored it visually, performed some feature engineering, transformed/scaled values, then created a regression model. After doing this, I was curious to see how each of these steps really impacted the models prediction and inference, so I decided to turn each of these steps into functions. I then iteratively built models either omitting or changing the parameters to each function to quantify the impact of each. 

## EDA Findings:

### The housing market shows a strong trend of seasonality in terms of number of houses sold:

 <img src="images/sale_date_histogram.PNG?raw=true" width="75%" height="75%">
 
### Houses near specific water features appear to sell for higher prices:

<img src="images/map_figure.PNG?raw=true" width="50%" height="50%">

### The number of floors in a home appears to have a quadratic relationship with the sale price of the home:

 <img src="images/price_vs_floors.PNG?raw=true" width="50%" height="50%">
 
## Model Findings:

### The model was able to explain nearly 90% of the variation in sale price:

<img src="images/predictions_vs_actuals_scatter.PNG?raw=true" width="50%" height="50%">

### Trimming outliers has a marginal impact on model performance, and could lead to spurious relationships:

<img src="images/model_performance_trimmed.PNG?raw=true" width="50%" height="50%">

### Feature Enginering with zip code and log normalizing our distributions have a marked impact on model performance:

 <img src="images/model_performance_features_engineered_log_transformed.PNG?raw=true" width="50%" height="50%">
 


