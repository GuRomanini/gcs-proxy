from errors import UaaSException


class InvalidSchema(UaaSException):
    code = "QIT000001"

    def __init__(self, __description) -> None:
        title = "Bad Request"
        http_status = 400
        description = __description
        translation = "Schema Inválido"
        super().__init__(title, self.code, http_status, description, translation)


class RedisConnectionError(UaaSException):
    code = "QIT000005"

    def __init__(self) -> None:
        title = "Failed to connect to redis"
        http_status = 500
        description = "Redis connection failed"
        translation = "Conexão com redis falhou"
        super().__init__(title, self.code, http_status, description, translation)
