from PIL import Image

def get_resolution(image_path):
    with Image.open(image_path) as img:
        resolution = img.info.get("dpi")
        return resolution
