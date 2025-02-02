import sys
import inspect
from unicodedata import normalize


def error_verification():
    clsmembers = inspect.getmembers(sys.modules["errors"], inspect.isclass)

    errors_dict = dict()
    for _class in clsmembers:
        class_name = _class[0]
        class_type = _class[1]
        is_custom_exception = False
        if issubclass(class_type, UaaSException) and class_name != "UaaSException":
            is_custom_exception = True

        if is_custom_exception:
            code = class_type.code
            if errors_dict.get(code) is not None:
                used_class_name = errors_dict[code]
                raise Exception(f"The code {code} is being used twice: In {class_name} and {used_class_name}")
            errors_dict[code] = class_name


class UaaSException(Exception):
    def __init__(self, title, code, http_status, description, translation, **kwargs) -> None:
        self.title = title
        self.description = description
        self.translation = normalize("NFKD", translation).encode("ASCII", "ignore").decode("ASCII")
        self.code = code
        self.http_status = http_status
        self.extra_fields = kwargs


class MethodNotAllowed(UaaSException):
    code = "QIT000405"

    def __init__(self) -> None:
        title = "Method not allowed"
        http_status = 405
        description = "The requested method is forbidden for this resource."
        translation = "O metodo desejado nao foi encontrado para esse recurso."
        super().__init__(title, self.code, http_status, description, translation)


class InternalError(UaaSException):
    code = "QIT000500"

    def __init__(self) -> None:
        title = "Internal Error"
        http_status = 500
        description = "An internal error has occurred and its being investigated."
        translation = "Um erro interno aconteceu e esta sendo investigado."
        super().__init__(title, self.code, http_status, description, translation)


class NotFoundResource(UaaSException):
    code = "QIT000404"

    def __init__(self) -> None:
        title = "Resource not Found"
        http_status = 404
        description = "The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible."
        translation = "O resource solicitado não podee ser encontrado, mas pode estar disponível no futuro. Requests subsequentes do cliente são permitidos."
        super().__init__(title, self.code, http_status, description, translation)
