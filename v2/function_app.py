import azure.functions as func
from copy_blobs.copy_blobs import bp as copy_blobs_func
from delta_table.delta_table import bp as delta_table_func
from delta_table_mi.delta_table_mi import bp as delta_table_func_mi
from do_something_blob.do_something_blob import bp as do_something_blob_func
from do_something_blob_mi.do_something_blob_mi import bp as do_something_blob_mi_func
from http_trigger.http_trigger import bp as http_trigger_func

app = func.FunctionApp()

app.register_functions(copy_blobs_func)
app.register_functions(http_trigger_func)
app.register_functions(do_something_blob_func)
app.register_functions(delta_table_func)
app.register_functions(do_something_blob_mi_func)
app.register_functions(delta_table_func_mi)
