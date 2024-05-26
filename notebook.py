import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def function_pred():
    plantDepth = pd.read_csv("tomato_details.csv")
    X = plantDepth[["Planted day","Root Depth in cm"]]
    y = plantDepth["water required in Lit"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

    lm = LinearRegression()
    lm.fit(X_train, y_train)
    predictions = lm.predict(X_test)

    return predictions

