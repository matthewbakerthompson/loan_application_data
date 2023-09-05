"""
Author:  Matthew Thompson [matthewbakerthompson@gmail.com]
Date:    9.4.2023 
Title:   Loan Application Data Quality Analysis 
Purpose: This script performs data quality checks and generates visualizations for a synthetic finance dataset. It also generates an html output which provides a data summary.
         The report includes a range of visualizations and insights that help analysts understand the dataset, identify potential issues, and make informed decisions during data analysis.

  
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport

# Display basic information about the dataset
def dataset_summary(dataframe):
    summary = dataframe.describe(include='all')
    return summary

# Visualize missing data
def visualize_missing_data(dataframe):
    missing_percentage = (dataframe.isnull().sum() / len(dataframe)) * 100
    missing_data = pd.DataFrame({'Missing Percentage': missing_percentage})
    missing_data = missing_data.sort_values(by='Missing Percentage', ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=missing_data.index, y='Missing Percentage', data=missing_data)
    plt.xticks(rotation=90)
    plt.title('Missing Data Percentage')
    plt.xlabel('Columns')
    plt.ylabel('Percentage')
    plt.tight_layout()
    plt.show()

# Visualize data distribution in numerical column buckets
def visualize_bucketing(dataframe, column):
    plt.figure(figsize=(10, 6))
    plt.hist(dataframe[column], bins=20, edgecolor='k', alpha=0.7)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# Data quality check: Duplicate records
def duplicate_record_check(dataframe):
    duplicate_count = dataframe.duplicated().sum()
    duplicate_rows = dataframe[dataframe.duplicated()]
    return f"{duplicate_count} duplicates found.\n", duplicate_rows

# Data quality check: Data type consistency
def data_type_check(dataframe):
    inconsistent_types = []
    for column in dataframe.columns:
        unique_types = dataframe[column].apply(type).unique()
        if len(unique_types) > 1:
            inconsistent_types.append(f"Column '{column}' has inconsistent data types: {unique_types}")
    return inconsistent_types

# Data quality check: Check for missing values in specific columns
def missing_values_in_columns(dataframe):
    columns_to_check = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed']
    missing_info = []
    for column in columns_to_check:
        missing_count = dataframe[column].isnull().sum()
        missing_info.append(f"Column '{column}' has {missing_count} missing values.")
    return missing_info

# Customized data quality report with visualizations
def generate_data_quality_report(dataframe):
    report = {
        'Dataset Summary': dataset_summary(dataframe),
        'Duplicate Records': duplicate_record_check(dataframe),
        'Missing Data Visualization': visualize_missing_data(dataframe),
        'Data Type Consistency Check': data_type_check(dataframe),
        'Missing Values in Columns Check': missing_values_in_columns(dataframe),
    }
    return report

if __name__ == "__main__":
    # Load the synthetic finance dataset with FICO scores
    data_path = r'C:\Users\terry\OneDrive\Documents\data\economic\expanded_loan_app_data_with_fico.csv'
    df = pd.read_csv(data_path)

    # Generate the data quality report
    data_quality_report = generate_data_quality_report(df)
    print("\nLoan Application Data Quality Report:")
    for section, content in data_quality_report.items():
        print(f"\n{section}:\n{content}")

    # Create an HTML report using ydata-profiling
    report_title = "Loan Application Data Quality Report"  # Edit this title
    profile = ProfileReport(df, title=report_title)
    profile.to_file("data_quality_report.html")
