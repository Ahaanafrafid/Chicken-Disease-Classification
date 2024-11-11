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
    params_weights: str
    params_classes: int

@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir:Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path 

@dataclass(frozen = True)
class TrainingConfig:
  root_dir: Path
  trained_model_path: Path
  updated_base_model_path: Path
  training_data: Path
  params_epochs: int
  params_batch_size: int
  params_is_augumentation: bool
  params_image_size: list


@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    all_params: dict
    params_image_size: list
    params_batch_size: int