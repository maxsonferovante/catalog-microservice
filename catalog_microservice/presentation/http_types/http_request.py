class HttpRequest:
    def __init__(self, 
                 body: dict, 
                 headers: dict,
                 query_params: dict = None,
                 path_params: dict = None,
                 url: str = None,
                 method: str = None,) -> None:
        
        self.body = body
        self.headers = headers
        self.query_params = query_params
        self.path_params = path_params
        self.url = url
        self.method = method
        
        
    