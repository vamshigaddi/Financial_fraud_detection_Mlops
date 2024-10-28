import logging
import pandas as pd
from src.evaluation import Accuracy, Precision, Recall, F1Score
from sklearn.base import ClassifierMixin
from typing import Tuple
from typing_extensions import Annotated
import mlflow
from logs.logging_config import setup_logging
import json

# Setup logging
setup_logging()

# Create a logger for this file
logger = logging.getLogger(__name__)


def evaluate_model(
    model: ClassifierMixin,
    X_test: pd.DataFrame,
    y_test: pd.Series
) -> Tuple[
    Annotated[float, 'accuracy'],
    Annotated[float, 'precision'],
    Annotated[float, 'recall'],
    Annotated[float, 'f1_score']
]:
    """
    Evaluates the classification model on the test data.

    Args:
        model: Trained classification model
        X_test: Test features
        y_test: True labels for the test data
    
    Returns:
        A tuple containing accuracy, precision, recall, and f1 scores.
    """
    try:
        predictions = model.predict(X_test)
        
        # Calculate and log Accuracy
        accuracy_class = Accuracy()
        accuracy = accuracy_class.calculate_scores(y_test, predictions)
        mlflow.log_metric('accuracy', accuracy)
        
        # Calculate and log Precision
        precision_class = Precision()
        precision = precision_class.calculate_scores(y_test, predictions)
        mlflow.log_metric('precision', precision)
        
        # Calculate and log Recall
        recall_class = Recall()
        recall = recall_class.calculate_scores(y_test, predictions)
        mlflow.log_metric('recall', recall)
        
        # Calculate and log F1 Score
        f1_class = F1Score()
        f1_score = f1_class.calculate_scores(y_test, predictions)
        mlflow.log_metric('f1_score', f1_score)
        
        #save metrics to metrics.json file
        metrics = {
            'accuracy':accuracy,
            'precision':precision,
            'recall':recall,
            'f1_score': f1_score
        }
        with open('metrics.json','w') as file:
            json.dump(metrics,file,indent=4)
        
        logger.info('metrics are saved to metrics.json file')
        
        return accuracy, precision, recall, f1_score
   
    except Exception as e:
        logger.error(f'Error in evaluating the model: {e}')
        raise e
