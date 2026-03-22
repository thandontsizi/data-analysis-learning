# Matplotlib Commands Reference:

## 1. Importing Matplotlib:
- Command: import matplotlib.pyplot as plt
- Explanation: Imports the plotting module. 'plt' is used to create and display charts.

## 2. Creating a Line Chart (Trends):
- Command: plt.plot(x, y)
- Explanation: Creates a line chart. Used to show trends over time or ordered data.
- Example:
```bash
	x = [1, 2, 3]
	y = [10, 20, 15]

	plt.plot(x, y)
	plt.show()
```
## 3. Creating a Bar Chart (Comparisons):
- Command: plt.bar(categories, values)
- Explanation: Creates a bar chart. Used to compare values across categories.
- Example:
```bash
	categories = ['A', 'B', 'C']
	values = [5, 7, 3]

	plt.bar(categories, values)
	plt.show()
```

## 4. Creating a Histogram (Distribution):
- Command: plt.hist(data, bins=n)
- Explanation: Displays how values are distributed across ranges. Useful for understanding frequency.
- Example:
```bash
	data = [1, 2, 2, 3, 3, 3, 4]

	plt.hist(data, bins=3)
	plt.show()
```

## 5. Adding Titles and Labels:
- Commands: plt.title(), plt.xlabel(), plt.ylabel()
- Explanation: Adds context to the chart so it is what is being shown.
- Example:
```bash
	plt.plot([1, 2, 3], [10, 20, 30])
	plt.title("Sales Trend")
	plt.xlabel("Month")
	plt.ylabel("Revenue")
	plt.show()
```

## 6. Adding a Legend:
- Command: plt.legend()
- Explanation: Labels multiple datasets so they can be distinguished on the same chart.
- Example:
```bash
	x = [1, 2, 3]

	plt.plot(x, [10, 20, 30], label="Product A")
	plt.plot(x, [15, 25, 35], label="Product B")

	plt.legend()
	plt.show()
```

## 7. Adding a Grid:
- Command: plt.grid()
- Explanation: Adds grid lines to improve readability and make values easier to interpret.
- Example:
```bash
	plt.plot([1, 2, 3], [2, 4, 6])
	plt.grid()
	plt.show()
```

## 8. Plotting Multiple Lines:
- Command: Multiple 'plt.plot()' calls.
- Explanation: Plots multiple datasets on the same chart for comparison.
- Example:
```bash
	x = [1, 2, 3]

	plt.plot(x, [1, 4, 9])
	plt.plot(x, [2, 5, 8])

	plt.show()
```

## 9. Displaying the Chart:
- Command: plt.show()
- Explanation: Renders and displays the chart. Must be called to view the output.
- Example:
```bash
	plt.plot([1, 2, 3], [3, 6, 9])
	plt.show()
```
