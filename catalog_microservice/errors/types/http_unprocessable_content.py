from http import HTTPStatus

class HttpUnprocessableContentError(Exception):
    def __init__(self, message: str = 'Unprocessable Content'):
        super().__init__(message)
        self.message = message
        self.name = HTTPStatus.UNPROCESSABLE_ENTITY.phrase
        self.status_code = HTTPStatus.UNPROCESSABLE_ENTITY
        