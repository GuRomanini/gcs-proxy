from errors import UaaSException


class NotFoundSampleEntity(UaaSException):
    code = "BAP000001"

    def __init__(self, sample_entity_key) -> None:
        title = "Entity not Found"
        http_status = 404
        description = f"Entity with key {sample_entity_key} was not found."
        translation = f"A entidade com chave {sample_entity_key} não foi encontrada."
        super().__init__(title, self.code, http_status, description, translation)


class SampleEntityFinalStatus(UaaSException):
    code = "BAP000002"

    def __init__(self, old_status, new_status) -> None:
        title = "Entity cannot change status"
        http_status = 409
        description = f"Entity with status {old_status} cannot update to {new_status}."
        translation = "Essa entidade não pode ser atualizada."
        super().__init__(title, self.code, http_status, description, translation)


class PubSubPublishMessageError(UaaSException):
    code = "BAP000003"

    def __init__(self) -> None:
        title = "Error publishing message on pub sub."
        http_status = 500
        description = "Error publishing message on Pub Sub, max reetries exceeded."
        translation = "Erro ao publicar mensagem no Pub Sub, número máximo de tentativas excedido."
        super().__init__(title, self.code, http_status, description, translation)
