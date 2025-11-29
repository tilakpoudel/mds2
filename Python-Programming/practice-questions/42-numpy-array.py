# Write a program to find sum and average of 10 numbers stored in a numpy array.

import numpy as np

def sum_and_average_of_array(arr):
    total_sum = np.sum(arr)
    average = np.mean(arr)

    return total_sum, average

# Example usage
numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
total_sum, average = sum_and_average_of_array(numbers)
print(f"Sum of the array: {total_sum}")
print(f"Average of the array: {average}")

# Output the sum and average
print(f"Sum: {total_sum}, Average: {average}")
