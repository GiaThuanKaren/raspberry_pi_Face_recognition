from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from flask import Flask
from flask import render_template , request
# from flask_cors import CORS, cross_origin
import tensorflow as tf
import argparse
import facenet
import os
import sys
import math
import pickle
import align.detect_face
import numpy as np
import cv2
import collections
from sklearn.svm import SVC

import base64
import cv2


from threading import Thread
import cv2

class VideoStreamWidget(object):
    def __init__(self, src=0):
        # Create a VideoCapture object
        self.capture = cv2.VideoCapture(src)

        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()

    def show_frame(self):
        # Display frames in main program
        if self.status:
            self.frame = self.maintain_aspect_ratio_resize(self.frame, width=600)
            cv2.imshow('IP Camera Video Streaming', self.frame)

        # Press Q on keyboard to stop recording
        key = cv2.waitKey(1)
        if key == ord('q'):
            self.capture.release()
            cv2.destroyAllWindows()
            exit(1)

    # Resizes a image and maintains aspect ratio
    def maintain_aspect_ratio_resize(self, image, width=None, height=None, inter=cv2.INTER_AREA):
        # Grab the image size and initialize dimensions
        dim = None
        (h, w) = image.shape[:2]

        # Return original image if no need to resize
        if width is None and height is None:
            return image

        # We are resizing height if width is none
        if width is None:
            # Calculate the ratio of the height and construct the dimensions
            r = height / float(h)
            dim = (int(w * r), height)
        # We are resizing width if height is none
        else:
            # Calculate the ratio of the 0idth and construct the dimensions
            r = width / float(w)
            dim = (width, int(h * r))

        # Return the resized image
        return cv2.resize(image, dim, interpolation=inter)

if __name__ == '__main__':
    stream_link = 'http://192.168.1.7:8080'
    video_stream_widget = VideoStreamWidget(stream_link)
    while True:
        try:
            video_stream_widget.show_frame()
        except AttributeError:
            pass  

# cap =  cv2.VideoCapture('http://192.168.1.7:8080')
# while True:

#     #print('About to start the Read command')
#     ret, frame = cap.read()
#     #print('About to show frame of Video.')
#     if frame is not None:  # add this line
#         (height, width) = frame.shape[:2] 
#         # print(frame)
#         print(height)
#         minimap = frame[1648:1920, 800:1080]
    
#     # cv2.imshow("Capturing",frame)
#     #print('Running..')

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()