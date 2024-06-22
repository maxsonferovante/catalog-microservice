from http import HTTPStatus

class HttpNotFoundError(Exception):
    
    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message
        self.name = HTTPStatus.NOT_FOUND.phrase
        self.status_code = HTTPStatus.NOT_FOUND