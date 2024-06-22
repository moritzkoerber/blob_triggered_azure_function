import logging

import azure.functions as func

logging.basicConfig()

bp = func.Blueprint()


@bp.function_name("copy_blobs")
@bp.blob_trigger(
    arg_name="obj",
    path="mycontainer/{name}.zip",  # only copy zip files
    connection="StorageConnectionString",
)
@bp.blob_input(
    arg_name="inputblob",
    path="mycontainer/{name}.zip",
    connection="StorageConnectionString",
)
@bp.blob_output(
    arg_name="outputblob",
    path="myothercontainer/{name}.zip",
    connection="StorageConnectionString",
)
def copy_blobs(obj: func.InputStream, inputblob: bytes, outputblob: func.Out[bytes]):
    logging.info("Processed %s", obj.name)
    outputblob.set(inputblob)
