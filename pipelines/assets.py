import pandas as pd
from dagster import asset


@asset
def raw_sales_data():
    """Ingest raw CSV data"""
    df = pd.read_csv("data/sample_sales.csv")
    return df


@asset
def bronze_sales(raw_sales_data):
    """Minimal cleaning layer"""
    df = raw_sales_data.copy()
    df["order_date"] = pd.to_datetime(df["order_date"])
    return df


@asset
def silver_sales(bronze_sales):
    """Transform and standardize"""
    df = bronze_sales.copy()

    df["amount"] = df["amount"].astype(float)

    return df


@asset
def sales_summary(silver_sales):
    """Analytics layer"""
    summary = silver_sales.groupby("customer_id")["amount"].sum().reset_index()

    summary.columns = ["customer_id", "total_spent"]

    return summary
