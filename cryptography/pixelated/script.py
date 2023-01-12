# try:
#     from PIL import Image
# except ImportError:
#     import Image

# background = Image.open("scrambled1.png")
# overlay = Image.open("scrambled2.png")

# # background = background.convert("RGBA")
# # overlay = overlay.convert("RGBA")

# background.paste(overlay, (0,0))

# background.show()
# background.save("decrypt.png","PNG")

# new_img = Image.blend(background, overlay, 1)
# new_img.save("decrypt.png","PNG")

# import cv2
# import numpy as np

# img1 = cv2.imread('scrambled1.png')
# img2 = cv2.imread('scrambled2.png')
# dst = cv2.addWeighted(img1, 0.5, img2, 0.7, 0)

# img_arr = np.hstack((img1, img2))
# cv2.imshow('Input Images',img_arr)
# cv2.imshow('Blended Image',dst)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import Image
from PIL import Image

# open both photos
i1 = Image.open('scrambled1.png')
i2 = Image.open('scrambled2.png')

# get width and height
width1, height1 = i1.size

# open new image
i3 = Image.new('RGB', (width1, height1))

# load the pixels
pixels = i3.load()

# loop through all pixels
for i in range(width1):
    for j in range(height1):
        # xor the values
        x = i1.getpixel((i,j))[0] ^ i2.getpixel((i,j))[0]
        y = i1.getpixel((i,j))[1] ^ i2.getpixel((i,j))[1]
        z = i1.getpixel((i,j))[2] ^ i2.getpixel((i,j))[2]

        # if all white then convert to black
        if (x,y,z) == (255,255,255):
            (x,y,z) = (0,0,0)

        # put the new pixels in place
        i3.putpixel((i,j), (x,y,z))

# save the image
i3.save("decrypt.png", "PNG")