# Examples and Practice for Data Visualization with Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# --- 1. Line Plot ---
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure()
plt.plot(x, y, label='sin(x)', color='blue', linestyle='-')
plt.title('Line Plot Example')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()

# --- 2. Scatter Plot ---
x = np.random.rand(50)
y = np.random.rand(50)
plt.figure()
plt.scatter(x, y, color='red', marker='o')
plt.title('Scatter Plot Example')
plt.xlabel('Random X')
plt.ylabel('Random Y')
plt.show()

# --- 3. Bar Chart ---
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]
plt.figure()
plt.bar(categories, values, color='green')
plt.title('Bar Chart Example')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

# --- 4. Histogram ---
data = np.random.randn(1000)
plt.figure()
plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# --- 5. Pie Chart ---
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [15, 30, 45, 10]
plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart Example')
plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
plt.show()

# --- 6. Customizing and Saving a Figure ---
x = np.arange(1, 6)
y = [1, 4, 9, 16, 25]
plt.figure()
plt.plot(x, y, 'bo--', label='Squares')
plt.title('Customized Plot')
plt.xlabel('Number')
plt.ylabel('Square')
plt.legend()
plt.savefig('custom_plot.png')  # Saves the figure to a file
plt.close()

# --- 7. Using Matplotlib with Pandas ---
import pandas as pd
df = pd.DataFrame({
    'x': np.arange(1, 6),
    'y': [2, 3, 5, 7, 11]
})
df.plot(x='x', y='y', kind='line', marker='o', title='Pandas Line Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# --- Questions ---
# 1. How do you add a legend to a matplotlib plot?
# 2. What function do you use to save a figure to a file?
# 3. How can you plot multiple lines on the same axes? 