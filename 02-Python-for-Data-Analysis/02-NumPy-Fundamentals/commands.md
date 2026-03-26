# NumPy Commands Reference:

## 1. Importing NumPy:
- Command: import numpy as np
- Explanation: Imports the NumPy library and gives it the alias 'np' which is standard shorthand for easier use in code.

---

## 2. Creating Arrays:
- Command: np.array([elements])
- Explanation: Creates a 1D or 2D array.
- Example:
	```bash
		arr = np.array([4, 5, 6])
		print(arr)

		Output: [4 5 6]
	```

---

## 3. Array Operations:
- Command: +, -, *, /
- Explanation: Element-wise operations.
- Example:
	```bash
		arr = np.array([1, 2, 3])
		print(arr * 2)

		Output: [2 4 6]
	```

---

## 4. Aggregation Functions:
- Commands: .sum(), .mean(), np.median(), .max(), .min()
- Explanation: Summarise data in an array.
- Example:
	```bash
		arr = np.array([1, 2, 3, 4, 5])
		print("Sum: ", arr.sum())
		print("Mean: ". arr.mean())
		print("Mean: ", np.median(arr))
		print("Max: ", arr.max())
		print("Min: ", arr.min())

		Output:
		Sum: 15
		Mean: 3.0
		Median: 3.0
		Max: 5
		Min: 1
	```

---

## 5. Indexing and Slicing:
- Commands: arr[index], arr[start:end]
- Explanation: Access individual elements or subsets of an array.
- Example:
	```bash
		arr = np.array([10, 20, 30, 40])
		print("First Element: ", arr[0])
		print("Slice: ", arr[1:3])

		Output:
		First Element: 10
		Slice: [20 30]
	```

---

## 6. 2D Arrays/Matrices:
- Command: np.array([row1], [row2])
- Explanation: Creates multi-dimensional arrays for more complex data. Columns and rows can be accessed using slicing.
- Example:
	```bash
		matrix = np.array([[1, 2, 3], [4, 5, 6]])
		print("Matrix: \n", matrix)
		print("Second Column: ", matrix[:,1])

		Output:
		Matrix:
			[[1 2 3]
			 [4 5 6]]
		Second Column: [2 5]
	```

---

## 7. Creating Arrays with Built-in Functions:
- Commands: np.zeros(), np.ones(), np.arange(), np.linspace()
- Explanation: Quickly generate arrays filled with zeros, ones, or ranges of numbers.
- Examples:
	```bash
		zeros = np.zeros(5)
		ones = np.ones(3)
		range_arr = np.arange(1, 10, 2) # Start = 1, Stop = 10, Step = 2.
		linspace_arr = np.linspace(0, 1, 5) # 5 evenly spaced numbers from 0 to 1.

		print("Zeros: ", zeros)
		print("Ones: ", ones)
		print("Range: ", range_arr)
		print("Linspace: ", linspace_arr)

		Output:
		Zeros: [0. 0. 0. 0. 0.]
		Ones: [1. 1. 1.]
		Range: [1 3 5 7 9]
		Linspace: [0.  0.25 0.5 0.75 1. ]
	```
