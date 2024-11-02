from steps.ingest_data import ingest_df
from steps.clean_data import clean_df
from steps.model_train import model_train
from steps.evaluation import evaluate_model



def training_pipeline(data_path:str):
    df = ingest_df(data_path)
    X_train,X_test,y_train,y_test = clean_df(df)
    model = model_train(X_train,y_train)
    accuracy,precision,recall,f1_score = evaluate_model(model,X_test,y_test)
 
 