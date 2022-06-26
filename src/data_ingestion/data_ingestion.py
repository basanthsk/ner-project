import argparse
import os
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories
import random
from datasets import load_dataset


STAGE = "STAGE_NAME" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


class DataIngestion:
    def __init__(self,config):
        self.config = config 
        self.dataset_name = config["dataset_name"]["name"]
        self.subset = config["dataset_name"]["subset"]
        self.cache_dir = os.path.join(
            config["artifacts"]["artifacts_dir"],
            config["artifacts"]["cache_dir"])

    def get_data(self):    
        en_dataset = load_dataset(self.dataset_name,self.subset,cache_dir=self.cache_dir)
        logging.info(f"dataset downloaded {self.cache_dir}")

def main(config_path):
    ## read config files
    config = read_yaml(config_path)
    data_ingestion = DataIngestion(config)
    data_ingestion.get_data()
    


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e