from app.services.cameras.usb_camera import USBCamera


class CameraManager:
    def __init__(self):
        self.cameras = {}

    def add_camera(self, name: str, camera_index: int):
        self.cameras[name] = USBCamera(camera_index)

    def connect_all(self):
        for camera in self.cameras.values():
            camera.connect()

    def disconnect_all(self):
        for camera in self.cameras.values():
            camera.release()

    def get_camera(self, name: str):
        return self.cameras.get(name)