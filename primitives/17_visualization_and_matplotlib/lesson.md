# Data Visualization with Matplotlib

## What is it?

Matplotlib is the most widely used Python library for creating static, animated, and interactive visualizations. It is essential for data analysis, scientific computing, and presenting results in a clear, visual way.

---

## Why Use Matplotlib?
- Visualize data to find patterns, trends, and outliers
- Communicate results effectively
- Create publication-quality figures

---

## Basic Plotting Example

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title('Simple Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
```

---

## Customizing Plots
- Change line style, color, and markers:
  ```python
  plt.plot(x, y, color='red', linestyle='--', marker='o')
  ```
- Add grid, legend, and annotations:
  ```python
  plt.grid(True)
  plt.legend(['Data'])
  plt.annotate('Peak', xy=(5, 10), xytext=(3, 8), arrowprops=dict(facecolor='black'))
  ```
- Multiple plots:
  ```python
  y2 = [1, 3, 5, 7, 9]
  plt.plot(x, y, label='y=2x')
  plt.plot(x, y2, label='y=2x-1')
  plt.legend()
  plt.show()
  ```

---

## Other Plot Types
- Scatter plot: `plt.scatter(x, y)`
- Bar chart: `plt.bar(x, y)`
- Histogram: `plt.hist(data, bins=10)`
- Pie chart: `plt.pie(sizes, labels=labels)`

---

## Saving Figures
```python
plt.savefig('my_plot.png')  # Save the current figure to a file
```

---

## Key Points
- Import as `import matplotlib.pyplot as plt`
- Always call `plt.show()` to display the plot (in scripts)
- Use `plt.figure()` to create new figures
- Customize with titles, labels, legends, and styles
- Save figures with `plt.savefig()`
- Matplotlib integrates with pandas and NumPy for data analysis

---

**Interview Tip:**
- Be able to quickly create and customize a basic plot
- Know how to label axes, add a legend, and save a figure
- Understand the difference between plot types and when to use each 