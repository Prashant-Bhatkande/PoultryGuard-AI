from app.services.cameras.manager import CameraManager

manager = CameraManager()

manager.add_camera("Main Camera", 0)

manager.connect_all()

camera = manager.get_camera("Main Camera")

while True:
    success, frame = camera.read()

    if not success:
        break

    import cv2
    cv2.imshow("Camera Manager Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

manager.disconnect_all()
cv2.destroyAllWindows()