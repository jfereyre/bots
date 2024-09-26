#!/bin/env python3

from threading import Thread
import numpy as np
import cv2 as cv
from PositionManager.box import Box

class CameraScanner(Thread):
    def __init__(self, a_camera_id: int = 1, a_tag_detection_callback = None):
        super(CameraScanner, self).__init__()

        self.m_arucoDict = cv.aruco.Dictionary_get(cv.aruco.DICT_4X4_50)
        self.m_arucoParams = cv.aruco.DetectorParameters_create()
        self.m_tag_detection_callback = a_tag_detection_callback
        self.m_camera_id = a_camera_id
        self.m_height = 0
        self.m_width = 0

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
            
                if not self.m_tag_detection_callback:
                    print("[INFO] ArUco marker ID: {}".format(markerID))
                else:
                    self.m_tag_detection_callback(markerID, l_box)


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

            self.m_width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
            self.m_height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)

            self.aruco_detector(frame)

            # Display the resulting frame
            cv.imshow('frame', frame)
            if cv.waitKey(1) == ord('q'):
                break
        
        # When everything done, release the capture
        cap.release()
        cv.destroyAllWindows()