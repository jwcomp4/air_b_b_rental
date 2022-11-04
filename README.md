# Airbnb Rental

## Team Members:
#### _**Colt Korth**_
#### _**Danielle Fulgenzi**_
#### _**Erin Neubauer**_
#### _**John Compton**_

&nbsp;

## Project Description/Outline:
+ Users will be able to enter in their potentially new rental space and receive a competitive price to list at. 
+ Users can view/fiter the overall Nashville listings for Nashville TN
+ Currently using a regression model because our target feature (Airbnb price) is a continuous variable.
+ Preprocessing has involved the following:
    - Deleting listings without reviews in the current year.
    - Drop columns unnecessary for machine learning model: 
        - host_id
        - latitude
        - longitude
    - Drop major outlier (listing with a price over $9k/night).
    - Drop null values.

&nbsp;

## Research Questions to Answer:
1. What is the greatest factor in price between listed Airbnbs?

2. What would be a competitve price for a new host user, given data they enter about their rental space?

&nbsp;

## Data Set to be Used:
Our data came from [Inside Airbnb](http://insideairbnb.com/get-the-data/) 
    - [ctrl + F] “Nashville” | “Show Archived Data”
    - Inside Airbnb is not formally associated with Airbnb, but actively scrapes data from the the Airbnb website.

 The dataset(s) contains information pulled from "Host" users in the Nashville TN area. The original dataset is divided in 4 fiscal quarters (Q4'21, Q1'22, Q2'22, Q3'22,). 

## Segment Tasks
Please review each segment file in the presentation branch to see the breakdown duties for each team member. 
