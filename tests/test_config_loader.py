import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.core.config_loader import ConfigLoader

loader = ConfigLoader()

camera_config = loader.load("cameras.yaml")
app_config = loader.load("app.yaml")

print("Camera Config:")
print(camera_config)

print("\nApp Config:")
print(app_config)