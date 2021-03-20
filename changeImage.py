#!/usr/bin/env python3
from PIL import Image
import os, sys, glob

source_folder = "supplier-data/images"
target_folder = source_folder + "/"
_format = ".jpeg"
_resolution = 600, 400

for image in os.listdir(source_folder):
  if "tiff" in image:
      f, e = os.path.splitext(image)
      im = Image.open(target_folder + image)
      im = im.convert('RGB')
      im = im.resize(_resolution)
      im.save(target_folder + f + _format)