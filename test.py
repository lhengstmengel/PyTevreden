#!/usr/bin/python3

# from tevreden import API
import tevreden.APIClient
import pprint

t = tevreden.APIClient( platform = 'autobedrijf', api_key = 'J2K3H9Z1T4WWQ33W7770JJBMAVXSAWHRXX1OEHNM1BNTS2F4OTWSCV2BQL4XQ2SI', domain='api.tevreden.nl' )

# pprint.pprint(t.call( method = 'GET', path='/platforms' ))
platforms = t.get_platforms()
for platform in platforms:
    print(platform['name'])
    

