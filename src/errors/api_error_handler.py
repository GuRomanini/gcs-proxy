import falcon
from falcon import HTTPError
import traceback
import json

from errors import UaaSException, MethodNotAllowed, InternalError
from utils.logger import Logger


class APIErrorHandler:
    @staticmethod
    def uaas_exception(req, resp, ex, params):
        raise FalconUaaSException(ex)

    @staticmethod
    def method_not_allowed(*args):
        raise FalconUaaSException(MethodNotAllowed())

    @staticmethod
    def unexpected(req, *args):
        stack_trace_limit = 10
        logger = Logger(req.context.instance, __name__)
        _traceback = traceback.format_exc(stack_trace_limit)
        logger.fatal(_traceback)
        raise FalconUaaSException(InternalError())


class FalconUaaSException(HTTPError):
    def __init__(self, uaas_exception: UaaSException):
        HTTPError.__init__(self, getattr(falcon, f"HTTP_{str(uaas_exception.http_status)}"))
        self.title = uaas_exception.title
        self.description = uaas_exception.description
        self.translation = uaas_exception.translation
        self.code = uaas_exception.code
        self.extra_fields = uaas_exception.extra_fields

    def to_dict(self):
        obj = dict()
        obj["title"] = self.title
        obj["description"] = self.description
        obj["translation"] = self.translation
        obj["code"] = self.code
        obj["extra_fields"] = self.extra_fields if self.extra_fields is not None else {}

        if self.link is not None:
            obj["link"] = self.link

        return obj

    def to_json(self, *args):
        obj = self.to_dict()
        json_str = json.dumps(obj, ensure_ascii=False)
        return str.encode(json_str)
