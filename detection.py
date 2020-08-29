#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@ScriptName  : detection.py
@Project     : Object-Detection-Cascade
@Author      : Meng Peng
@Date        : 10-08-2020
@Description : object (vehicle) detection with cv2.CascadeClassifier
"""
import os
import cv2


class Detection:
    __obj_cascade = None

    def __init__(self):
        self.load_cascade()

    def load_cascade(self):
        cascade_path = os.path.abspath(".") + '/detector/data/xml/cascade.xml'

        # load CascadeClassifier for vehicle detection
        self.__obj_cascade = cv2.CascadeClassifier(cascade_path)

    def object_detection(self, img):
        # convert to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # detect vehicles, return(x, y, w, h)
        vehicles = self.__obj_cascade.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5)

        for (x, y, w, h) in vehicles:
            cv2.rectangle(img, (x, y), (x + w, y + h), (200, 100, 0), 2)
            cv2.rectangle(img, (x, y - 16), (x + 40, y - 2), (200, 100, 0), -1)
            cv2.putText(img, 'car', (x, y - 1), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0, 0, 0), 2)

        return img
