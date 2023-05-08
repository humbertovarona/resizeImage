

input_image_path = "data/images/sample.jpeg"
output_image_path = input_image_path
width = 800 # 800 pixels
height = 600 # 600 pixels
dpi = 900

scale_image(input_image_path, output_image_path, width, height, dpi)

input_image_path = "data/images/sample1.jpeg"
output_image_path = input_image_path
width_cm = 15 # 15cm
height_cm = 12 # 12cm
dpi = 550

scale_image_cm(input_image_path, output_image_path, width_cm, height_cm, dpi)

input_image_path = "data/images/sample_scaled_900dpi.jpeg"

resolution = get_resolution(input_image_path)
if resolution:
    print(f"Image resolution: {resolution[0]}x{resolution[1]} dpi")
else:
    print("Resolution information not available.")

dimensions = get_image_dimensions(input_image_path)
print(dimensions)
