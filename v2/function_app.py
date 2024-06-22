import azure.functions as func
from copy_blobs.copy_blobs import bp as copy_blobs_func
from http_trigger.http_trigger import bp as http_trigger_func

app = func.FunctionApp()

app.register_functions(copy_blobs_func)
app.register_functions(http_trigger_func)
