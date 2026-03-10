from dagster import Definitions

from .assets import raw_data, transformed_data
from .jobs import data_pipeline_job

defs = Definitions(assets=[raw_data, transformed_data], jobs=[data_pipeline_job])
