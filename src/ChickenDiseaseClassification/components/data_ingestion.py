import os
import urllib.request as request
import zipfile
from src.ChickenDiseaseClassification import logger
from src.ChickenDiseaseClassification.utils.common import get_size
from src.ChickenDiseaseClassification.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
  def __init__(self, config: DataIngestionConfig):
    self.config = config


  def download_file(self):
    if not os.path.exists(self.config.local_data_file):
      filename, headers = request.urlretrieve(
        url = self.config.source_URL,
        filename = self.config.local_data_file
      )
      logger.info(f"{filename} Download! with following info: \n{headers}")
    else:
        logger.info(f"File already exsists of size: {get_size(Path(self.config.local_data_file))}")


  def extract_zip_file(self):
    """
    Zip_file_path: str
    extracts the zip file into the data directory
    functions returns none

    """
    unzip_path = self.config.unzip_dir
    os.makedirs(unzip_path, exist_ok=True)
    with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
        zip_ref.extractall(unzip_path)