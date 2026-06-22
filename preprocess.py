import os
import random
from PIL import Image, ImageEnhance

SOURCE_DIR = "."
OUTPUT_DIR = "processed_dataset"

IMG_SIZE = (224, 224)

TRAIN_RATIO = 0.7
VAL_RATIO = 0.15
TEST_RATIO = 0.15

random.seed(42)

# 출력 폴더 생성
for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(OUTPUT_DIR, split), exist_ok=True)


def save_image(img, save_path):
    img = img.convert("RGB")
    img = img.resize(IMG_SIZE)
    img.save(save_path)


for class_name in os.listdir(SOURCE_DIR):

    class_path = os.path.join(SOURCE_DIR, class_name)

    if not os.path.isdir(class_path):
        continue

    images = [
        f for f in os.listdir(class_path)
        if f.lower().endswith(
            (".jpg", ".jpeg", ".png", ".webp")
        )
    ]

    random.shuffle(images)

    total = len(images)

    train_end = int(total * TRAIN_RATIO)
    val_end = train_end + int(total * VAL_RATIO)

    train_files = images[:train_end]
    val_files = images[train_end:val_end]
    test_files = images[val_end:]

    split_dict = {
        "train": train_files,
        "val": val_files,
        "test": test_files
    }

    for split_name, file_list in split_dict.items():

        save_dir = os.path.join(
            OUTPUT_DIR,
            split_name,
            class_name
        )

        os.makedirs(save_dir, exist_ok=True)

        for file_name in file_list:

            src = os.path.join(class_path, file_name)

            try:
                img = Image.open(src)

                base_name = os.path.splitext(file_name)[0]

                original_path = os.path.join(
                    save_dir,
                    f"{base_name}.jpg"
                )

                save_image(img, original_path)

                # Train 데이터만 증강
                if split_name == "train":

                    # 회전
                    rotated = img.rotate(
                        random.randint(-20, 20)
                    )

                    save_image(
                        rotated,
                        os.path.join(
                            save_dir,
                            f"{base_name}_rot.jpg"
                        )
                    )

                    # 밝기
                    bright = ImageEnhance.Brightness(
                        img
                    ).enhance(
                        random.uniform(0.8, 1.2)
                    )

                    save_image(
                        bright,
                        os.path.join(
                            save_dir,
                            f"{base_name}_bright.jpg"
                        )
                    )

                    # 확대
                    w, h = img.size

                    zoom = img.crop(
                        (
                            int(w * 0.05),
                            int(h * 0.05),
                            int(w * 0.95),
                            int(h * 0.95)
                        )
                    )

                    save_image(
                        zoom,
                        os.path.join(
                            save_dir,
                            f"{base_name}_zoom.jpg"
                        )
                    )

            except Exception as e:
                print("오류:", src)
                print(e)

print("전처리 및 증강 완료!")