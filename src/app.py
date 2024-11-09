import falcon

from utils.logger import LogHandler
from errors import APIErrorHandler, UaaSException, error_verification

from middlewares.context_creator import ContextCreator
from middlewares.input_output import InputOutputMiddleware

from resources.health_check import HealthcheckResource
from resources.home import Home
from resources.time import TimeResource
from resources.sink import SinkResource
from resources.service_handler_resource import ServiceHandlerResource

from constants import check_variables


def create():
    api = falcon.App(
        middleware=[
            ContextCreator(),
            InputOutputMiddleware(),
        ]
    )

    home_resource = Home()
    api.add_route("/", home_resource)
    hc_resource = HealthcheckResource()
    api.add_route("/health_check", hc_resource)

    sink_resource = SinkResource()
    api.add_sink(sink_resource, r"/")

    time_resource = TimeResource()
    api.add_route("/time", time_resource)

    service_handler_resource = ServiceHandlerResource()
    api.add_sink(service_handler_resource, r"/")

    return api


def main():
    error_verification()
    check_variables()
    LogHandler()
    api = create()

    api.add_error_handler(Exception, APIErrorHandler.unexpected)
    api.add_error_handler(falcon.HTTPMethodNotAllowed, APIErrorHandler.method_not_allowed)
    api.add_error_handler(UaaSException, APIErrorHandler.uaas_exception)
    return api


application = main()
