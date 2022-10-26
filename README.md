# AirBnB Rental

## Team Members:
#### Erin Neubauer
#### Danielle Fulgenzi
#### John Compton
#### Colt Korth

## Project Description/Outline:
    + Users will be able to enter in their potentially new rental space and receive a competitive price to list. 
    + Users can view/fiter the overall Nashville listings for Nashville TN

## Research Questions to Answer:
    Room Type vs Pricing
    Neighborhood vs Pricings
    Predicting Rental price (for new properties that come on the market?)

## Data Sets to be Used:
    // [Link to data file here]
    http://insideairbnb.com/get-the-data/
    [ctrl + F] “Nashville”
    “Show Archived Data”
### Cleaning Data Set:
    + Drop Columns: "host_id", "host_name", "neighbourhood_group", "calculated_host_listings_count", "license".


## Rough Breakdown of Tasks:
### Segment #1

### Square Role - Repository - John Compton
    + Team Branches in Github
    + Move Finish Code to Main branch 

### Triangle Role - Machine Learning Model - Danielle Fulgenzi
    + Rough Model
    + Most useful fields to use from data
    + Which algorithm to use
      - (un)Supervised?
    + Price predictor for rentals

## Circle Role - Database - Erin Neubauer
    + Merge 4 csv sets
    + ERDs
    + Quarterly sets for timeline

## X Role - Technology Planning - Colt Korth
    + Data Cleaning and Analysis
    + SQL to merge data sets into single year csv and quarterly csv
    + Pandas to Clean up special characters and duplicate data
    + DataBase Storage
    + Mongo to hold the data and integrate with Flask?
    + Machine Learning
      - [Library] [algorithm] 
    + Dashboard
    - Flask? Tableau? Hosted on ___? 
