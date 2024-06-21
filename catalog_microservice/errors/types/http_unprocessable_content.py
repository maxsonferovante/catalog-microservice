

class HttpUnprocessableContentError(HttpError):
    def __init__(self, message: str = 'Unprocessable Content'):
        super().__init__(message)
        self.message = message
        self.name = 'HttpUnprocessableContentError'
        self.status_code = 422
        