"""
Task 5:
Problem:
You have been given a 2D NumPy array representing temperature data across different days and cities. Each row corresponds to a city, and each column corresponds to a day. Perform the following tasks:
Here's the temperature data:
import numpy as np

temperature_data = np.array([[28, 30, 32, 29, 27, 26, 28],
                             [31, 33, 30, 29, 28, 25, 26],
                             [24, 26, 25, 28, 30, 29, 27],
                             [22, 23, 26, 21, 20, 24, 26],
                             [29, 31, 33, 32, 30, 28, 27]])
Slice and print the temperatures for the first 3 cities and the first 5 days.
Calculate and print the average temperature for each city.
Find and print the city with the highest average temperature.
Hint:
research on np.mean and have a look at the axis prameter
research the np.argmax

"""

# Solution

import numpy as np

temperature_data = np.array([[28, 30, 32, 29, 27, 26, 28],
                             [31, 33, 30, 29, 28, 25, 26],
                             [24, 26, 25, 28, 30, 29, 27],
                             [22, 23, 26, 21, 20, 24, 26],
                             [29, 31, 33, 32, 30, 28, 27]])

# Task 1: Slice and print temperatures for the first 3 cities and first 5 days
sliced_data = temperature_data[:3, :5]
print("Sliced Data:\n", sliced_data)

# Task 2: Calculate and print average temperature for each city
average_temperatures = np.mean(temperature_data, axis=1)
print("\nAverage Temperatures for Each City:\n", average_temperatures)

# Task 3: Find and print the city with the highest average temperature
city_with_highest_avg_temp = np.argmax(average_temperatures)
print("\nCity with Highest Average Temperature:", city_with_highest_avg_temp)
