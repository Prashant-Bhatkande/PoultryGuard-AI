"""
PoultryGuard AI

Camera Exceptions
"""


class CameraError(Exception):
    """Base camera exception."""
    pass


class CameraConnectionError(CameraError):
    """Raised when camera connection fails."""
    pass


class CameraReadError(CameraError):
    """Raised when a frame cannot be read."""
    pass


class CameraDisconnectedError(CameraError):
    """Raised when camera disconnects unexpectedly."""
    pass