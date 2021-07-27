#!/usr/bin/env python3

import os
import socket
import ssl
import sys
import urllib.request
import urllib.error


backendhost = os.environ.get('DOA_SERVICE_NAME','localhost')

print("Will try connecting to %s:443" % backendhost)

try:
    r = urllib.request.urlopen('https://%s:443/files' % backendhost, context=ssl._create_unverified_context())
    sys.exit(0)
except urllib.error.HTTPError as e:
    if e.code == 404:
        # 404 is okay here
        sys.exit(0)
    print("Unexpected error talking to doa: \n\n%s" % e)

sys.exit(1)



