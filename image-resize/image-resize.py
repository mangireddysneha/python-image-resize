import os
from PIL import Image


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INPUT_FOLDER = os.path.join(BASE_DIR, "images")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "resized_images")
TARGET_WIDTH, TARGET_HEIGHT = 200, 300
OUTPUT_FORMAT = "png"


def is_image_file(filename):
    valid_extensions = (".png", ".jpg", ".jpeg", ".bmp", ".gif")
    return filename.lower().endswith(valid_extensions)

def prepare_output_directory(path):
    os.makedirs(path, exist_ok=True)

def process_image(file_path, save_path, size, format_):
    with Image.open(file_path) as img:
        mode = "RGBA" if format_.upper() == "PNG" else "RGB"
        resized = img.resize(size).convert(mode)
        resized.save(save_path, format_)
        print(f"✅ Saved: {os.path.basename(save_path)}")

def main():
    prepare_output_directory(OUTPUT_FOLDER)

    images = [f for f in os.listdir(INPUT_FOLDER) if is_image_file(f)]
    if not images:
        print("⚠️ No valid image files found in the folder.")
        return

    for img_file in images:
        source_path = os.path.join(INPUT_FOLDER, img_file)
        name, _ = os.path.splitext(img_file)
        target_filename = f"{name}.{OUTPUT_FORMAT.lower()}"
        target_path = os.path.join(OUTPUT_FOLDER, target_filename)
        process_image(source_path, target_path, (TARGET_WIDTH, TARGET_HEIGHT), OUTPUT_FORMAT)

if __name__ == "__main__":
    main()
