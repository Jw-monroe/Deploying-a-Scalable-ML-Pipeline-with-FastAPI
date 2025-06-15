import pytest
import os
import pandas as pd
import numpy as np
from ml.model import train_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
# TODO: add necessary import


@pytest.fixture(scope="session")
def data():
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")
    df = pd.read_csv(data_path)
    return df


# TODO: implement the first test. Change the function name and input as needed
def test_RandomForestClassifier():
    """
    Testing that the model being utilized is random forest
    """
    X_dummy = np.random.rand(10, 5)
    y_dummy = np.random.randint(0, 2, 10)
    model = train_model(X_dummy, y_dummy)
    assert isinstance(model, RandomForestClassifier), f"Expected RandomForestClassifier, got {type(model)}"


# TODO: implement the second test. Change the function name and input as needed
def test_for_NaN_null_values(data):
    """
    checking for null data in records that is not represented by "?"
    """
    null_counts = data.isnull().sum()
    total_nulls = null_counts.sum()

    assert total_nulls == 0, f"Data contains {total_nulls} null values:\n{null_counts[null_counts > 0]}"


# TODO: implement the third test. Change the function name and input as needed
def test_train_test_split_proportions(data):
    """
    Testing to ensure that data set is being split correctly. while still allowing for small rounding errors.
    """
    train, test = train_test_split(data, test_size=0.2, random_state=12)
    total_rows = len(data)
    assert abs(len(test) - total_rows * 0.2) <= 1, "Test size off by more than 1"