import numpy as np

def mse(y, y_predicted):
    """
    Computes mean squared error

    :params y: actual value
    :params y_predicted: predicted value
    """

    return np.sum((y - y_predicted) ** 2 ) / len(y)
    # return np.mean((y-y_predicted) ** 2)