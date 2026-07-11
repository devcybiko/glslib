"""glslib - A Python package for graphics and simulation utilities."""

__version__ = "0.1.0"
__author__ = "Greg"

from .core import greeting
from .glogger import GLogger
from .application import Application
from .gjson import GJSON

__all__ = ["greeting", "GLogger", "Application", "GJSON"]
