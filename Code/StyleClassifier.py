import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import time

#################################################################################################################
### Other Functions

def TrainStyleClassifier():
    locations_dataset_DF = pd.read_csv('Data\locations_dataset.csv')
    
    style_classifier_model = 0
    return style_classifier_model

#################################################################################################################
### Variables

#################################################################################################################
### Main Code

if __name__ == "__main__":
    start_time = time.time()
    TrainStyleClassifier()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")