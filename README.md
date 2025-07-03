# 🖼️ Image Resizer with Python & PIL

This project is a simple yet powerful tool for batch-resizing images using Python and the Pillow (PIL) library. It automatically converts all images from a source folder to a specified size and format, saving them in an output directory. Perfect for preparing image assets for websites, apps, or presentations.

---

## 📁 Folder Structure

```
image_resizer/
├── images/              # Input folder (place your original images here)
├── resized_images/              # Output folder (automatically created if missing)
├── resize.py            # Main Python script to run the resizer
└── README.md            # Project documentation
```

---

## ⚙️ Features

- ✅ Supports multiple formats: JPG, PNG, BMP, GIF
- 📐 Resize all images to your target dimensions
- 🧠 Automatically creates the output folder if it doesn't exist
- 🎯 Converts to desired format (e.g., JPEG or PNG)
- 🛡️ Safe image handling with proper file closing using `with` statement

---

## 🔧 Requirements

Make sure you have Python 3 installed. Then install Pillow:

```bash
pip install Pillow
```

---

## 🚀 How to Use

1. Place your source images inside the `images/` folder.
2. Set your desired size and format in `resize.py` (optional).
3. Run the script:

```bash
python resize.py
```

4. Resized images will be saved in the `resized_images/` folder.

---

## ✏️ Configuration (in `resize.py`)

```python
TARGET_WIDTH, TARGET_HEIGHT = 800, 600
OUTPUT_FORMAT = "JPEG"  # Options: "JPEG", "PNG", etc.
```


