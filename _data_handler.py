#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Race-car Data Creation Class.

This script contains all utilities to create proper dataset. 

Revision History:
        2020-05-10 (Animesh): Baseline Software.
        2020-08-22 (Animesh): Updated Docstring.

Example:
        from _data_handler import DataHandler

"""


#___Import Modules:
import os
import random
import pandas as pd
import matplotlib.pyplot as plt
from rc_nn_utility import ParseData


#___Global Variables:
SEED = 717


#__Classes:
class DataHandler:
    """Data Creation Utility Class.
    
    This class contains all methods to complete create datasets such as random
    data set, or 5 fold cross validation dataset.
    
    """


    def __init__(self):
        """Constructor.
        

        """
        
        pass
    

    def merge_all(self, idir, output):
        """File Merger.
        
        This method merges contents from multiple csv files.
        
        Args:
            idir (directory path): Directory path containing all csv files.
            output (csv file): File containing all contents.
        
        Returns:
            (float): Accuracy percentage.

        """
        
        # read all files from provided folder
        files = os.listdir(idir)
        content = []
        
        for ifile in files:
            
            # collect contents from files in provided folder
            if ifile[-4:] == ".csv":
                content.extend(pd.read_csv(os.path.join(idir, \
                                                    ifile))['image'].to_list())
        
        # write merged contents to output file
        pd.DataFrame(content, columns =['image']).to_csv(output, index=False)
        
        return None
    
    
    def list_merge(self, lists):
        """List Merger.
        
        This method merges contents from multiple lists.
        
        Args:
            lists (list): List of multiple lists to merge.
        
        Returns:
            data (list): Merged list.

        """

        # loop over lists and put them all in one list
        data = []
        for list in lists:
            data.extend(list)
        
        return data
    
    
    def refine_running(self, input, output, speed = 15):
        """Refine Running.
        
        This method removes data with provided motor value from a list.
        
        Args:
            input (csv file): File containing contents to refine.
            output (csv file): File containing refined contents.
            speed (int): Motor value to be removed.

        """
        
        parsedata = ParseData()
        
        # read file contents
        data = pd.read_csv(input)
        
        file = []
        for index in range(len(data)):
            
            # parse motor data to varify speed
            _,_,mot = parsedata.parse_data(data["image"][index])
            
            # append data if car is runneing
            if mot != speed:
                file.append(data["image"][index])
        
        # write merged contents to output file
        pd.DataFrame(file, columns=["image"]).to_csv(output, index=False)
        
        return None
    
    
    def histogram(self, ilist, odir):
        """Plot Histogram.
        
        This method plots histogram from servo and motor value parsed from a 
        list of images.
        
        Args:
            ilist (csv file): File containing list of images.
            odir (directory path): Output directory.

        """
        
        parsedata = ParseData()

        # read file contents
        data = pd.read_csv(ilist)
        
        servo = []
        motor = []
        for index in range(len(data)):
            
            # parse servo and motor data
            _,ser,mot = parsedata.parse_data(data["image"][index])
            servo.append(ser)
            motor.append(mot)
        
        # plot histogram of servo data
        plt.figure()
        plt.hist(servo, bins=11)
        plt.title("Servo Data Histogram")
        plt.savefig(os.path.join(odir,"Servo Data Histogram.png"))
        
        # plot histogram of motor data
        plt.figure()
        plt.hist(motor, bins=11)
        plt.title("Motor Data Histogram")
        plt.savefig(os.path.join(odir,"Motor Data Histogram.png"))
        
        return None

    
    def devide_data(self, ilist, odir):
        """Dataset Devider.
        
        This method devides dataset according to servo value.
        
        Args:
            ilist (csv file): File containing list of images.
            odir (directory path): Output directory.

        """
        
        parsedata = ParseData()
        
        # read file contents
        data = pd.read_csv(ilist)
        
        data_10 = []
        data_11 = []
        data_12 = []
        data_13 = []
        data_14 = []
        data_15 = []
        data_16 = []
        data_17 = []
        data_18 = []
        data_19 = []
        data_20 = []
        for index in range(len(data)):

            # parse servo and motor data
            _,servo,_ = parsedata.parse_data(data["image"][index])

            # devide dataset
            if servo == 10:
                data_10.append(data["image"][index])
            elif servo == 11:
                data_11.append(data["image"][index])
            elif servo == 12:
                data_12.append(data["image"][index])
            elif servo == 13:
                data_13.append(data["image"][index])
            elif servo == 14:
                data_14.append(data["image"][index])
            elif servo == 15:
                data_15.append(data["image"][index])
            elif servo == 16:
                data_16.append(data["image"][index])
            elif servo == 17:
                data_17.append(data["image"][index])
            elif servo == 18:
                data_18.append(data["image"][index])
            elif servo == 19:
                data_19.append(data["image"][index])
            elif servo == 20:
                data_20.append(data["image"][index])

        # write data
        pd.DataFrame(data_10, columns=["image"]).to_csv(os.path.join(odir, \
                                                  "servo_10.csv"), index=False)
        pd.DataFrame(data_11, columns=["image"]).to_csv(os.path.join(odir, \
                                                  "servo_11.csv"), index=False)
        pd.DataFrame(data_12, columns=["image"]).to_csv(os.path.join(odir, \
                                                  "servo_12.csv"), index=False)
        pd.DataFrame(data_13, columns=["image"]).to_csv(os.path.join(odir, \
                                                  "servo_13.csv"), index=False)
        pd.DataFrame(data_14, columns=["image"]).to_csv(os.path.join(odir, \
                                                  "servo_14.csv"), index=False)
        pd.DataFrame(data_15, columns=["image"]).to_csv(os.path.join(odir, \
                                                  "servo_15.csv"), index=False)
        pd.DataFrame(data_16, columns=["image"]).to_csv(os.path.join(odir, \
                                                  "servo_16.csv"), index=False)
        pd.DataFrame(data_17, columns=["image"]).to_csv(os.path.join(odir, \
                                                  "servo_17.csv"), index=False)
        pd.DataFrame(data_18, columns=["image"]).to_csv(os.path.join(odir, \
                                                  "servo_18.csv"), index=False)
        pd.DataFrame(data_19, columns=["image"]).to_csv(os.path.join(odir, \
                                                  "servo_19.csv"), index=False)
        pd.DataFrame(data_20, columns=["image"]).to_csv(os.path.join(odir, \
                                                  "servo_20.csv"), index=False)

        return None
    
    
    def train_test_dev(self, type, idir, odir, ratio=None, total=None):
        """Final Dataset Creator.
        
        This method creates train, test and dev dataset.
        
        Args:
            type (string): Determines the type of input dataset
            idir (directory path): Directory containing input CSV files.
            odir (directory path): Output directory.
            ratio (list): List containing ratio of train, test and dev dataset.
            total (list): List containing the number of total data to be parsed
                          from each CSV file.

        """
        
        if type == "random":
            self.random(idir, odir, ratio)
        elif type == "folded":
            self.folded(idir, odir)
        elif type == "controlled":
            self.controlled(idir, odir, ratio, total)

        return None


    def random(self, idir, odir, ratio):
        """Randomly Shuffled Dataset Creator.
        
        This method creates a randomly shuffled train, test and dev dataset.
        
        Args:
            idir (directory path): Directory containing input CSV files.
            odir (directory path): Output directory.
            ratio (list): List containing ratio of train, test and dev dataset.

        """

        # read all files from provided folder
        files = os.listdir(idir)
        content = []

        for ifile in files:

            # collect contents from files in provided folder
            if ifile[-4:] == ".csv":
                content.extend(pd.read_csv(os.path.join(idir, \
                                                    ifile))['image'].to_list())

        # randomly shuffle dataset
        random.shuffle(content)

        # devide dataset into train, test, dev set according to given ratio
        train = content[0:int(ratio[0]*len(content))]
        test = content[int(ratio[0]*len(content)):
                       int((ratio[0]+ratio[1])*len(content))]
        dev = content[int((ratio[0]+ratio[1])*len(content)):]

        # write data
        pd.DataFrame(train, columns=["image"]).to_csv(odir + 'train.csv',
                                                      index=False)
        pd.DataFrame(test, columns=["image"]).to_csv(odir + 'test.csv',
                                                     index=False)
        pd.DataFrame(dev, columns=["image"]).to_csv(odir + 'dev.csv',
                                                    index=False)

        return None
    
    
    def folded(self, idir, odir):
        """5 Fold Cross-Validation Dataset Creator.
        
        This method creates 5 fold cross validation dataset.
        
        Args:
            idir (directory path): Directory containing input CSV files.
            odir (directory path): Output directory.

        """
        
        # read all files from provided folder
        files = os.listdir(idir)
        
        D10 = []
        D11 = []
        D20 = []
        D21 = []
        D30 = []
        D31 = []
        D40 = []
        D41 = []
        D50 = []
        D51 = []
        for ifile in files:
            
            # collect contents from files in provided folder
            if ifile[-4:] == ".csv":
                data = pd.read_csv(idir + ifile)
                D10.extend(data['image'][0:int(len(data)/10)])
                D11.extend(data['image'][int(len(data)/10):2*int(len(data)/10)])
                D20.extend(data['image'][2*int(len(data)/10):3*int(len(data)/10)])
                D21.extend(data['image'][3*int(len(data)/10):4*int(len(data)/10)])
                D30.extend(data['image'][4*int(len(data)/10):5*int(len(data)/10)])
                D31.extend(data['image'][5*int(len(data)/10):6*int(len(data)/10)])
                D40.extend(data['image'][6*int(len(data)/10):7*int(len(data)/10)])
                D41.extend(data['image'][7*int(len(data)/10):8*int(len(data)/10)])
                D50.extend(data['image'][8*int(len(data)/10):9*int(len(data)/10)])
                D51.extend(data['image'][9*int(len(data)/10):])
        
        # create 5 folds of train, test and dev dataset
        train1 = self.list_merge([D10,D11,D20,D21,D30,D31,D40,D41])
        train2 = self.list_merge([D20,D21,D30,D31,D40,D41,D50,D51])
        train3 = self.list_merge([D10,D11,D30,D31,D40,D41,D50,D51])
        train4 = self.list_merge([D10,D11,D20,D21,D40,D41,D50,D51])
        train5 = self.list_merge([D10,D11,D20,D21,D30,D31,D50,D51])
        
        test1 = D50
        test2 = D10
        test3 = D20
        test4 = D30
        test5 = D40
        
        dev1 = D51
        dev2 = D11
        dev3 = D21
        dev4 = D31
        dev5 = D41
        
        # create required directories
        if not os.path.exists(odir + 'fold1/'):
            os.mkdir(odir + 'fold1/')
        if not os.path.exists(odir + 'fold2/'):
            os.mkdir(odir + 'fold2/')
        if not os.path.exists(odir + 'fold3/'):
            os.mkdir(odir + 'fold3/')
        if not os.path.exists(odir + 'fold4/'):
            os.mkdir(odir + 'fold4/')
        if not os.path.exists(odir + 'fold5/'):
            os.mkdir(odir + 'fold5/')
        
        # write data
        pd.DataFrame(train1,columns=["image"]).to_csv(odir + 'fold1/train.csv',
                                                      index=False)
        pd.DataFrame(train2,columns=["image"]).to_csv(odir + 'fold2/train.csv',
                                                      index=False)
        pd.DataFrame(train3,columns=["image"]).to_csv(odir + 'fold3/train.csv',
                                                      index=False)
        pd.DataFrame(train4,columns=["image"]).to_csv(odir + 'fold4/train.csv',
                                                      index=False)
        pd.DataFrame(train5,columns=["image"]).to_csv(odir + 'fold5/train.csv',
                                                      index=False)
        
        pd.DataFrame(test1,columns=["image"]).to_csv(odir + 'fold1/test.csv',
                                                     index=False)
        pd.DataFrame(test2,columns=["image"]).to_csv(odir + 'fold2/test.csv',
                                                     index=False)
        pd.DataFrame(test3,columns=["image"]).to_csv(odir + 'fold3/test.csv',
                                                     index=False)
        pd.DataFrame(test4,columns=["image"]).to_csv(odir + 'fold4/test.csv',
                                                     index=False)
        pd.DataFrame(test5,columns=["image"]).to_csv(odir + 'fold5/test.csv',
                                                     index=False)
        
        pd.DataFrame(dev1,columns=["image"]).to_csv(odir + 'fold1/dev.csv',
                                                    index=False)
        pd.DataFrame(dev2,columns=["image"]).to_csv(odir + 'fold2/dev.csv',
                                                    index=False)
        pd.DataFrame(dev3,columns=["image"]).to_csv(odir + 'fold3/dev.csv',
                                                    index=False)
        pd.DataFrame(dev4,columns=["image"]).to_csv(odir + 'fold4/dev.csv',
                                                    index=False)
        pd.DataFrame(dev5,columns=["image"]).to_csv(odir + 'fold5/dev.csv',
                                                    index=False)

        return None


    def controlled(self, idir, odir, ratio, total):
        """Controlled Dataset Creator.
        
        This method creates train, test and dev dataset from a servo based
        devided dataset in a controlled way.
        
        Args:
            idir (directory path): Directory containing input CSV files.
            odir (directory path): Output directory.
            ratio (list): List containing ratio of train, test and dev dataset.
            total (list): List containing the number of total data to be parsed
                          from each CSV file.

        """
        
        train = [int(x*ratio[0]) for x in total]
        test = [int(x*(ratio[0]+ratio[1])) for x in total]
        total = [int(x) for x in total]
        
        data_10 = pd.read_csv(idir + "servo_10.csv").sample(n=total[0],\
                                                             random_state=SEED)
        data_11 = pd.read_csv(idir + "servo_11.csv").sample(n=total[1],\
                                                             random_state=SEED)
        data_12 = pd.read_csv(idir + "servo_12.csv").sample(n=total[2],\
                                                             random_state=SEED)
        data_13 = pd.read_csv(idir + "servo_13.csv").sample(n=total[3],\
                                                             random_state=SEED)
        data_14 = pd.read_csv(idir + "servo_14.csv").sample(n=total[4],\
                                                             random_state=SEED)
        data_15 = pd.read_csv(idir + "servo_15.csv").sample(n=total[5],\
                                                             random_state=SEED)
        data_16 = pd.read_csv(idir + "servo_16.csv").sample(n=total[6],\
                                                             random_state=SEED)
        data_17 = pd.read_csv(idir + "servo_17.csv").sample(n=total[7],\
                                                             random_state=SEED)
        data_18 = pd.read_csv(idir + "servo_18.csv").sample(n=total[8],\
                                                             random_state=SEED)
        data_19 = pd.read_csv(idir + "servo_19.csv").sample(n=total[9],\
                                                             random_state=SEED)
        data_20 = pd.read_csv(idir + "servo_20.csv").sample(n=total[10],\
                                                             random_state=SEED)
        
        data_train = pd.DataFrame([], columns=["image"])
        data_test = pd.DataFrame([], columns=["image"])
        data_dev = pd.DataFrame([], columns=["image"])
        
        data_train = data_train.append(data_10[0:train[0]], \
                                               ignore_index = True)
        data_train = data_train.append(data_11[0:train[1]], \
                                               ignore_index = True)
        data_train = data_train.append(data_12[0:train[2]], \
                                               ignore_index = True)
        data_train = data_train.append(data_13[0:train[3]], \
                                               ignore_index = True)
        data_train = data_train.append(data_14[0:train[4]], \
                                               ignore_index = True)
        data_train = data_train.append(data_15[0:train[5]], \
                                               ignore_index = True)
        data_train = data_train.append(data_16[0:train[6]], \
                                               ignore_index = True)
        data_train = data_train.append(data_17[0:train[7]], \
                                               ignore_index = True)
        data_train = data_train.append(data_18[0:train[8]], \
                                               ignore_index = True)
        data_train = data_train.append(data_19[0:train[9]], \
                                               ignore_index = True)
        data_train = data_train.append(data_20[0:train[10]], \
                                               ignore_index = True)
        
        data_test = data_test.append(data_10[train[0]:test[0]], \
                                                 ignore_index = True)
        data_test = data_test.append(data_11[train[1]:test[1]], \
                                                 ignore_index = True)
        data_test = data_test.append(data_12[train[2]:test[2]], \
                                                 ignore_index = True)
        data_test = data_test.append(data_13[train[3]:test[3]], \
                                                 ignore_index = True)
        data_test = data_test.append(data_14[train[4]:test[4]], \
                                                 ignore_index = True)
        data_test = data_test.append(data_15[train[5]:test[5]], \
                                                 ignore_index = True)
        data_test = data_test.append(data_16[train[6]:test[6]], \
                                                 ignore_index = True)
        data_test = data_test.append(data_17[train[7]:test[7]], \
                                                 ignore_index = True)
        data_test = data_test.append(data_18[train[8]:test[8]], \
                                                 ignore_index = True)
        data_test = data_test.append(data_19[train[9]:test[9]], \
                                                 ignore_index = True)
        data_test = data_test.append(data_20[train[10]:test[10]], \
                                                 ignore_index = True)
        
        data_dev = data_dev.append(data_10[test[0]:total[0]], \
                                                   ignore_index = True)
        data_dev = data_dev.append(data_11[test[1]:total[1]], \
                                                   ignore_index = True)
        data_dev = data_dev.append(data_12[test[2]:total[2]], \
                                                   ignore_index = True)
        data_dev = data_dev.append(data_13[test[3]:total[3]], \
                                                   ignore_index = True)
        data_dev = data_dev.append(data_14[test[4]:total[4]], \
                                                   ignore_index = True)
        data_dev = data_dev.append(data_15[test[5]:total[5]], \
                                                   ignore_index = True)
        data_dev = data_dev.append(data_16[test[6]:total[6]], \
                                                   ignore_index = True)
        data_dev = data_dev.append(data_17[test[7]:total[7]], \
                                                   ignore_index = True)
        data_dev = data_dev.append(data_18[test[8]:total[8]], \
                                                   ignore_index = True)
        data_dev = data_dev.append(data_19[test[9]:total[9]], \
                                                   ignore_index = True)
        data_dev = data_dev.append(data_20[test[10]:total[10]], \
                                                   ignore_index = True)
        
        # write data
        data_train.to_csv(odir + "train.csv", index=False)
        data_test.to_csv(odir + "test.csv", index=False)
        data_dev.to_csv(odir + "dev.csv", index=False)
        
        return None


#                                                                              
# end of file
"""ANI717"""