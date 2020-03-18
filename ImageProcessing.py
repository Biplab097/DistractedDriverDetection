from PIL import Image
from resizeimage import resizeimage
from matplotlib import image
from matplotlib import pyplot
import os
import cv2
import numpy as np


class ImageProcessing:
    def resize_Image(self):#sample image converter to change shape and size of existing images
        with open('img_6.jpg', 'r+b') as f:
            with Image.open(f) as img:
                print(img.size)
                cover = resizeimage.resize_cover(img, [64, 64])
                cover.save('test-image-cover.jpeg', img.format)
                data = image.imread('test-image-cover.jpeg')
                pyplot.imshow(data)
                pyplot.show()

    def file_resize(self): #passing particular folder to convert image data to csv file for training purpose minimizing
        #size of single image
        IMG_DIR = '/home/code_broom/PycharmProjects/DistractedDrivers/test'
        for img in os.listdir(IMG_DIR):
            img_array = cv2.imread(os.path.join(IMG_DIR, img), cv2.IMREAD_GRAYSCALE)

            img_pil = Image.fromarray(img_array)
            img_64x64 = np.array(img_pil.resize((64, 64), Image.ANTIALIAS))

            img_array = (img_64x64.flatten())

            img_array = img_array.reshape(-1, 1).T

            print(img_array)

            with open('test.csv', 'ab') as f:
                np.savetxt(f, img_array, delimiter=",")


ob = ImageProcessing()
#ob.resize_Image()
ob.file_resize()
