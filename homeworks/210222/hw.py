import numpy as np
from PIL import Image

image_name = 'space.jpg'
image = Image.open(image_name)
image_np = np.array(image)
# image_np_conv = image_np / 5
image_np_conv = image_np + 15


# print(image_np[:, :, 0].mean(), image_np[:, :, 1].mean(),
#       image_np[:, :, 2].mean())
# print(image_np_conv[:, :, 0].mean(), image_np_conv[:, :, 1].mean(),
#       image_np_conv[:, :, 2].mean())

new_image = Image.fromarray(image_np_conv.astype('uint8'))
save_name = 'space_conv.jpg'
new_image.save(save_name)
