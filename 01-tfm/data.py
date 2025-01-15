# Regenerate necessary setup after code execution state reset
import pandas as pd
import random
import numpy as np

# Function to generate the loan dataset
def generate_loan_dataset(num_records):
    random.seed(42)
    np.random.seed(42)
    
    data = {
        "loan_id": [f"LN{str(i).zfill(6)}" for i in range(1, num_records + 1)],
        "customer_age": np.random.randint(18, 70, num_records),
        "loan_amount": np.random.randint(1000, 50000, num_records),
        "interest_rate": np.random.uniform(2.5, 25.0, num_records).round(2),
        "loan_duration_months": np.random.choice([12, 24, 36, 48, 60], num_records),
        "loan_status": np.random.choice(["approved", "rejected", "pending"], num_records, p=[0.7, 0.2, 0.1]),
        "customer_income": np.random.randint(15000, 120000, num_records),
        "loan_purpose": np.random.choice(["education", "car", "home", "business"], num_records),
        "credit_score": np.random.randint(300, 850, num_records),
        "state": np.random.choice(["CA", "NY", "TX", "FL", "IL"], num_records)
    }
    
    df = pd.DataFrame(data)
    return df

# Generate the dataset
loan_dataset = generate_loan_dataset(1000)

# Save the dataset to a CSV file
file_path = "D:/datasets/loan_dataset.csv"
loan_dataset.to_csv(file_path, index=False)

file_path
