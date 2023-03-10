"""Enum file for file extension to be read"""
from enum import Enum

class FileExtension(str,
                    Enum):
    """Filter file extension type"""
    JSON = "json"
    CSV = "csv"
