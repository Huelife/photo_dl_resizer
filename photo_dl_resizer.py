"""
Created: April 17, 2022, 03:00:00 PM (Sunday)
Author: Eric Meas
Contact:
Copyright: Copyright (C) 2022 Eric Meas All rights reserved
License: GNU GPLv3
Version: 1.0
https://www.gnu.org/licenses/gpl-3.0
"""

import os

from PIL import Image

input_path = "C:/Users/Eric/Desktop/Images"

for f in os.listdir(input_path):
  if f.endswith(".jpg"):
    im = Image.open(Input + "/{}".format(f))
    resize = im.resize((1100,800),Image.Resampling.LANCZOS)
    file_ext = os.path.splitext(f)
    resize.save("Copy/{}.jpg".format(file_ext))
