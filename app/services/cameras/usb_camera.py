"""
PoultryGuard AI

USB Camera Implementation
"""

import cv2

from app.services.cameras.interface import CameraInterface
from app.services.cameras.exceptions import CameraConnectionError


class USBCamera(CameraInterface):
    """USB camera implementation."""

    def __init__(self, camera_id: int = 0):
        self.camera_id = camera_id
        self.cap = None

    def connect(self) -> bool:
        self.cap = cv2.VideoCapture(self.camera_id)

        if not self.cap.isOpened():
            raise CameraConnectionError(
                f"Cannot connect to camera {self.camera_id}"
            )

        return True

    def read(self):
        return self.cap.read()

    def release(self):
        if self.cap:
            self.cap.release()

    def is_connected(self):
        return self.cap is not None and self.cap.isOpened()