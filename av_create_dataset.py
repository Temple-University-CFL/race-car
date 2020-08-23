#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Race-car Dataset Refining Tool.

This script helps to create dataset for deep learning sessions.

Revision History:
        2020-05-11 (Animesh): Baseline Software.
        2020-07-25 (Animesh): Updated Docstring.

Example:
        $ python rc_refine_dataset.py

"""


#___Import Modules:
from rc_data_handler import DataHandler


#___Global Variables:
TYPE = ['random', 'folded', 'controlled']


#___Main Method:
def main():
    """This is the Main Method.

    This method performs required operations to create proper dataset.

    """

    datahandler = DataHandler()

    # # merge all csv files in a folder to one csv file
    # datahandler.merge_all("data/lists/Base Dataset/0_2Floor/", 
    #                       "data/lists/Refined/0_2Floor.csv")
    # datahandler.merge_all("data/lists/Base Dataset/0_6Floor/", 
    #                       "data/lists/Refined/0_6Floor.csv")
    # datahandler.merge_all("data/lists/Base Dataset/1_2Floor/", 
    #                       "data/lists/Refined/1_2Floor.csv")

    # # remove data when car is not running
    # datahandler.refine_running("data/lists/Refined/0_2Floor.csv", 
    #                             "data/lists/Running/0_2Floor.csv", 15)
    # datahandler.refine_running("data/lists/Refined/0_6Floor.csv", 
    #                             "data/lists/Running/0_6Floor.csv", 15)
    # datahandler.refine_running("data/lists/Refined/1_2Floor.csv", 
    #                             "data/lists/Running/1_2Floor.csv", 15)

    # # devide dataset according to servo values
    # datahandler.merge_all("data/lists/Running/", 
    #                       "data/lists/Servo Based Devided/running.csv")
    # datahandler.devide_data("data/lists/Servo Based Devided/running.csv", 
    #                         "data/lists/Servo Based Devided/")

    # # create random sorted train, test, dev dataset
    # ratio = [0.8,0.1,0.1] # train:test:dev
    # datahandler.train_test_dev(TYPE[0], "data/lists/Running/",
    #                             "data/lists/Random/", ratio)
    
    # # create 5-fold cross validation train, test, dev dataset
    # datahandler.train_test_dev(TYPE[1], "data/lists/Running/",
    #                             "data/lists/5 Fold Cross-Val/")

    # # create train, test, dev dataset from servo based devided dataset
    # # total = [3161,5651,11678,8855,5987,11707,3736,6934,5241,1763,1340]
    # total = [1340,1340,1340,1340,1340,1340,1340,1340,1340,1340,1340]
    # ratio = [0.8,0.1,0.1] # train:test:dev
    # datahandler.train_test_dev(TYPE[2], "data/lists/Servo Based Devided/",
    #                             "data/lists/Controlled/", ratio, total)

    # plot histogram
    datahandler.histogram("data/train.csv", "data/histogram/")

    return None


#___Driver Program:
if __name__ == "__main__":
    main()


#                                                                              
# end of file
"""ANI717"""