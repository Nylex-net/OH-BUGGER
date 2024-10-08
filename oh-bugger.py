import os
import shutil
import asyncio

# Asynchronous file creation function
async def create_files(directory_path):

    async def make_file(path, content):
        with open(path, "w") as file:
            file.write(content)

    usage = shutil.disk_usage(directory_path)

    # Create the directory if it doesn't exist.
    os.makedirs(directory_path, exist_ok=True)

    # Content of text file.
    BUGGER = r"""
        ,
       /|
      / |
     /  /
    |   |
   /    |
   |    \_
   |      \__
   \       __\_______
    \                 \_
    | /                 \
    \/                   \
     |                    |
     \                   \|
     |                    \
     \                     |
     /\    \_               \
    / |      \__ (   )       \
   /  \      / |\\  /       __\____
snd|  ,     |  /\ \ \__    |       \_
   \_/|\___/   \   \}}}\__|  (@)     )
    \)\)\)      \_\---\   \|       \ \
                  \>\>\>   \   /\__o_o)
                            | /  VVVVV
                            \ \    \
                             \ \MMMMM                  oh bugger!
                              \______/         _____ /
                                              |  O O|
                                             /___|_|/\_
                                        ==( |          |
                                             (o)====(o)
"""
    # Create text files containing the content until we hit an amount of free space left.
    i = 0
    try:
        while (usage.free / 1024) > 2:
            file_name = f"oh-bugger_{i}.txt"
            file_path = os.path.join(directory_path, file_name)
            if not os.path.exists(file_path):
                await make_file(file_path, BUGGER)
                usage = shutil.disk_usage(directory_path)
            i += 1
    except KeyboardInterrupt as k:
        print(f"Okay fine, here are the directory results:")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Print space details of drive.
    print(f"Drive: {directory_path}")
    print(f"Total: {usage.total / 1024:.2f} KB")
    print(f"Used: {usage.used / 1024:.2f} KB")
    print(f"Free: {usage.free / 1024:.2f} KB")

# Main asynchronous function to run the code
async def main():
    # Define the directory path.
    directory_path = "S:\\"
    await create_files(directory_path)

# Run the event loop
asyncio.run(main())