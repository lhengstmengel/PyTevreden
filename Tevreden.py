#!/usr/bin/python3

class Tevreden:

    def __init__(self, platform = None, api_key = None):
        
    if not platform:
        raise MissingPlatformError
        
    if not api_key:
        raise MissingApiKeyError


class MissingPlatformError(Exception):
    
    pass
    
    
class MissingApiKeyError(Exception):
    
    pass



    
