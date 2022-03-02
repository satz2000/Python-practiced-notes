nums = [12, 3, 4, 5, 43, 34]

# Filter function
print("Filter function:")
even = list(filter(lambda a: a % 2 == 0, nums))
print(even)

# Map function
print("-----------------------------------------")
print("Map function:")
double = list(map(lambda a: a * 2, even))
print(double)

from functools import reduce
# Reduce function
print("----------------------------------------")
print("Reduce function:")
sum = reduce(lambda a,b: a + b, double)
print(sum)
