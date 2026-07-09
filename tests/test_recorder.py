import cv2

from app.services.cameras.usb_camera import USBCamera
from app.services.recorder.recorder import Recorder


camera = USBCamera()

camera.connect()

success, frame = camera.read()

height, width = frame.shape[:2]

recorder = Recorder()

recorder.start(
    "test.mp4",
    fps=30,
    width=width,
    height=height,
)

count = 0

while count < 300:

    success, frame = camera.read()

    if not success:
        break

    recorder.write(frame)

    cv2.imshow("Recording...", frame)

    if cv2.waitKey(1) == ord("q"):
        break

    count += 1

recorder.stop()

camera.release()

cv2.destroyAllWindows()

print("Recording saved!")