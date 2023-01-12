#! /usr/bin/python3

from PIL import Image

image = Image.open('tunn3l_v1s10n.png')

# Open Image
# image.show()

# The file format of the source file.
print(image.format) # Output: JPEG

# The pixel format used by the image. Typical values are "1", "L", "RGB", or "CMYK."
print(image.mode) # Output: RGB

# Image size, in pixels. The size is given as a 2-tuple (width, height).
print(image.size) # Output: (1920, 1280)

# Colour palette table, if any.
print(image.palette) # Output: None




new_image = image.resize((400, 400))
new_image.save('image_400.jpg')

print(image.size) # Output: (1920, 1280)

print(new_image.size) # Output: (400, 400)