# How to append the data/characters into the files

# How to open a files and append the value
Files = open("Files.txt", "a")              # "a" denotes the methods of appending
Files.write("\nHai sir")                    # writing the new data with the last lines by appending methods
Files.write("\nHello")

# close the files after opening and writing
Files.close()