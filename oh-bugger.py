import os
import shutil

# Define the directory path
directory_path = "S:\\"

usage = shutil.disk_usage(directory_path)

# Create the directory if it doesn't exist
os.makedirs(directory_path, exist_ok=True)

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
i = 0
while (usage.free / 1024) > 2:
    file_name = f"oh-bugger_{i}.txt"
    file_path = os.path.join(directory_path, file_name)
    with open(file_path, "w") as file:
        file.write(BUGGER)
        usage = shutil.disk_usage(directory_path)
    i += 1

print(f"Drive: {directory_path}")
print(f"Total: {usage.total / 1024:.2f} KB")
print(f"Used: {usage.used / 1024:.2f} KB")
print(f"Free: {usage.free / 1024:.2f} KB")