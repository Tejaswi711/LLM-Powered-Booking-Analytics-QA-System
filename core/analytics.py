import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "hotel_bookings.csv"


def load_data():
    """Load and cache the dataset"""
    df = pd.read_csv(DATA_PATH)
    # Your preprocessing code here
    return df


def generate_analytics():
    df = load_data()

    # Your existing analytics code
    monthly_rev = df.groupby(['arrival_date_year', 'arrival_date_month'])['revenue'].sum().unstack()
    cancellation_rate = df['is_canceled'].mean() * 100

    return {
        "revenue_trends": monthly_rev.to_dict(),
        "cancellation_rate": cancellation_rate,
        "top_countries": df['country'].value_counts().head(10).to_dict()
    }