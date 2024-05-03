#!/usr/bin/python3

# For use from the login console, when not running X Windows.

import time

from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.start_preview(Preview.DRM, x=0, y=0, width=1920, height=1080)

preview_config = picam2.create_preview_configuration({"size": (640, 360)})
picam2.configure(preview_config)

picam2.start()
time.sleep(5)
