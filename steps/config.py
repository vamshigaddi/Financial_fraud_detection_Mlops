from pydantic import BaseModel

class ModelNameConfig(BaseModel):
    """Model Configurations"""
    
    model_name:str = "LogisticRegression"
    fine_tuning:bool = False


config = ModelNameConfig()
