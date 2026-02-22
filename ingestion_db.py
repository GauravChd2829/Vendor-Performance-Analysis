# Use this script to save csv files into database with their filename as tablename
import pandas as pd
import sqlite3
import logging
import os
import time

# Ensure logs folder exists
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

def load_final_dataset():
    """Load processed vendor_sales_summary.csv into SQLite database"""

    start = time.time()
    
    try:
        # Connect to SQLite database
        conn = sqlite3.connect("inventory.db")

        logging.info("Reading vendor_sales_summary.csv")

        # Read final processed dataset
        df = pd.read_csv("data/vendor_sales_summary.csv")

        logging.info("Ingesting vendor_sales_summary into database")

        # Write to SQLite
        df.to_sql("vendor_sales_summary", conn, if_exists="replace", index=False)

        conn.close()

        end = time.time()
        total_time = round((end - start) / 60, 4)

        logging.info("-------------- Ingestion Complete ------------")
        logging.info(f"Total Time Taken: {total_time} minutes")

        print("vendor_sales_summary table created successfully!")

    except Exception as e:
        logging.error(f"Error during ingestion: {e}")
        print("Error occurred during ingestion. Check logs.")

if __name__ == "__main__":
    load_final_dataset()