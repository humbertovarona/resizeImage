import os
from PIL import Image

def scale_image(input_image_path, output_image_path, width, height, DPI):
    original_image = Image.open(input_image_path)
    #width, height = original_image.size
    new_resolution = (dpi, dpi)
    scaled_image = original_image.resize((width, height), resample=Image.LANCZOS)
    scaled_image = scaled_image.convert('RGB')
    scaled_image.info["dpi"] = new_resolution
    filename, extension = os.path.splitext(output_image_path)
    output_image_path = f"{filename}_scaled_{DPI}dpi{extension}"
    scaled_image.save(output_image_path, dpi=new_resolution)
    
