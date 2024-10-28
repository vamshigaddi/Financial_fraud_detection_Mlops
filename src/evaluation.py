import logging
from abc import ABC, abstractmethod
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from logs.logging_config import setup_logging

# Setup logging
setup_logging()

# Create a logger for this file
logger = logging.getLogger(__name__)

class Evaluation(ABC):
    """ Abstract class for defining strategy for evaluating our models"""
    @abstractmethod
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """ Calculates scores for the model
        
        Args:
            y_true: true labels
            y_pred: predicted labels
            
        Returns:
            float: the calculated score
        """
        pass

class Accuracy(Evaluation):
    """ Evaluation strategy that uses Accuracy Score """
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        try:
            logger.info('Calculating Accuracy')
            accuracy = accuracy_score(y_true, y_pred)
            logger.info(f'Accuracy: {accuracy}')
            return accuracy
        except Exception as e:
            logger.error(f"Error in calculating Accuracy: {e}")
            raise e

class Precision(Evaluation):
    """ Evaluation strategy that uses Precision Score """
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        try:
            logger.info('Calculating Precision')
            precision = precision_score(y_true, y_pred, average='binary')  # adjust `average` if needed
            logger.info(f'Precision: {precision}')
            return precision
        except Exception as e:
            logger.error(f"Error in calculating Precision: {e}")
            raise e

class Recall(Evaluation):
    """ Evaluation strategy that uses Recall Score """
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        try:
            logger.info('Calculating Recall')
            recall = recall_score(y_true, y_pred, average='binary')  # adjust `average` if needed
            logger.info(f'Recall: {recall}')
            return recall
        except Exception as e:
            logger.error(f"Error in calculating Recall: {e}")
            raise e

class F1Score(Evaluation):
    """ Evaluation strategy that uses F1 Score """
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        try:
            logger.info('Calculating F1 Score')
            f1 = f1_score(y_true, y_pred, average='binary')  # adjust `average` if needed
            logger.info(f'F1 Score: {f1}')
            return f1
        except Exception as e:
            logger.error(f"Error in calculating F1 Score: {e}")
            raise e
