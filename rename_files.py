import os

for folder_name in os.listdir("."):
    folder_path = os.path.join(".", folder_name)

    if not os.path.isdir(folder_path):
        continue

    files = [
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]

    files.sort()

    # 임시 이름으로 먼저 변경
    temp_files = []

    for i, file in enumerate(files):
        old_path = os.path.join(folder_path, file)

        temp_name = f"temp_{i}{os.path.splitext(file)[1]}"
        temp_path = os.path.join(folder_path, temp_name)

        os.rename(old_path, temp_path)
        temp_files.append(temp_name)

    # 최종 이름으로 변경
    for i, file in enumerate(temp_files, start=1):
        old_path = os.path.join(folder_path, file)

        ext = os.path.splitext(file)[1]

        new_name = f"{folder_name}_{i:03d}{ext}"
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)

print("파일명 변경 완료!")