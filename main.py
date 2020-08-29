#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@ScriptName  : main.py
@Project     : Object-Detection-Cascade
@Author      : Meng Peng
@Date        : 12-08-2020
@Description : input image or video, test detection.py
"""
import os
import cv2
from detection import Detection


def get_base_path():
    base = os.path.abspath(".")
    return base


def get_file_path(filename):
    full_path = get_base_path() + filename
    return full_path


if __name__ == '__main__':
    detector = Detection()

    cv2.namedWindow('display', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('display', 960, 720)

    # test image
    image_path = get_file_path("/data/car.jpg")
    image = cv2.imread(image_path)
    img_detect = detector.object_detection(image)
    cv2.imwrite(get_base_path()+"/data/car_detect.jpg", img_detect)
    # Display the output
    cv2.imshow("display", img_detect)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

    '''
    # test video
    video_path = get_file_path("/data/video2.mp4")
    cap = cv2.VideoCapture(video_path)
    # change the path to your directory or to '0' for webCam
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv2.VideoWriter(get_base_path() + "/data/video2_detect.mp4",
                          fourcc, fps, size)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame_detect = detector.object_detection(frame)
            out.write(frame_detect)
            # Display the output
            cv2.imshow("display", frame_detect)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            out.release()
            cap.release()
    cv2.destroyAllWindows()
    '''
