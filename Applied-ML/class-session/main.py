import numpy as np
from linear import LinearRegression

n = 2
x = np.random.rand(n)
y = 2 * x + 7 + (np.random.rand() * 2)

# Set the static values
EPOCHS = 10
LEARNING_RATE = 0.00001

print(x, y)

linear_regression = LinearRegression(x, y)

linear_regression.train(epochs = EPOCHS, learning_rate = LEARNING_RATE)
