import azure.functions as func
from copy_blobs.copy_blobs import bp

app = func.FunctionApp()

app.register_functions(bp)
