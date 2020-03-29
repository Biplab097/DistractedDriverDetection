import os
import pickle
import pandas as pd


class MergeAndShuffle:

    def mergeCsvFiles(self):
        csv_header = 'index,image,label'                                 # comma separated value for heading
        csv_out = 'data.csv'                                             # output merged file name

        csv_dir = '/home/code_broom/PycharmProjects/DistractedDrivers/dataframe_csv'  # path to the directory of files
        print(csv_dir)                                                    # to be merged
        dir_tree = os.walk(csv_dir)                                       # list down all the tree of files
        for dirpath, dirnames, filenames in dir_tree:
            pass

        print(dir_tree)
        csv_list = []
        for file in filenames:
            if file.endswith('.csv'):
                csv_list.append(file)                               # store file names with .csv in list
        print(csv_list)
        csv_merge = open(csv_out, 'w')                              # open to write to file
        csv_merge.write(csv_header)                                 # write  csv header
        csv_merge.write('\n')                                       # write new line

        for file in csv_list:
            csv_in = open(os.path.join(csv_dir, file), "rt")        # open file to text write
            print(type(csv_in))
            for line in csv_in:
                # print(type(line))
                if line.startswith(csv_header):                      # ignore top header of files and write
                    continue
                csv_merge.write(line)                                # write all the lines to new merged file
        csv_in.close()
        csv_merge.close()                                            # closes csv file after merging
        # with open()
        print('Verify merged CSV file : ' + csv_out)                 # verify and print

        df_data = pd.read_csv(csv_out,skiprows=1)
        # print(df_data)

        with open('/home/code_broom/PycharmProjects/DistractedDrivers/dataframe_of_data.pkl', 'wb') as f:
            pickle.dump(df_data, f)

        with open('/home/code_broom/PycharmProjects/DistractedDrivers/dataframe_of_data.pkl', 'rb') as f:
            df_pkl = pickle.load(f)

        df_pkl = df_pkl.sample(frac=1).reset_index(drop=True)
        print(df_pkl)


ob = MergeAndShuffle()
ob.mergeCsvFiles()
