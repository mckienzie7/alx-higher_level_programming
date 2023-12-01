#!/usr/bin/python3
import urllib.parse
import urllib.request

url = 'http://www.someserver.com/cgi-bin/register.cgi'
#values = {'name' : 'Michael Foord',
#          'location' : 'Northampton',
#         'language' : 'Python' }

#data = urllib.parse.urlencode(values)
#data = data.encode('ascii') # data should be bytes
#req = urllib.request.Request(url, data)
#with urllib.request.urlopen(req) as response:
#the_page = response.read()
from urllib.request import Request, urlopen
from urllib.error import URLError
req = Request('http://flozzykamau.tech/')
try:
    response = urlopen(req)
    print(response.read())
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
