# First you have to integrate the data from the different sources.
# Importing Useful Libraries
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig


# from src.components.model_trainer import ModelTrainer
# Remember - when we are performing data ingestion component their should be an input that will be required for the data ingestion component the input like where i save tranning path, where i save the test data, where i save the predicted data those type of input we saved into the class. that called Data Ingestion Config Class.

@dataclass # @dataclasses we use when we need to store only variables , it saves time & space as we no need to write constructor
class DataIngestionConfig:
    # to store our tranning data.
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")
    # This class will knows where to stored our data.
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

     # If my data is stored in some database then this function will work
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv') #here you change the code and read from the mongoDB or SQL any other way
            logging.info('Read the dataset as dataframe')

            # Now creating the folder 
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) # if the file has alread in the dir so we cannot create the new dir.
            
            # Converting data into the CSV file
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
