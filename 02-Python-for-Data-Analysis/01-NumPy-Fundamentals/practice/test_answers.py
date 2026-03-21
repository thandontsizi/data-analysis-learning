import numpy as np

# NumPy Test Answers:

# Basic Exercises:
## 1. Array Creation:
arr = np.array([10, 20, 30, 40, 50])
print("First Array: ", arr)

## 2. Array Multiplication:
arr2 = np.array([1, 2, 3, 4])
print("Sample Array: ", arr2)
print("Sample Array times 3: ", arr2 * 3)

## 3. Array with steps:
range_arr = np.arange(10, 50, 5)
print(range_arr)


# Aggregation Exercises:
## 1. Aggregate [5, 10, 15, 20, 25]
arr3 = np.array([5, 10, 15, 20, 25])
print("Sum: ", arr3.sum())
print("Mean: ", arr3.mean())
print("Median: ", np.median(arr3))
print("Maximum: ", arr3.max())
print("Minimum: ", arr3.min())
