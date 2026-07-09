"""
PoultryGuard AI

Simulation Camera

Reads frames from a video file and behaves like a camera.
"""

import cv2

from app.services.cameras.interface import CameraInterface


class SimulationCamera(CameraInterface):

    def __init__(self, video_path: str):
        self.video_path = video_path
        self.cap = None

    def connect(self) -> bool:
        self.cap = cv2.VideoCapture(self.video_path)
        return self.cap.isOpened()

    def read(self):
        return self.cap.read()

    def release(self):
        if self.cap:
            self.cap.release()

    def is_connected(self):
        return self.cap is not None and self.cap.isOpened()