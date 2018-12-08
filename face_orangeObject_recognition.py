# Hello World Example
#
# Welcome to the OpenMV IDE! Click on the green run arrow button below to run the script!

import sensor, image, time

sensor.reset()                      # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.HQVGA)   # Set frame size to QVGA (320x240)
sensor.skip_frames(time = 2000)     # Wait for settings take effect.
clock = time.clock()                # Create a clock object to track the FPS.

thresholds = [ (68, 80, 14, 127, 127, -6)]

#Facial Tracking
harr = image.HaarCascade("frontalface", 20)

#Color tracking/Blobs
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
i = 0

while(True):
    clock.tick()                    # Update the FPS clock.

    img = sensor.snapshot()         # Take a picture and return the image.

    faces = img.find_features(harr,threshold=0.7, scale_factor=1.3)

    for face in faces:
        img.draw_rectangle(face)

    for blob in img.find_blobs([thresholds[i]], pixels_threshold=250, area_threshold=250, merge=True):
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())

    print("FPS:", clock.fps())
