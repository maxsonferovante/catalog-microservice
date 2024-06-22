from http import HTTPStatus

class HttpBadRequestError(Exception):
    
    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message
        self.name =  HTTPStatus.BAD_REQUEST.phrase
        self.status_code = HTTPStatus.BAD_REQUEST