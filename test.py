#!/usr/bin/python3

import tevreden.API
import pprint

t = tevreden.API.API( platform = 'autobesdfsddrijf', api_key = 'J2K3H9Z1T4WWQ33W7770JJBMAVXSAWHRXX1OEHNM1BNTS2F4OTWSCV2BQL4XQ2SI', domain='api.tevreden.nl' )

import pprint

pprint.pprint(t.call( method = 'GET', path='/platforms' ))
