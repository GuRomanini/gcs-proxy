import os


ENV_ID = os.environ.get("ENV_ID")
SERVICE_ROOT = os.path.abspath(os.path.dirname(__file__))
SCHEMA_PATH = SERVICE_ROOT + "/schemas/"
BYPASS_ENDPOINTS = ["/", "/health_check"]

SERVICE_NAME = os.environ.get("SERVICE_NAME")
SERVICE_DOMAIN = os.environ.get("SERVICE_DOMAIN")
COMMIT = os.environ.get("COMMIT")
APP_ENV = os.environ.get("APP_ENV")
PROJECT_ENV = os.environ.get("PROJECT_ENV")

# SERVICE_HANDLER
SERVICE_HANDLER_API_SERVICE_ADDRESS = os.environ.get("SERVICE_HANDLER_API_SERVICE_ADDRESS")
SERVICE_HANDLER_API_SERVICE_TIMEOUT = int(os.environ.get("SERVICE_HANDLER_API_SERVICE_TIMEOUT", "-1"))


def check_variables():
    variable_names = [k for k in dir() if (not k.startswith("__") and not callable(globals()[k]))]
    variables_without_value = []
    for variable in variable_names:
        variable_value = globals()[variable]
        if (
            (isinstance(variable_value, int) and variable_value == -1)
            or (isinstance(variable_value, float) and variable_value == -1)
            or (isinstance(variable_value, str) and not variable_value)
        ):
            variables_without_value.append(variable)
    if variables_without_value:
        raise EnvironmentError(
            "A Error occurred while checking variables, please verify these variables without values {}".format(
                variables_without_value
            )
        )
