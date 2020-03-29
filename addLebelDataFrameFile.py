import pandas as pd
import os
import csv


class AddLabel:
    def addLabelDataFrameFile(self):
        IMG_DIR = '/home/code_broom/PycharmProjects/DistractedDrivers/csv_lebels'
        num_files=[]                                                 # stores all file with .csv extension
        fileNames = os.listdir(IMG_DIR)                              # list out all files in that directory
        fileNames.sort()                                             # sort the list with name of files
        print(fileNames)
        images = []                                                  # stores all images of csv file in list
        label = []                                                   # add label in data frame object

        for fileName in fileNames:
            if fileName.endswith(".csv"):
                num_files.append(fileName)                           # only append files with .csv

        for ele in num_files:
            if ele == 'c9.csv':    # pass file name which u want to create data frame     # doing for a particular file
                file = open(os.path.join(IMG_DIR, ele), "rb")        # rb stands for read binary
                reader = csv.reader(file)
                df = pd.read_csv(file)                             # more faster than csv.reader
                # reader = reader(file)
                # print(type(data))
                # print(df)
                i = 0

                df_row = df.shape[0]                               # return no. rows in df object created from csv file
                df_col = df.shape[1]                               # no. of column in df object
                print(df_row)

                for i in range(df_row):                            # iterate over rows of df
                    image = df.values[i][0:]                       # store image
                    images.append(image)                           # append image to images list
                    label.append(ele[1])                           # add label to all images according to class

                # for row in reader:
                #     images.append(row)
                #     label.append(ele[1])

        # print(len(images))
        # for img in os.listdir(IMG_DIR):
        #     img_list.append(img)
        #     label.append(0)

        my_dict = {'image':images,'label':label}
        # print(my_dict)
        df = pd.DataFrame(my_dict)
        print(df)
        df.to_csv('c9_df.csv')    # provide file name it will save with this particular name so change for every file


ob = AddLabel()
ob.addLabelDataFrameFile()
