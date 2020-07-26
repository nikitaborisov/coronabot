import glob
import requests
import re
import datetime
import sys
from postimage import post_image

headers = {}
files = glob.glob('CU-covid.*.png')
if files:
    latest = sorted(files)[-1]
    m = re.match(r'CU-covid\..*\.([^.]*)\.png$', latest)
    if m:
        etag = m.group(1)
        #print("Etag is", etag)
        headers = { "If-None-Match": f'"{m.group(1)}"' }
    else:
        print("No etag:", latest)

r = requests.get('https://public.tableau.com/static/images/Ma/Master2COVIDTableau/Dashboard1/1.png', 
                 headers=headers)
if r.status_code == 304:
    pass
else:
    r.raise_for_status()
    if r.headers.get('Content-Type', None) == 'image/png':
        filename = 'CU-covid.' + datetime.datetime.now().isoformat(timespec='seconds')
        etag = r.headers.get('ETag', None)
        if etag:
            filename += "." + etag.replace('"', '')
        filename += '.png'

        print("Saving to", filename)
        with open(filename, 'wb') as savefile:
            savefile.write(r.content)
        post_image(filename)
    else:
        print("Not a PNG:", r.headers)





