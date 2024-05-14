import os

# Define the directory path
directory_path = "S:\\"

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
for i in range(0, 30):
    file_name = f"oh-bugger_{i}.txt"
    file_path = os.path.join(directory_path, file_name)
    with open(file_name, "w") as file:
        file.write(BUGGER)