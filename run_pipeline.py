from pipeline.training_pipeline import training_pipeline
import mlflow


data_path = r'C:\Users\vamsh\OneDrive\Desktop\Mlops_Financial\data\fraud_detection_dataset.csv'
    
if __name__ == "__main__":
    training_pipeline(data_path=data_path)
    print(
        "Now run \n "
        f"    mlflow ui --backend-store-uri '{mlflow.get_tracking_uri()}'\n"
        "To inspect your experiment runs within the mlflow UI.\n"
        "You can find your runs tracked within the `mlflow_example_pipeline`"
        "experiment. Here you'll also be able to compare the two runs.)"
    )