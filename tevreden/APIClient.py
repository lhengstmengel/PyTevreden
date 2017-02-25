import httplib2
import pprint
import json


class APIClient:

    def __init__( self, platform = None, api_key = None, domain = 'api.tevreden.nl' ):
            
        self.platform = platform
        self.api_key = api_key
        self.domain = domain
        

    def call( self, method = 'GET', path = '/', params = None, body = None ):
        
        # TODO params!
        
        h = httplib2.Http(".cache")
        (response, raw_content) = h.request(
            "https://%s%s" % (self.domain, path),
            method, 
            body=body, 
            headers={
                'tevreden-platform': self.platform, 
                'tevreden-api-key': self.api_key
            }
        )

        content = raw_content.decode("utf-8")
        if response['content-type'] == 'application/json':
            decoded_content = json.loads(content)
        else:
            decoded_content = content
        
        if response.status == 200 or response.status == 201:
            return decoded_content
        elif response.status == 400:
            raise BadRequestError(decoded_content['message'])
        elif response.status == 401:
            raise UnauthorizedError(decoded_content['message'])
        elif response.status == 403:
            raise ForbiddenError(decoded_content['message'])
        elif response.status == 404:
            raise NotFoundError(decoded_content['message'])
        elif response.status == 405:
            raise MethodNotAllowedError(decoded_content['message'])
        elif response.status == 420:
            raise TooManyRequestsError(decoded_content['message'])
        elif response.status == 500:
            raise InternalServerError(decoded_content['message'])
        elif response.status == 501:
            raise NotImplementedError(decoded_content['message'])


    def get_platforms( self ):
        r = self.call( path = '/platforms' )
        return r['platforms']


# Exceptions



class APIError(Exception):
    def __init__(self, message):
        self.message = message

class MissingPlatformError(APIError):
    pass
    
class MissingApiKeyError(APIError):
    pass

class BadRequestError(APIError):
    pass
    
class UnauthorizedError(APIError):
    pass

class ForbiddenError(APIError):
    pass

class NotFoundError(APIError):
    pass

class MethodNotAllowedError(APIError):
    pass

class TooManyRequestsError(APIError):
    pass
    
class InternalServerError(APIError):
    pass
    
class NotImplementedError(APIError):
    pass
    
