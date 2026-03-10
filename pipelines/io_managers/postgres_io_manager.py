import pandas as pd
from dagster import IOManager
from sqlalchemy import create_engine


class PostgresIOManager(IOManager):

    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)

    def handle_output(self, context, obj):
        table_name = context.asset_key.path[-1]

        if isinstance(obj, pd.DataFrame):
            obj.to_sql(table_name, self.engine, if_exists="replace", index=False)

    def load_input(self, context):
        table_name = context.asset_key.path[-1]

        return pd.read_sql_table(table_name, self.engine)
