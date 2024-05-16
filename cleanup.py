import os

# Define the path to the text file you want to delete
directory_path  = "S:/"

# Create the directory if it doesn't exist
os.makedirs(directory_path, exist_ok=True)

# Iterate through all existing files whose title contains "oh-bugger" and delete them.
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.exists(file_path) and os.path.isfile(file_path) and filename.find("oh-bugger") != -1:
        os.remove(file_path)