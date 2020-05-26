import cv2
from keras.models import load_model
import os


CATEGORIES = ["SAFE","CELL_RIGHT","CALL_RIGHT","CELL_LEFT","CALL_LEFT","RADIO_RIGHT","DRINK"]
class PredictClass:
    def prepare(self,filepath):

      img_reshape_size = (224,224)
      img = cv2.imread(filepath)
      img = cv2.resize(img, img_reshape_size)
      return img

    def predictClass(self,item):

        model = load_model("/home/code_broom/PycharmProjects/DistractedDrivers/Models/class_7/VGG16_lr0.0001_train3_epochs4_data_aug0.h5")
        imgs = []
        imgs.append(item)
        prediction = model.predict([imgs])
        list1 = prediction[0].tolist()
        print(list1)
        print(CATEGORIES[list1.index(max(list1))])

print("starting....")
ob = PredictClass()
item = ob.prepare("frame300.jpg")
ob.predictClass(item)

