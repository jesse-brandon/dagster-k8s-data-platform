from dagster import define_asset_job

from .assets import raw_data, transformed_data

data_pipeline_job = define_asset_job(
    name="data_pipeline_job", selection=[raw_data, transformed_data]
)
