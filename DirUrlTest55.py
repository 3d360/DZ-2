import requests
import re

def getFilename_fromCd(cd):
"""
Get filename from content-disposition
"""
if not cd:
return None
fname = re.findall('filename=(.+)', cd)
if len(fname) == 0:
return None
return fname[0]


url = 'http://see3d.ru/'
r = requests.get(url, allow_redirects=True)
filename = getFilename_fromCd(r.headers.get('content-disposition'))
open(filename, 'wb').write(r.content)