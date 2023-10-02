# Part 4
import os

# Get the path of the file
path = os.path.abspath("pseudo-code.txt")

# Open the file
file = open(path, "r")

# Read the file
print(file.read())

# Close the file
file.close()