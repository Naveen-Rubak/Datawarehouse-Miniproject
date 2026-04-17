import pandas as pd

# Load data
customers = pd.read_csv('../data/customers.csv')
orders = pd.read_csv('../data/orders.csv')

# Clean data
customers.dropna(inplace=True)
orders.dropna(inplace=True)

# Transform
merged = pd.merge(orders, customers, on='customer_id')

# Save cleaned data
merged.to_csv('../data/cleaned_data.csv', index=False)

print("ETL Process Completed Successfully")