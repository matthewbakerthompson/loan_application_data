# Loan Data Generation, Analysis, and HTML Export

## Overview

This project showcases the complete workflow for generating synthetic loan data, performing data analysis, and exporting the analysis results to an interactive HTML report. The project consists of the following components:

1. Loan Data Generation: Python script to generate synthetic loan data.
2. Loan Data Analysis: Jupyter Notebook for data exploration and analysis.
3. HTML Export: Python script to convert analysis results into an interactive HTML report.

## Loan Data Generation

The `loans_data_generation.py` script generates synthetic loan data using the Faker library. It simulates various attributes of loan applications, including applicant details, loan amounts, interest rates, and approval statuses. The generated data is saved to a CSV file named `generated_loans_data.csv`.

To run the loan data generation script, execute the following command:

```bash```
python loans_data_generation.py

## Loan Data Analysis

The loan_data_analysis.py performs data analysis on the generated loan data. The file covers the following steps:

1. Loading the generated loan data from generated_loans_data.csv.
2. Exploratory Data Analysis (EDA) to understand the data's characteristics.
3. Visualizations of loan attributes using Matplotlib and Seaborn.
4. Basic statistical analysis and insights.

## HTML Export

The export_to_html.py script takes the analysis results from the Jupyter Notebook and exports them to an interactive HTML report. This report includes visualizations and key findings from the loan data analysis.

To generate the HTML report, run the following command:

```bash``` python export_to_html.py

The exported HTML report will be saved as loan_analysis_report.html.

## Prerequisites

- Python 3.x
- Required Python packages 
  - csv
  - Faker

## Usage
- Generate loan data: Run loans_data_generation.py.
- Perform data analysis: Open and execute loan_data_analysis.py  
- Export analysis to HTML: Run export_to_html.py.
 

## Acknowledgments
- The Faker library for providing synthetic data generation capabilities.
- This project demonstrates the end-to-end process of generating, analyzing, and visualizing loan data.
