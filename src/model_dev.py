import logging
from abc import  ABC,abstractmethod
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from logs.logging_config import setup_logging

# Setup logging
setup_logging()

# Create a logger for this file
logger = logging.getLogger(__name__)



class Model(ABC):
    """
    Abstract class for all models 
    """
    @abstractmethod
    def train(self,x_train,y_train):
        """
        Trains the model 
        """
        """
        Args:
            x_train: training data
            y_train: training labels 
        """
        """
        Returns:
            None 
        """
        pass

class LogisticRegressionModel(Model):
    """
    LinearRegression Model 
    """
    def train(self,x_train,y_train,**kwargs):
        """
        Trains the model 
        """
        """
        Args:  
            x_train:training data
            y_train: training label 
        """
        """ 
        Returns:
            None
        """
        try:
            classifier = LogisticRegression(**kwargs)
            classifier.fit(x_train,y_train)
            logger.info('Model Training completed')
            return classifier
        except Exception as e:
            logger.error(f'Error in training the model:{e}')
            raise e
            

class RandomForestModel(Model):
    """
    RandomForestModel that implements the Model interface.
    """

    def train(self, x_train, y_train, **kwargs):
        """
        Trains the model 

        Args:  
            x_train:training data
            y_train: training label 
        

        Returns:
            None
        """
        try:
            classifier = RandomForestClassifier(**kwargs)
            classifier.fit(x_train, y_train)
            logger.info('model training completed')
            return classifier
        except Exception as e:
            logger.error(f"error in training the model {e}")
            raise e
