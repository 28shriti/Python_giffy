import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = ['img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg']
images = []

# Set the target size (e.g., 256x256)
target_size = (256, 256)

for filename in filenames:
    img = iio.imread(filename)
    
    # Convert the image to a PIL Image object
    pil_img = Image.fromarray(img)
    
    # Resize the image
    pil_img = pil_img.resize(target_size)
    
    # Convert back to numpy array and append to the images list
    images.append(np.array(pil_img))

# Write the images to a GIF
iio.imwrite('picture.gif', images, duration=500, loop=0)


# import imageio.v3 as iio

# filenames = ['img1.jpg', 'img2.jpg','img3.jpg','img4.jpg']
# images = [ ]

# for filename in filenames:
#     images.append(iio.imread(filename))

# iio.imwrite('picture.gif', images, duration = 500, loop = 0)


