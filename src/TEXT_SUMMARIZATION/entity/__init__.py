from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True) #frozen=True makes the object immutable, like a constant.
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path

#or

"""class DataIngestionConfig:
    def __init__(self, root_dir, source_URL, local_data_file, unzip_dir):
        self.root_dir = root_dir
        self.source_URL = source_URL
        self.local_data_file = local_data_file
        self.unzip_dir = unzip_dir
"""
@dataclass(frozen = True)
class DataValidationConfig:
    root_dir:Path
    status_file:Path
    All_required_file:list