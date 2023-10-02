import os

# Get the path of the file
path = os.path.abspath("output.txt")

# Open the file
file = open(path, "w")

# Write to the file
file.write("Hello World!")

# Close the file
file.close()
