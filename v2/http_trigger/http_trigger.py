import logging

import azure.functions as func

logging.basicConfig()

bp = func.Blueprint()


@bp.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> str:
    return f"Hello, {req.params.get('name')}!"
