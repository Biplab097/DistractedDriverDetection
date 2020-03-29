import os

import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

file = open(os.path.join('/home/code_broom/PycharmProjects/DistractedDrivers/csv_lebels', 'c0.csv'), "rb")

df = pd.read_csv(file)                                       # read the training data file from working directory

print(df)
i = 0                                                        # set any valid index of an image
label = df.values[i][0]                                      # retrieve label from first column in data frame
im_buf = df.values[i][0:]                                    # create flat array of only the pixels of the given image
axis_len = int(np.math.sqrt(im_buf.shape[0]))                # calculate the dimensions of the square image
im_array = np.int8(np.reshape(im_buf, (axis_len, axis_len))) # create a 2D array from flat array
img = Image.fromarray(im_array, 'L')                         # convert to a PIL.Image object ('L' is for grayscale)

print(type(img))
# print(f'Label: {label}')
# img.show()
i = np.asarray(img)
plt.imshow(i, cmap="gray")
plt.show()