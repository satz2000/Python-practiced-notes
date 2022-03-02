"""
# What is Dictionary ?
    A dictionary is unordered and mutable that stores mapping of unique keys with values.
    {} is represented as dictionary
"""

names = {1: "Sathish", 2: "Saran", 4: "Shiva", 5: "Ragu"}

# Some method in Dictionary

print(names.keys())        # Getting the unique keys
print(names.values())      # Getting the values that are stored
print(names.get(2))        # Gets the value that are mapping with keys
print(names.items())       # Prints the Key with Values

# If there is no key instant of showing error we show something understandable
print(names.get(3, "Not Found"))   # Only print "Not Found" if the key is present

# Delete the specific values with the unique keys
del names[4]               # there is no remove function so we use Del function
print(names)

# Combining the two list into Dictionary
name = ["Sathish", "Saran", "Shiva", "Ragu"]
language = ["Python", "Java", "C++", "R"]

data = dict(zip(name, language))      # zip used to combine the two list then use dict function for mapping
print(data)


# Complex one
data = {"Sathish": 9842922606, "Saran": 8726373289, "Shiva": [8726373289, 9842922606], "Ragu": {"Jio": 9842922606, "Airtel": 8726373289}}

print(data.get("Shiva"))
print(data.get("Ragu")["Jio"])
