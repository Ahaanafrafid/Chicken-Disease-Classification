from dataclasses import dataclass
from pathlib import Path

@dataclass#(frozen=True)
class DataIngestionConfig:
    def __init__(self, root_dir: str, source_URL: str, local_data_file: str, unzip_dir: str):
        self.root_dir = root_dir
        self.source_URL = source_URL
        self.local_data_file = local_data_file
        self.unzip_dir = unzip_dir


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: tuple
    params_learning_rate: float
    params_include_top: bool
    params_weight: str
    params_classes: int