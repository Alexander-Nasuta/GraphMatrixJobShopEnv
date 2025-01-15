from pathlib import Path
from PIL import Image

def replace_black_with_transparent(image_path):
    img = Image.open(image_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        # Change all black (also shades of black)
        # to transparent
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(image_path, "PNG")

def process_folder(folder_path):
    folder = Path(folder_path)
    for file_path in folder.glob("*.png"):
        replace_black_with_transparent(file_path)

if __name__ == "__main__":
    for mode in ['asni', 'debug', 'default', 'window']:
        process_folder(mode)