import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import time

# Start timing
start_time = time.time()

# Define the Anscombe data
anscombe = pd.DataFrame({
    'x1': [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
    'x2': [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
    'x3': [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
    'x4': [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8],
    'y1': [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68],
    'y2': [9.14, 8.14, 8.74, 8.77, 9.26, 8.1, 6.13, 3.1, 9.13, 7.26, 4.74],
    'y3': [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73],
    'y4': [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89]
})

# Perform OLS regression for each dataset
for i in range(1, 5):
    design_matrix = sm.add_constant(anscombe[f'x{i}'])
    model = sm.OLS(anscombe[f'y{i}'], design_matrix).fit()
    print(f"Set {i} - Python")
    print(model.summary())

# Measure execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time (Python): {execution_time:.4f} seconds")

# Output for comparison
with open("python_results.txt", "w") as f:
    for i in range(1, 5):
        design_matrix = sm.add_constant(anscombe[f'x{i}'])
        model = sm.OLS(anscombe[f'y{i}'], design_matrix).fit()
        f.write(f"Set {i} - Python\n")
        f.write(model.summary().as_text())
        f.write("\n")
    f.write(f"Execution Time (Python): {execution_time:.4f} seconds\n")
