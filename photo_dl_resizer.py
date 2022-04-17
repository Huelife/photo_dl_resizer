"""
Created: April 17, 2022, 03:00:00 PM (Sunday)
Author: Eric Meas
Contact:
Copyright: Copyright (C) 2022 Eric Meas All rights reserved
License: GNU GPLv3
Version: 1.0
https://www.gnu.org/licenses/gpl-3.0
"""

from PIL import Image
im = Image.open("*.jpg")
resize = im.resize((1100,800),Image.Resampling.LANCZOS)
resize.save("*.jpg")
