from app.core.logger import get_logger
from app.services.cameras.camera import Camera
from app.services.cameras.manager import CameraManager

logger = get_logger()


def main():
    logger.info("Starting PoultryGuard")

    manager = CameraManager()

    manager.add_camera(Camera(0, "Laptop Camera"))

    manager.start()
    manager.show()


if __name__ == "__main__":
    main()