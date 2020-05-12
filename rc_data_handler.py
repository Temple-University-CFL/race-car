#!/usr/bin/env python
#
#==============================================================================
# Initialization
#==============================================================================
# revision history
#  20200511 (Animesh): baseline software
#
# usage: from rc_data_handler import DataHandler
#
# This script refines dataset and explores prediction
#
#==============================================================================
# Import Modules
#==============================================================================
#
# import global modules
#
import os
import pandas as pd
import matplotlib.pyplot as plt

# import local modules
#
from rc_nn_utility import ParseData

#==============================================================================
# Global Variables
#==============================================================================
SEED = 717

#==============================================================================
# Classes
#==============================================================================

# class: DataHandler
#
# This class refines dataset and explores prefdiction
#
class DataHandler:

    #==========================================================================
    # method: constructor
    #
    # arguments: none
    #
    # return: none
    #
    def __init__(self):
        
        pass
        
    #
    # end of method

    #==========================================================================
    # method: merge_all
    #
    # arguments:
    #  idir: directory path containing all csv lists
    #  output: output list
    #
    # return: none
    #
    # This method merges contents from multiple csv files
    #
    def merge_all(self, idir, output):
        
        # read all files from provided folder
        files = os.listdir(idir)
        content = []
        
        for ifile in files:
            
            # collect contents from files in provided folder
            content.extend(pd.read_csv(os.path.join(idir, \
                                                    ifile))['image'].to_list())
        
        # write merged contents to output file
        pd.DataFrame(content, columns =['image']).to_csv(output, index=False)
        
        return None
    #
    # end of method
    
    #==========================================================================
    # method: refine_running
    #
    # arguments:
    #  input: input list
    #  output: output list
    #
    # return: none
    #
    # This method removes data when car is not running
    #
    def refine_running(self, input, output):
        
        parsedata = ParseData()
        
        # read file contents
        data = pd.read_csv(input)
        
        file = []
        for index in range(len(data)):
            
            # parse motor data to varify speed
            _,_,mot = parsedata.parse_data(data["image"][index])
            
            # append data if car is runneing
            if mot != 15:
                file.append(data["image"][index])
        
        # write merged contents to output file
        pd.DataFrame(file, columns=["image"]).to_csv(output, index=False)
        
        return None
    #
    # end of method
    
    #==========================================================================
    # method: histogram
    #
    # arguments:
    #  ilist: image file list
    #  odir: output directory
    #
    # return: none
    #
    # This method removes data when car is not running
    #
    def histogram(self, ilist, odir):
        
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
    #
    # end of method
    
    #==========================================================================
    # method: devide_data
    #
    # arguments:
    #  ilist: image file list
    #  odir: output directory
    #
    # return: none
    #
    # This method devides dataset according to servo value
    #
    def devide_data(self, ilist, odir):
        
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
    #
    # end of method
    
    #==========================================================================
    # method: train_test_dev
    #
    # arguments:
    #  ilist: image file list
    #  odir: output directory
    #
    # return: none
    #
    # This method creates train, test and dev dataset
    #
    def train_test_dev(self, total, ratio):
        
        train = [int(x*ratio[0]) for x in total]
        test = [int(x*(ratio[0]+ratio[1])) for x in total]
        total = [int(x) for x in total]
        
        data_10 = pd.read_csv("data/lists/servo_10.csv").sample(n=total[0],\
                                                             random_state=SEED)
        data_11 = pd.read_csv("data/lists/servo_11.csv").sample(n=total[1],\
                                                             random_state=SEED)
        data_12 = pd.read_csv("data/lists/servo_12.csv").sample(n=total[2],\
                                                             random_state=SEED)
        data_13 = pd.read_csv("data/lists/servo_13.csv").sample(n=total[3],\
                                                             random_state=SEED)
        data_14 = pd.read_csv("data/lists/servo_14.csv").sample(n=total[4],\
                                                             random_state=SEED)
        data_15 = pd.read_csv("data/lists/servo_15.csv").sample(n=total[5],\
                                                             random_state=SEED)
        data_16 = pd.read_csv("data/lists/servo_16.csv").sample(n=total[6],\
                                                             random_state=SEED)
        data_17 = pd.read_csv("data/lists/servo_17.csv").sample(n=total[7],\
                                                             random_state=SEED)
        data_18 = pd.read_csv("data/lists/servo_18.csv").sample(n=total[8],\
                                                             random_state=SEED)
        data_19 = pd.read_csv("data/lists/servo_19.csv").sample(n=total[9],\
                                                             random_state=SEED)
        data_20 = pd.read_csv("data/lists/servo_20.csv").sample(n=total[10],\
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
        
        data_train.to_csv("data/lists/train.csv", index=False)
        data_test.to_csv("data/lists/test.csv", index=False)
        data_dev.to_csv("data/lists/dev.csv", index=False)
        
        return None
    #
    # end of method

#==============================================================================







#==============================================================================
# Debugging Block ANI717
#==============================================================================
# datahandler = DataHandler()
# datahandler.merge_all("data/lists/refined/", "data/lists/refined.csv")

# datahandler = DataHandler()
# datahandler.refine_running("data/lists/refined.csv", "data/lists/running.csv")