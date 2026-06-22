import os

for folder_name in os.listdir("."):
    folder_path = os.path.join(".", folder_name)

    if os.path.isdir(folder_path):
        count = len([
            f for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
        ])

        print(f"{folder_name}: {count}장")