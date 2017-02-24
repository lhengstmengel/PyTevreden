
class MissingPlatformError(Exception):
    pass
    
    
class MissingApiKeyError(Exception):
    pass


class HttpError(Exception):
    
    def __init__(self, message):
        self.message = message


class HttpBadRequestError(HttpError):
    pass
    
class HttpUnauthorizedError(HttpError):
    pass

class HttpForbiddenError(HttpError):
    pass

class HttpNotFoundError(HttpError):
    pass

class HttpMethodNotAllowedError(HttpError):
    pass

class HttpTooManyRequestsError(HttpError):
    pass
    
class HttpInternalServerError(HttpError):
    pass
    
class HttpNotImplementedError(HttpError):
    pass
    
