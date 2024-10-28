import logging
from abc import ABC, abstractmethod
from typing import Union

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from logs.logging_config import setup_logging

# Setup logging
setup_logging()

# Create a logger for this file
logger = logging.getLogger(__name__)


class DataStrategy(ABC):
    """
    Abstract Class defining strategy for handling data 
    """
    @abstractmethod
    def handle_data(self,data:pd.DataFrame) ->Union[pd.DataFrame,pd.Series]:
        pass
    
class DataPreprocessStrategy(DataStrategy):
    """
    Data preprocessing strategy which preprocess the data 
    """
    def handle_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Removes columns which are not required, fills missing values with median average values, and converts the data type to float. 
        """
        try:
            # Remove leading and trailing spaces from all column names
            data.columns = data.columns.str.strip()  

            # Drop specified columns from the DataFrame
            data = data.drop(
                [
                    'timestamp',
                    'user_id'
                ],
                axis=1,
            )
            
            # Initialize the LabelEncoder
            label_encoder = LabelEncoder()

            # Apply LabelEncoder to the 'location' column
            data['location'] = label_encoder.fit_transform(data['location'])

            # Apply LabelEncoder to the 'device_type' column
            data['device_type'] = label_encoder.fit_transform(data['device_type'])

            # Select only numerical columns
            #data = data.select_dtypes(include=[np.number])

            return data

        except Exception as e:
            logger.error(e)
            raise e


class DataDivideStrategy(DataStrategy):
    """
    Data dividing strategy which divides the data into train and test data.
    """

    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        """
        Divides the data into train and test data.
        """
        try:
            X = data.drop("is_fraud", axis=1)
            y = data["is_fraud"]
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            return X_train, X_test, y_train, y_test
        except Exception as e:
            logger.error(e)
            raise e


class DataCleaning:
    """
    Data cleaning class which preprocesses the data and divides it into train and test data.
    """

    def __init__(self, data: pd.DataFrame, strategy: DataStrategy) -> None:
        """Initializes the DataCleaning class with a specific strategy."""
        self.df = data
        self.strategy = strategy

    def handle_data(self) -> Union[pd.DataFrame, pd.Series]:
        """Handle data based on the provided strategy"""
        return self.strategy.handle_data(self.df)