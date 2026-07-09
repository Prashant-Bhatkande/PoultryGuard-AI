import cv2

from app.services.cameras.usb_camera import USBCamera


camera = USBCamera()

camera.connect()

while True:
    success, frame = camera.read()

    if not success:
        break

    cv2.imshow("PoultryGuard Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()