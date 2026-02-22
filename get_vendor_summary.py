import sqlite3
import pandas as pd
import logging
import os

# Ensure logs folder exists
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

def load_vendor_data(conn):
    """Load vendor_sales_summary table from SQLite"""
    logging.info("Reading vendor_sales_summary table...")
    df = pd.read_sql_query("SELECT * FROM vendor_sales_summary", conn)
    return df


def clean_data(df):
    """Clean data and create analytical KPIs"""

    logging.info("Cleaning data...")

    # Convert numeric columns safely
    numeric_cols = [
        'Volume',
        'TotalPurchaseQuantity',
        'TotalPurchaseDollars',
        'TotalSalesQuantity',
        'TotalSalesDollars'
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Fill missing values
    df.fillna(0, inplace=True)

    # Strip text columns safely
    if 'VendorName' in df.columns:
        df['VendorName'] = df['VendorName'].astype(str).str.strip()

    if 'Description' in df.columns:
        df['Description'] = df['Description'].astype(str).str.strip()

    # Create KPIs safely
    if 'TotalSalesDollars' in df.columns and 'TotalPurchaseDollars' in df.columns:
        df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
        df['ProfitMargin'] = df.apply(
            lambda x: (x['GrossProfit'] / x['TotalSalesDollars'] * 100)
            if x['TotalSalesDollars'] != 0 else 0,
            axis=1
        )

    if 'TotalSalesQuantity' in df.columns and 'TotalPurchaseQuantity' in df.columns:
        df['StockTurnover'] = df.apply(
            lambda x: (x['TotalSalesQuantity'] / x['TotalPurchaseQuantity'])
            if x['TotalPurchaseQuantity'] != 0 else 0,
            axis=1
        )

    if 'TotalSalesDollars' in df.columns and 'TotalPurchaseDollars' in df.columns:
        df['SalesToPurchaseRatio'] = df.apply(
            lambda x: (x['TotalSalesDollars'] / x['TotalPurchaseDollars'])
            if x['TotalPurchaseDollars'] != 0 else 0,
            axis=1
        )

    logging.info("Data cleaning and KPI creation completed.")

    return df


if __name__ == "__main__":

    conn = sqlite3.connect("inventory.db")

    logging.info("Starting Vendor Summary Processing...")

    df = load_vendor_data(conn)
    logging.info("Data loaded successfully.")

    clean_df = clean_data(df)
    logging.info("Data processed successfully.")

    # Save updated table back to DB
    clean_df.to_sql("vendor_sales_summary", conn, if_exists="replace", index=False)

    logging.info("Updated vendor_sales_summary table saved.")
    logging.info("Process Completed Successfully.")

    print("Vendor summary processed successfully!")

    conn.close()