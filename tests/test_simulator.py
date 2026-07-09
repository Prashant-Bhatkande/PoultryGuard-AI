import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import cv2
from app.services.cameras.simulator import SimulationCamera


# Change this to the path of your test video
VIDEO_PATH = "data/test.mp4"

camera = SimulationCamera(VIDEO_PATH)

if not camera.connect():
    print("Failed to open video.")
    exit()

while True:
    success, frame = camera.read()

    if not success:
        print("Video finished.")
        break

    cv2.imshow("Simulation Camera", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()