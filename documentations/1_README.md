Day 1 - Project Setup and Exploratory Data Analysis
Project: Phishing URL Detection using Machine Learning
Objectives
Set up the project environment.
Load and inspect the phishing dataset.
Perform Exploratory Data Analysis (EDA).
Understand the distribution of phishing and legitimate websites.
Analyze feature relationships and data quality.
Tasks Completed
1. Environment Setup

Installed and imported the required libraries:

pandas
numpy
matplotlib
seaborn
scikit-learn
2. Dataset Loading

Loaded the phishing dataset into a Pandas DataFrame and inspected:

Number of rows and columns
Data types
Missing values
Duplicate records
3. Exploratory Data Analysis

Performed the following analyses:

Class distribution analysis
Feature value distribution
Correlation analysis
Identification of important URL-based features
Detection of missing or inconsistent values
4. Key Observations
The dataset contains both legitimate and phishing websites.
Several URL-based features show strong correlation with phishing behavior.
Some features can be extracted directly from URLs while others require HTML content or external services such as WHOIS and SSL information.
Features Categorization
URL-Based Features

These can be extracted directly from the URL:

URL length
Number of dots
Number of hyphens
Presence of IP address
Number of subdomains
Presence of special characters
HTML-Based Features

These require webpage scraping:

External resource ratio
Number of links
Forms and redirects
Favicon source
