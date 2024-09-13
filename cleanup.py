import os
import asyncio

async def delete_buggers(directory_path):
    # Iterate through all existing files whose title contains "oh-bugger" and delete them.
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.exists(file_path) and os.path.isfile(file_path) and filename.find("oh-bugger") != -1:
            os.remove(file_path)

# Main asynchronous function to run the code
async def main():
    # Define the directory path.
    # Define the path to the text file you want to delete
    PATH  = "S:/"
    await delete_buggers(PATH)

# Run the event loop
asyncio.run(main())