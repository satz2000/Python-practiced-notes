# How to read a text file
Files = open("Files.txt", "r")

# Read the entire files
print(Files.read())

# Read a line at a time
print(Files.readline())

# Reading all lines at a time
print(Files.readlines())

# To check files is readable or not?
print(Files.readable())
