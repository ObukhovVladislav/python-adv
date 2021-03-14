import numpy as np
from PIL import Image

image_name = '../data/space.jpg'
image = Image.open(image_name)
image_np = np.array(image)
# image_np_conv = image_np / 5
image_np_conv = image_np + 15
new_image = Image.fromarray(image_np_conv.astype('uint8'))
save_name = 'space_conv.jpg'
new_image.save(save_name)
