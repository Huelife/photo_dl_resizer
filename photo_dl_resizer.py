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

input_path = r"C:\Users\Eric\Desktop\Images"
output_path = r"C:\Users\Eric\Desktop\Images\Copy"
image_ext = (".jpg",".JPG",".jpeg",".JPEG",".gif",".GIF")

for f in os.listdir(input_path):
  im_in_path = os.path.join(input_path,f)
  im_out_path = os.path.join(output_path,f)
  
  if f.endswith(image_ext):
    im = Image.open(im_in_path)
    resize = im.resize((1100,800),Image.Resampling.LANCZOS)
    resize.save(im_out_path)
