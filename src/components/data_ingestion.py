import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from pymongo import MongoClient

class DataIngestion:
    def __init__(self):
        self.train_data_path = os.path.join('artifacts', 'train.csv')
        self.test_data_path = os.path.join('artifacts', 'test.csv')
        self.raw_data_path = os.path.join('artifacts', 'data.csv')

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:
            df = pd.read_csv('data\cleaned_zomato_data_2.csv')
            logging.info(f"Columns: {df.columns}")
            df.drop('name', inplace=True, axis=1)
            logging.info("Read the dataset as dataframe")
            logging.info(f"Dataframe is: {df}")

            # make the directory for train data
            os.makedirs(os.path.dirname(self.train_data_path), exist_ok=True)
            # convert the dataframe df into csv and save it as data.csv
            df.to_csv(self.raw_data_path, index=False, header=True)
            
            logging.info("Train Test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.train_data_path, index=False, header=True)
            test_set.to_csv(self.test_data_path, index=False, header=True)

            logging.info("Ingestion of data is completed")

            return(
                self.train_data_path,
                self.test_data_path
            )
        except Exception as e:
            logging.info(e)
            raise CustomException(e, sys)


if __name__=="__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))