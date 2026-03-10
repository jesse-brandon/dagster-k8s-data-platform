from dagster import io_manager

from .io_managers.postgres_io_manager import PostgresIOManager


@io_manager
def postgres_io_manager(_):

    connection_string = "postgresql://dagster:dagster@postgres:5432/dagster"

    return PostgresIOManager(connection_string)
