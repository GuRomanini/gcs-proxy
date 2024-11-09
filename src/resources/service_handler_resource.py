import falcon
from falcon import Request, Response

from connectors import BaseConnectorResponse, RestConnector

from constants import SERVICE_HANDLER_API_SERVICE_ADDRESS, SERVICE_HANDLER_API_SERVICE_TIMEOUT


class ServiceHandlerResource:
    def __call__(self, req, resp, *args, **kwargs):
        if req.method == 'POST':
            self.on_post(req, resp, *args, **kwargs)
        elif req.method == 'PUT':
            self.on_put(req, resp, *args, **kwargs)
        elif req.method == 'GET':
            self.on_get(req, resp, *args, **kwargs)
        elif req.method == 'PATCH':
            self.on_patch(req, resp, *args, **kwargs)

    def on_post(self, req: Request, resp: Response):
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json"
        }
        body = req.context.instance.media

        if "ROLES" in req.headers:
            headers["ROLES"] = req.headers["ROLES"]

        connector = RestConnector(
            context=req.context.instance,
            class_name=__name__,
            base_url=SERVICE_HANDLER_API_SERVICE_ADDRESS,
            timeout=SERVICE_HANDLER_API_SERVICE_TIMEOUT
        )
        response: BaseConnectorResponse = connector.send(endpoint=req.relative_uri, method="POST", headers=headers, payload=body)
        resp.media = response.response_json
        resp.status = falcon.code_to_http_status(response.response_status)

    def on_put(self, req: Request, resp: Response):
        headers = req.headers
        body = req.context.instance.media
        
        connector = RestConnector(
            context=req.context.instance,
            class_name=__name__,
            base_url=SERVICE_HANDLER_API_SERVICE_ADDRESS,
            timeout=SERVICE_HANDLER_API_SERVICE_TIMEOUT
        )
        response: BaseConnectorResponse = connector.send(endpoint=req.relative_uri, method="PUT", headers=headers, payload=body)
        resp.media = response.response_json
        resp.status = falcon.code_to_http_status(response.response_status)

    def on_get(self, req: Request, resp: Response):
        headers = req.headers
        body = req.context.instance.media
        
        connector = RestConnector(
            context=req.context.instance,
            class_name=__name__,
            base_url=SERVICE_HANDLER_API_SERVICE_ADDRESS,
            timeout=SERVICE_HANDLER_API_SERVICE_TIMEOUT
        )
        response: BaseConnectorResponse = connector.send(endpoint=req.relative_uri, method="GET", headers=headers, payload=body)
        resp.media = response.response_json
        resp.status = falcon.code_to_http_status(response.response_status)

    def on_patch(self, req: Request, resp: Response):
        headers = req.headers
        body = req.context.instance.media
        
        connector = RestConnector(
            context=req.context.instance,
            class_name=__name__,
            base_url=SERVICE_HANDLER_API_SERVICE_ADDRESS,
            timeout=SERVICE_HANDLER_API_SERVICE_TIMEOUT
        )
        response: BaseConnectorResponse = connector.send(endpoint=req.relative_uri, method="PATCH", headers=headers, payload=body)
        resp.media = response.response_json
        resp.status = falcon.code_to_http_status(response.response_status)
