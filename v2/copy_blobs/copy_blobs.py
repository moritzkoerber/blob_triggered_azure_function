import logging

import azure.functions as func

logging.basicConfig()

bp = func.Blueprint()


@bp.function_name("copy_blobs")
@bp.blob_trigger(
    arg_name="obj",
    path="mycontainer/{name}.zip",  # only copy zip files
    connection="AZURE_STORAGE_SOURCE_CONN_STR",
)
@bp.blob_input(
    arg_name="inputblob",
    path="mycontainer/{name}.zip",
    connection="AZURE_STORAGE_SOURCE_CONN_STR",
)
@bp.blob_output(
    arg_name="outputblob",
    path="myothercontainer/{name}.zip",
    connection="AZURE_STORAGE_DEST_CONN_STR",
)
def blob_trigger_function(
    obj: func.InputStream, inputblob: bytes, outputblob: func.Out[bytes]
):
    logging.info("Python Queue trigger function processed %s", obj.name)
    outputblob.set(inputblob)
