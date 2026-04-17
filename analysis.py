import pandas as pd

df = pd.read_csv('../data/cleaned_data.csv')

# Revenue calculation
df['revenue'] = df['quantity'] * 100  # example price

# Top customers
top_customers = df.groupby('name')['revenue'].sum().sort_values(ascending=False)

print(top_customers)