from PIL import Image, ImageFilter
import os

path = './imgs'
pathOut = '/editedImgs'

if not os.path.exists(path):
    print(f"Input folder '{path}' does not exist. Please check the path. ")
    exit()

for filename in os.listdir(path):
    img = Image.open(os.path.join(path, filename))

    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    clean_name = os.path.splitext(filename)[0]

    if not os.path.exists(pathOut):
        os.makedirs(pathOut)

    edit.save(os.path.join(pathOut, f"{clean_name}_edit.jpg"))

print("Image processing completed!")