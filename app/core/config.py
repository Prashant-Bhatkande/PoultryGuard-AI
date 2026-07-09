from pathlib import Path
import yaml

CONFIG_PATH = Path("config/settings.yaml")


class Config:
    def __init__(self):
        with open(CONFIG_PATH, "r") as f:
            self.data = yaml.safe_load(f)

    def get(self, *keys):
        value = self.data
        for key in keys:
            value = value[key]
        return value


config = Config()