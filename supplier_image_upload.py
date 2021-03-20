#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
_file = "supplier-data/images"
for image in os.listdir(_file):
  if image.endswith(".jpeg"):
    with open(_file + "/" + image, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
