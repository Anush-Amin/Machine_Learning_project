import sys

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

class DataTransformation:
    def __init__(self):
        self.preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        
        '''
        try:
            numerical_columns = ['Indian_dish', 'Foreign_dish', 'Mixed_dish', 'votes', 'approx_cost(for two people)', 'has_phone']
            categorical_columns = ['online_order', 'book_table', 'listed_in(type)', 'listed_in(city)', 'restaurant_type']
            # categorical_columns = ['restaurant_type', 'location']
            # numerical_columns = ['online_order', 'book_table', 'votes', 'approx_cost_for_two_people', 'has_phone']

            num_pipeline= Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )

            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("cat_pipelines",cat_pipeline,categorical_columns)
                ]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="rate"
            
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info("Applying preprocessing object on training dataframe and testing dataframe.")

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            logging.info(f"input_feature_train_arr shape: {input_feature_train_arr.shape}")
            logging.info(f"target_feature_train_df shape: {target_feature_train_df.shape}")
            logging.info(f"target_feature_train_df array shape: {len(np.array(target_feature_train_df))}")

            logging.info(f"input_feature_train_arr: {input_feature_train_arr[0]}")
            logging.info(f"target_feature_train_df: {np.array(target_feature_train_df)}")
            logging.info(f"target_feature_train_df: {target_feature_train_df}")

            train_arr = np.c_[input_feature_train_arr, target_feature_train_df]
            test_arr = np.c_[input_feature_test_arr, target_feature_test_df]
            # train_arr = np.c_[
            #     input_feature_train_arr, np.array(target_feature_train_df)
            # ]
            # test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path=self.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)