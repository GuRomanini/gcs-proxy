from datetime import datetime, UTC
from falcon import Request, Response
import json

from utils.context import Context
from utils.logger import Logger

from errors import InvalidSchema
from constants import BYPASS_ENDPOINTS


class InputOutputMiddleware:
    def process_request(self, req: Request, resp: Response):
        if req.method == "OPTIONS" or req.path in BYPASS_ENDPOINTS:
            return

        logger = Logger(context=req.context.instance, class_name=__name__)
        req.context.instance.timing = {}
        req.context.instance.timing["request_start_time"] = datetime.now(UTC)

        self.deserialize_request(req)
        logger.info(
            f"INCOMING REQUEST {req.method} {req.path} {req.remote_addr}",
            req.context.instance.media,
        )

    def process_response(self, req, resp, resource, req_succeeded):
        if req.method == "OPTIONS" or req.path in BYPASS_ENDPOINTS:
            return

        logger = Logger(context=req.context.instance, class_name=__name__)

        req.context.instance.timing["request_finish_time"] = datetime.now(UTC)
        start_time = req.context.instance.timing["request_start_time"]
        finish_time = req.context.instance.timing["request_finish_time"]
        total_request_time = (finish_time - start_time).total_seconds() * 1000.0

        resp_media = None
        if resp.media is not None:
            resp_media = resp.media

        logger.info(
            f"OUTGOING RESPONSE {resp.status} {req.method} {req.path} {req.remote_addr} {total_request_time} ms",
            resp_media,
        )

    def deserialize_request(self, req: Request):
        binary_data = req.bounded_stream.read()

        ctx = req.context.instance
        ctx: Context
        ctx.binary_body = binary_data

        req_media = None
        if req.content_length is not None and req.content_length > 0:
            try:
                req_media = json.loads(binary_data.decode("utf-8"))
            except json.JSONDecodeError:
                raise InvalidSchema("Malformated JSON File")

        ctx.media = req_media
