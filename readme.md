# Exercise 1: Creating NumPy Arrays

Task 1:
Create a 1D NumPy array containing integers from 0 to 9.

Task 2:
Create a 2D NumPy array with shape (3, 4) filled with random floating-point numbers between 0 and 1.

Task 3:
Create a 3D NumPy array with shape (2, 3, 2) containing consecutive odd numbers starting from 1.
Hint: - look at the reshape method

# Exercise 2: SLice numpy
Task 4:
Look at the following numpy array:
game_board = np.array([[ 1,  2,  3,  4,  5],
                       [ 6,  7,  8,  9, 10],
                       [11, 12, 13, 14, 15],
                       [16, 17, 18, 19, 20],
                       [21, 22, 23, 24, 25]])
Slice and print the subarray of the central 3x3 game board.

# Exercise 3: Slicing and Analyzing Temperature Data

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

# Exercise 4: Broadcasting

Task 6:
Research about broadcasting in numpy
Problem:
You have been given a NumPy array representing the distances of different runners in a race, and another NumPy array representing their average speeds. The distance array contains the distances covered by each runner, and the speed array contains the average speeds of the runners. Perform the following tasks:
Calculate the total time taken by each runner to complete the race (time = distance / speed).
Find the runner(s) with the shortest total time.
Here's the data:
import numpy as np

distances = np.array([800, 1500, 1000, 1200])
average_speeds = np.array([5, 4, 6, 5.5])
Hint: used broadcasting to perform element-wise division