"""
Author: Matthew Thompson [matthewbakerthompson@gmail.com]
Date: 9.4.2023 
Title: Loan Application Data Generation 
Purpose: This script generates a synthetic finance dataset for loan application analysis and data quality reporting.
   
"""


import pandas as pd
import numpy as np

# Generate synthetic finance dataset with additional columns
np.random.seed(42)
num_records = 5000

data = {
    'Loan_ID': ['LP{:04}'.format(i) for i in range(1, num_records + 1)],
    'Gender': np.random.choice(['Male', 'Female'], size=num_records),
    'Married': np.random.choice(['Yes', 'No'], size=num_records),
    'Dependents': np.random.choice(['0', '1', '2', '3+'], size=num_records),
    'Education': np.random.choice(['None', 'High School', 'Some College', 'College', 'Graduate'], size=num_records),
    'Self_Employed': np.random.choice(['Yes', 'No'], size=num_records),
    'ApplicantIncome': np.random.randint(9000, 235001, size=num_records),
    'CoapplicantIncome': np.random.randint(9000, 235001, size=num_records),
    'LoanAmount': np.random.randint(500, 45001, size=num_records),
    'Loan_Amount_Term': np.random.choice([120, 240, 360], size=num_records),
    'Credit_History': np.random.choice([0, 1], size=num_records),
    'Property_Area': np.random.choice(['Urban', 'Semiurban', 'Rural'], size=num_records),
    'Loan_Status': np.random.choice(['Y', 'N'], size=num_records),
    'FICO_Score': np.random.randint(300, 851, size=num_records)
}

df = pd.DataFrame(data)

# Save the synthetic dataset to a CSV file
data_path = r'C:\Users\terry\OneDrive\Documents\data\economic\expanded_loan_app_data_with_fico.csv'
df.to_csv(data_path, index=False)

print("Synthetic finance dataset with FICO scores generated and saved.")
