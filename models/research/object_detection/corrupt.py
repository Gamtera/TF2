from PIL import Image
import os

img_dir = 'images/train'
for img_file in os.listdir(img_dir):
    if img_file.endswith('.jpg') or img_file.endswith('.jpeg'):
        try:
            img = Image.open(os.path.join(img_dir, img_file))
            img.verify()  # Verifies the image file is not corrupted
            print(f"{img_file} is valid")
        except (IOError, SyntaxError) as e:
            print(f"{img_file} is corrupted: {e}")
