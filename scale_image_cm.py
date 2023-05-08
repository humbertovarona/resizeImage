import os
from PIL import Image

def scale_image_cm(input_image_path, output_image_path, width_cm, height_cm, DPI):
    original_image = Image.open(input_image_path)
    #width_px, height_px = image.size
    px_per_cm = dpi / 2.54
    width_cm = int(width_cm * px_per_cm)
    height_cm = int(height_cm * px_per_cm)
    scaled_image = original_image.resize((width_cm, height_cm), resample=Image.LANCZOS)
    scaled_image = scaled_image.convert('RGB')
    filename, extension = os.path.splitext(output_image_path)
    output_image_path = f"{filename}_scaled_{DPI}dpi{extension}"
    scaled_image.save(output_image_path, dpi=(DPI, DPI))
