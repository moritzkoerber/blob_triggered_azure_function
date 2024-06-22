import io
import logging
import os

import azure.functions as func
import polars as pl

logging.basicConfig()

bp = func.Blueprint()


@bp.blob_trigger(
    arg_name="blob",
    path="mycontainer/{name}.parquet",
    connection="StorageConnectionString",
)
def delta_table_func(blob: func.InputStream):
    # type(blob.read()) is bytes
    df = pl.read_parquet(io.BytesIO(blob.read()))
    df.write_delta(
        "abfss://test/delta_table",
        mode="overwrite",
        storage_options={
            "account_name": os.environ.get("AZ_STA_NAME"),
            "account_key": os.environ.get("AZ_STA_KEY"),
        },
    )
    print(df)
