import logging
import pandas as pd 
from.config import ModelNameConfig
from src.model_dev import LogisticRegressionModel
from sklearn.base import ClassifierMixin
import mlflow
import joblib
import os

from logs.logging_config import setup_logging

# Setup logging
setup_logging()

# Create a logger for this file
logger = logging.getLogger(__name__)

def model_train(
    X_train:pd.DataFrame,
    y_train:pd.DataFrame)->ClassifierMixin:
    """
    Trains the model on the ingested data 
    """
    """
    Args:
        X_train: pd.DataFrame
        X_test: pd.DataFrame
        y_train:pd.DataFrame
        y_test:pd.DataFrame
    """
    """
    Returns:
            RegressorMixin
    """
    try:
        model = None
        config = ModelNameConfig()
        if config.model_name =='LogisticRegression':
            mlflow.sklearn.autolog()
            model =LogisticRegressionModel()
            trained_model = model.train(X_train,y_train)
            
        
         # Specify the save path
            save_dir = "saved_model"
            os.makedirs(save_dir, exist_ok=True)
            model_path = os.path.join(save_dir, "model.pkl")
            
            # Save the trained model
            joblib.dump(trained_model, model_path)
            logger.info(f"Model saved at {model_path}")
            return trained_model
        
        else:
            raise ValueError("Model {} not supported".format(config.model_name))
    except Exception as e:
        logger.error(f'Error in training the model {e}')
        raise e 