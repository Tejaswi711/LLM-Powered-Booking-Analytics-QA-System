import pandas as pd

# Load your data
df = pd.read_csv("Booking dataset.csv")
# In database.py
def get_documents():
    pass

# 1. Create the missing column
df['total_nights'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']

# 2. Now calculate revenue
df['revenue'] = df['adr'] * df['total_nights']

# Verify
print(df[['adr', 'stays_in_weekend_nights', 'stays_in_week_nights', 'total_nights', 'revenue']].head())