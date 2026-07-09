"""
PoultryGuard AI

Camera Interface

Every camera implementation must inherit from this class.
"""

from abc import ABC, abstractmethod
from typing import Any


class CameraInterface(ABC):
    """Base interface for all camera types."""

    @abstractmethod
    def connect(self) -> bool:
        """Connect to the camera."""
        pass

    @abstractmethod
    def read(self) -> tuple[bool, Any]:
        """Read a frame from the camera."""
        pass

    @abstractmethod
    def release(self) -> None:
        """Release the camera."""
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        """Return camera connection status."""
        pass