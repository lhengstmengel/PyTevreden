#!/usr/bin/python3


'''

import httplib2
import pprint
import json

class API:

    def __init__( self, platform = None, api_key = None, domain = 'api.tevreden.nl' ):
            
        self.platform = platform
        self.api_key = api_key
        self.domain = domain
        

    def call( self, method = 'GET', path = '/', body = None ):
        
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
            raise HttpBadRequestError(decoded_content['message'])
        elif response.status == 401:
            raise HttpUnauthorizedError(decoded_content['message'])
        elif response.status == 403:
            raise HttpForbiddenError(decoded_content['message'])
        elif response.status == 404:
            raise HttpNotFoundError(decoded_content['message'])
        elif response.status == 405:
            raise HttpMethodNotAllowedError(decoded_content['message'])
        elif response.status == 420:
            raise HttpTooManyRequestsError(decoded_content['message'])
        elif response.status == 500:
            raise HttpInternalServerError(decoded_content['message'])
        elif response.status == 501:
            raise HttpNotImplementedError(decoded_content['message'])
            
            


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
    
    

'''

    
