import pandas as pd
from dagster import asset


@asset
def raw_data():
    data = {"id": [1, 2, 3], "value": [10, 20, 30]}
    return pd.DataFrame(data)


@asset
def transformed_data(raw_data):
    raw_data["value_x2"] = raw_data["value"] * 2
    return raw_data
