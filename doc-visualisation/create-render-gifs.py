from pathlib import Path
from PIL import Image

def create_gif_from_images(folder_path, output_path):
    # Get list of PNG files in the folder, sorted by creation date
    images = sorted(
        [p for p in Path(folder_path).glob('*.png')],
        #key=lambda x: x.stat().st_ctime
        key=lambda x: x.name
    )

    # Open images and append to a list
    frames = [Image.open(image) for image in images]

    # Save frames as a GIF
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=500,  # duration of each frame in milliseconds
        loop=0  # loop forever
    )

if __name__ == '__main__':

    for mode in ['asni','debug','default','window']:
        folder_path = f'./{mode}'
        output_path = f'{mode}-render.gif'
        create_gif_from_images(folder_path, output_path)