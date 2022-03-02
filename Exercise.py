"""
# BASKETBALL PLAYERS
    You need to calculate and output how many players are in the range of one SD from the mean
"""
# Given data
players = [180, 172, 178, 185, 190, 195, 192, 200, 210,  190]

# importing necessary packages
import numpy as np

# Find mean of the all players
mean = np.mean(players)
print("Mean:",mean)
# Find standard deviation for players
standard_deviation = np.std(players)
print("Standard deviation:",standard_deviation)

# To store value in results for each iteration its increment the value
results = 0
value = []
# Using for loop
for i in players:
    if i <= mean + standard_deviation and i >= mean - standard_deviation:
        value.append(i)
        results += 1

# print the total numbers of players are in range of one_SD from the mean
print(f"total numbers of players are in range of one_SD from the mean: {results}")
print(f"These are the values: {value}")