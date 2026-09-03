#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 18:33:20 2026

@author: peg
"""

print("Hello Pegah")
print(1+1)

import numpy as np
import matplotlib.pyplot as plt

# Create x values
x = np.linspace(-10, 10, 400)

# Calculate y = x^2
y = x**2

# Plot
plt.plot(x, y)

# Labels and title
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = x²")

# Add grid
plt.grid(True)

# Show the plot
plt.show()