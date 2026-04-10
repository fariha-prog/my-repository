# 

# import matplotlib as plt
# plt.imshow(matrix,cmap='coolwarm')
# plt.colorbar()
# plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Create a sample matrix
matrix = np.array([
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [15, 25, 35, 45, 55],
    [85, 75, 65, 55, 45],
    [90, 80, 70, 60, 50]
])

# Plot the heatmap
plt.imshow(matrix, cmap='coolwarm')

# Add colorbar
plt.colorbar()

# Show the plot
plt.show()