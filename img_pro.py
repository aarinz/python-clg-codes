from PIL import Image, ImageFilter

# Load the image
input_image_path = "pog.png"
input_image = Image.open(input_image_path)

# a) Convert an image from RGBA to L mode
converted_image = input_image.convert("L")
converted_image.save("converted_image.png")

# b) Rotate the image 5 different angles
angles = [90, 180, 270, 45, 135]
for angle in angles:
    rotated_image = input_image.rotate(angle, expand=True)
    rotated_image.save(f"rotated_image_{angle}.png")

# c) Paste one image on another image
# Load the second image
second_image_path = "pog2.png"
second_image = Image.open(second_image_path)

# Resize the second image to fit the first image
second_image = second_image.resize(input_image.size)

# Paste the second image onto the first image
pasted_image = input_image.copy()
pasted_image.paste(second_image, (0, 0))

# Save the pasted image
pasted_image.save("pasted_image.png")

# d) Apply five different filters to the image
filter_names = ["BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EMBOSS"]
for filter_name in filter_names:
    filtered_image = input_image.filter(getattr(ImageFilter, filter_name))
    filtered_image.save(f"filtered_image_{filter_name.lower()}.png")

#Display the properties of the image
print("Image properties:")
print("Format:", input_image.format)
print("Mode:", input_image.mode)
print("Size:", input_image.size)
print("Width:", input_image.width)
print("Height:", input_image.height)

# b) Save the image to a different file format
# Convert the image to RGB mode (if it's in RGBA mode)
if input_image.mode == "RGBA":
    input_image = input_image.convert("RGB")

# Save the image to a different file format (JPEG)
output_format = "JPEG"
output_image_path = "output_image." + output_format.lower()
input_image.save(output_image_path, format=output_format)

# c) Resize the image
new_size = (input_image.width // 2, input_image.height // 2)  # Resize to half of the original size
resized_image = input_image.resize(new_size)
resized_image.save("resized_image.png")

# d) Crop the image
# Define the cropping region (left, upper, right, lower)
crop_region = (100, 100, 400, 400)
cropped_image = input_image.crop(crop_region)
cropped_image.save("cropped_image.png")

# e) Flip the image left to right and top to bottom
flipped_lr_image = input_image.transpose(Image.FLIP_LEFT_RIGHT)
flipped_lr_image.save("flipped_lr_image.png")

flipped_tb_image = input_image.transpose(Image.FLIP_TOP_BOTTOM)
flipped_tb_image.save("flipped_tb_image.png")