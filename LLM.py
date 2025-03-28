import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_plot(fig, filename, folder="analytics_output"):

    try:
        output_path = Path(folder)
        output_path.mkdir(parents=True, exist_ok=True)
        filepath = output_path / filename
        fig.savefig(filepath, bbox_inches='tight', dpi=300)
        plt.close(fig)
        logger.info(f"Saved visualization: {filepath}")
    except Exception as e:
        logger.error(f"Failed to save plot: {str(e)}")
        raise

def generate_analytics(data):

    try:
        # Convert 'is_canceled' to a categorical variable with descriptive labels
        data['cancel_status'] = data['is_canceled'].map({0: 'Not Canceled', 1: 'Canceled'})

        # 1. Cancellation Analysis
        fig1, ax1 = plt.subplots(figsize=(12, 6))
        sns.boxplot(
            x='cancel_status',
            y='lead_time',
            hue='cancel_status',
            data=data,
            palette={'Not Canceled': 'lightblue', 'Canceled': 'salmon'},
            dodge=False,
            legend=False,
            ax=ax1
        )
        ax1.set_title('Cancellation Lead Time Analysis', fontsize=14)
        ax1.set_xlabel('Cancellation Status', fontsize=12)
        ax1.set_ylabel('Lead Time (Days)', fontsize=12)
        save_plot(fig1, "cancellation_analysis.png")

        # 2. Revenue Trends
        monthly_revenue = data.groupby(['arrival_date_year', 'arrival_date_month'])['revenue'].sum().unstack()
        fig2, ax2 = plt.subplots(figsize=(14, 6))
        monthly_revenue.plot(kind='bar', ax=ax2)
        ax2.set_title('Monthly Revenue Trends', fontsize=14)
        ax2.set_xlabel('Month', fontsize=12)
        ax2.set_ylabel('Revenue (€)', fontsize=12)
        plt.xticks(rotation=45)
        save_plot(fig2, "monthly_revenue.png")

        # 3. Market Segment Impact
        fig3, ax3 = plt.subplots(figsize=(12, 6))
        sns.countplot(
            x='market_segment',
            hue='cancel_status',
            data=data,
            palette={'Not Canceled': 'lightgreen', 'Canceled': 'lightcoral'},
            ax=ax3
        )
        ax3.set_title('Bookings by Market Segment', fontsize=14)
        ax3.set_xlabel('Market Segment', fontsize=12)
        ax3.set_ylabel('Count', fontsize=12)
        plt.xticks(rotation=45)
        save_plot(fig3, "market_segment_analysis.png")

    except Exception as e:
        logger.error(f"Analytics generation failed: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        # Load data
        data_path = Path("Booking dataset.csv")
        if not data_path.exists():
            raise FileNotFoundError(f"Data file not found at {data_path}")

        logger.info(f"Loading data from {data_path}")
        data = pd.read_csv(data_path)

        # Ensure 'revenue' column exists
        if 'revenue' not in data.columns:
            data['revenue'] = data['adr'] * (data['stays_in_weekend_nights'] + data['stays_in_week_nights'])

        # Generate analytics
        generate_analytics(data)
        logger.info("Analytics reports successfully generated in /analytics_output folder")

    except Exception as e:
        logger.error(f"Application error: {str(e)}")
        raise
