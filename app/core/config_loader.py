"""
PoultryGuard AI

Configuration Loader
"""

from pathlib import Path
import yaml


class ConfigLoader:
    def __init__(self):
        self.config_dir = Path("config")

    def load(self, filename: str) -> dict:
        file_path = self.config_dir / filename

        if not file_path.exists():
            raise FileNotFoundError(f"{filename} not found.")

        with open(file_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)