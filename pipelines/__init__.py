from dagster import Definitions

from .assets import bronze_sales, raw_sales_data, sales_summary, silver_sales

defs = Definitions(
    assets=[
        raw_sales_data,
        bronze_sales,
        silver_sales,
        sales_summary,
    ]
)
