import cv2
from pathlib import Path
from datetime import datetime


class Recorder:

    def __init__(self):
        self.writer = None
        self.is_recording = False

    def start(self, filename, fps, width, height):

        Path("recordings").mkdir(exist_ok=True)

        output_path = Path("recordings") / filename

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        self.writer = cv2.VideoWriter(
        str(output_path),
        fourcc,
        fps,
        (width, height)
    )

        self.is_recording = True

    def write(self, frame):

        if self.is_recording:
           self.writer.write(frame)

    def stop(self):

        if self.writer:
           self.writer.release()

        self.is_recording = False