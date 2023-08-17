"""
Research about broadcasting in numpy
Problem:
You have been given a NumPy array representing the distances of different runners in a race,
and another NumPy array representing their average speeds. The distance array contains
the distances covered by each runner, and the speed array contains the average speeds
of the runners. Perform the following tasks:
Calculate the total time taken by each runner to complete the race (time = distance / speed).
Find the runner(s) with the shortest total time.

Here's the data:
import numpy as np

distances = np.array([800, 1500, 1000, 1200])
average_speeds = np.array([5, 4, 6, 5.5])
Hint: used broadcasting to perform element-wise division

"""   

# Solution

import numpy as np

# Given data
distances = np.array([800, 1500, 1000, 1200])
average_speeds = np.array([5, 4, 6, 5.5])

# Calculate total time taken by each runner using broadcasting
total_times = distances / average_speeds

# Find the index of the runner with the shortest total time
shortest_time_index = np.argmin(total_times)

# Get the shortest time and corresponding runner's information
shortest_time = total_times[shortest_time_index]
shortest_time_runner_distance = distances[shortest_time_index]
shortest_time_runner_speed = average_speeds[shortest_time_index]

# Print results
print("Total times:", total_times)
print("Runner(s) with the shortest total time:")
print("Runner Index:", shortest_time_index)
print("Runner Distance:", shortest_time_runner_distance)
print("Runner Average Speed:", shortest_time_runner_speed)
print("Shortest Time:", shortest_time)

#