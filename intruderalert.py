# Authored by Duy Dao. 4/23/2019.
# Follow@ twitter.com/DuyTheDao
# Do as you please.
# This was created for learning purposes.
#######################################################################
# ██╗███╗   ██╗████████╗██████╗ ██╗   ██╗██████╗ ███████╗██████╗      #
# ██║████╗  ██║╚══██╔══╝██╔══██╗██║   ██║██╔══██╗██╔════╝██╔══██╗     #
# ██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║  ██║█████╗  ██████╔╝     #
# ██║██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║  ██║██╔══╝  ██╔══██╗     #
# ██║██║ ╚████║   ██║   ██║  ██║╚██████╔╝██████╔╝███████╗██║  ██║     #
# ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝     #
#                                                                     #
# █████╗ ██╗     ███████╗██████╗ ████████╗                            #
# ██╔══██╗██║     ██╔════╝██╔══██╗╚══██╔══╝                           #
# ███████║██║     █████╗  ██████╔╝   ██║                              #
# ██╔══██║██║     ██╔══╝  ██╔══██╗   ██║                              #
# ██║  ██║███████╗███████╗██║  ██║   ██║                              #
# ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝                              #
#######################################################################
# Options for either Video output or Image output
# Soon to come: Segmentation + Adruino Tracking + Notifications
# Requirements Python3, OpenCV4

import os
import cv2
from time import sleep
import datetime as dt
import logging as log

# Classifier from OpenCV
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Log of Faces Detected including datetime
log.basicConfig(filename='webcam.log', level=log.INFO)
video_capture = cv2.VideoCapture(0)
anterior = 0

# Counter for the picture image capture on the bottom
screen_counter = 0

# frame height and width for the boxes
frameWidth = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# You can change it to other codecs but this is MJPG
# VideoWriter(outvid, fourcc, float(fps), size, is_color)
# fourcc or 'codec' selected is MJPG.
# Change FPS according to webcam capability
out = cv2.VideoWriter('intruder.avi',cv2.VideoWriter_fourcc('M','J','P','G'),30.0,(frameWidth,frameHeight))

while True:
    if not video_capture.isOpened():
        print('Cannot load webcam')
        sleep(5)
        pass

    # Video Capture - Frames
    ret, frame = video_capture.read()

    # Colorspace in OpenCV
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Actual face cascade classifier
    face = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

    # Displays text if a face is shown
    if len(face) > 0:
        out.write(frame)

        # Below is if you only want pictures and not videos.
        # Only thing is, it is per frame. So it's very fast.

        # picture_name = "intruder_frame_{}.png".format(screen_counter)
        # cv2.imwrite(picture_name, frame)
        # print("{} written!".format(picture_name))
        # screen_counter += 1

        # Text as you guessed it.
        cv2.putText(img = frame,
                            text = "face found",
                            org = (int(frameWidth/10 - 1),int(frameHeight/1)),
                            fontFace = cv2.FONT_HERSHEY_DUPLEX,
                            fontScale = 2.5,
                            color = (0,0,255),
                            thickness = 2,
                            lineType = cv2.LINE_AA)

    # Bounding Box to Face
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Logging system that prints # of faces and date/time.
    if anterior != len(face):
        anterior = len(face)
        log.info("face: "+str(len(face))+" at "+str(dt.datetime.now()))

    # Shows frame and name of window
    cv2.imshow('Faces Detected', frame)

    # Press Q to break the cycle"
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

    # Shows frame and name of window after wait
    cv2.imshow('Faces Detected', frame)

# Closes webcam window
video_capture.release()
cv2.DestroyAllWindows()