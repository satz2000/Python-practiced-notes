"""
# What is variable?
    Variable is reserved memory location to store values.
    Name of the variable are starts with alphabets and underscore(val, _val) not start with number or any others(any numeric value)
"""

# Assign a variable for this value to store in memory
val = 10        # 10 is value that are stored using variable name

_name = "Sathish"
print(_name)

# To find the ID of the variable using inbuilt function
print(id(val))


# For same value but different variable in python will store in same memory
a = 10
print(id(a))     # Both are different variable but has same ID bcoz of same value


# Data types or variable types
"""
There are 8 data types or variable types:
1. None
2. Numeric
    * Integers dtype
    * float dtype
    * complex dtype
    * Bool dtype
3. List
4. Tuple
5. Set
6. Dictionary
7. Range
8. String
"""

a = None
print(type(a))

a = 5
print(type(a))

a = 2.5
print(type(a))

a = 6+9j
print(type(a))

a = 8 > 5
print(type(a))

a = [2, 4, 6, 7, 12, 34]
print(type(a))

a = (12, 34, 65, "sathish", 23)
print(type(a))

a = {"sathish", 21, "saran", 20}
print(type(a))

a = {1: "sathish", 2: "saran"}
print(type(a))

a = "hai buddy"
print(type(a))

a = range(0, 10)
print(type(a))
