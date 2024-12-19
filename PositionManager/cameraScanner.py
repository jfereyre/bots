#!/bin/env python3

from threading import Thread
import numpy as np
import cv2 as cv
from PositionManager.box import Box

class DetectionCallback(object):

    def call(self):
        pass        

class CameraScanner(Thread):
    def __init__(self, a_camera_id: int = 1):
        super(CameraScanner, self).__init__()

        self.m_arucoDict = cv.aruco.Dictionary_get(cv.aruco.DICT_4X4_50)
        self.m_arucoParams = cv.aruco.DetectorParameters_create()
        self.m_camera_id = a_camera_id
        self.m_height = 0
        self.m_width = 0
        self._m_callbacks = {}

    @property
    def dimension(self):
        return (self.m_width, self.m_height)

    def aruco_detector(self, frame):
        """
        """
        (corners, ids, rejected) = cv.aruco.detectMarkers(frame, self.m_arucoDict, parameters=self.m_arucoParams)

        # verify *at least* one ArUco marker was detected
        if len(corners) > 0:
            # flatten the ArUco IDs list
            ids = ids.flatten()
            # loop over the detected ArUCo corners
            for (markerCorner, markerID) in zip(corners, ids):
                # extract the marker corners (which are always returned in
                # top-left, top-right, bottom-right, and bottom-left order)
                corners = markerCorner.reshape((4, 2))
                (topLeft, topRight, bottomRight, bottomLeft) = corners
                # convert each of the (x, y)-coordinate pairs to integers
                l_box = Box(topRight, bottomRight, bottomLeft, topLeft)

                # draw the bounding box of the ArUCo detection
                cv.line(frame, l_box.topLeft, l_box.topRight, (0, 255, 0), 2)
                cv.line(frame, l_box.topRight, l_box.bottomRight, (0, 255, 0), 2)
                cv.line(frame, l_box.bottomRight, l_box.bottomLeft, (0, 255, 0), 2)
                cv.line(frame, l_box.bottomLeft, l_box.topLeft, (0, 255, 0), 2)

                cv.circle(frame, l_box.center(), 4, (0, 0, 255), -1)
                # draw the ArUco marker ID on the image
                cv.putText(frame, str(markerID),
                    (l_box.topLeft[0], l_box.topLeft[1] - 15), cv.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)
            
                if markerID in self._m_callbacks.keys():
                    self._m_callbacks[markerID].call(markerID, l_box)
                else:
                    print("[INFO] ArUco marker ID: {}".format(markerID))

    def registerCallbackForTag(self, a_markerID: int, a_callbak: DetectionCallback):
        """
        """
        self._m_callbacks[a_markerID] = a_callbak


    def run(self):
        cap = cv.VideoCapture(self.m_camera_id)
        if not cap.isOpened():
            print("Cannot open camera")
            exit()

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
        
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break


            self.aruco_detector(frame)

            # Display the resulting frame
            cv.imshow('frame', frame)
            if cv.waitKey(1) == ord('q'):
                break
        
        # When everything done, release the capture
        cap.release()
        cv.destroyAllWindows()