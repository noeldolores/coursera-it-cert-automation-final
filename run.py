#! /usr/bin/env python3
import os
import requests
import re
description_path = "supplier-data/descriptions/"
url = "http://localhost/fruits/"

for files in os.listdir(description_path):
  upload_dict = {}
  with open(description_path + files) as f:
    _ = f.read().splitlines()
    upload_dict['name']=_[0]
    upload_dict['weight']=re.sub("[^\d\.]", "",_[1])
    upload_dict['description']=_[2]
    upload_dict['image_name'] = re.sub("txt","jpeg",files)
    r = requests.post(url, data=upload_dict)
    print(r.text)
