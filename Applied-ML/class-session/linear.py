import numpy as np
from evaluation import mse

class LinearRegression:

    def __init__(self, x, y):
        self.weights = {
            "w1": np.random.rand(),
            "w0" : np.random.rand() 
        }

        self.x = x
        self.y = y

    def train(self, epochs , learning_rate):
        """
        For training linear regression using gradient descent
        """

        for t in range(epochs):
            y_predicted = self.predict()

            mse_error = mse(self.y, y_predicted)

            print(f"Error: {mse_error}")

            error = y_predicted - self.y

            self.weights["w1"] = self.weights["w1"] - learning_rate * np.dot(error, self.x)
            
            print(f"New weight: {self.weights['w1']}")


    def predict(self):
        """
        A linear function that processes single variable in a data with bias.

        :returns y: numpy array after linear transformation
        """
        w1 = self.weights["w1"]
        w0 =self. weights["w0"]

        y_predicted = w1 * self.x + w0

        return y_predicted