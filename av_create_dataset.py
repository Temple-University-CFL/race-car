#!/usr/bin/env python
#
#==============================================================================
# Initialization
#==============================================================================
# revision history
#  20200511 (Animesh): baseline software
#
# usage: python av_train_test
#
# This script helps create dataset
#
#==============================================================================
# Import Modules
#==============================================================================
#
# import local modules
#
from rc_data_handler import DataHandler

#==============================================================================
# Main Method
#==============================================================================
# method: main
#
# arguments: none
#
# return: none
#
# This method is the main function
#
def main():

    datahandler = DataHandler()
    
    # merge csv files in a folder
    datahandler.merge_all("data/lists/refined/", "data/lists/refined.csv")
    
    # remove data when car is not running
    datahandler.refine_running("data/lists/refined.csv", "data/lists/running.csv")
    
    # plot histogram for servo and motor data from total dataset
    datahandler.histogram("data/lists/running.csv", "data/lists/")
    
    # devide dataset according to servo values
    datahandler.devide_data("data/lists/running.csv", "data/lists/")
    
    # create train, test, dev dataset
    total = [3161,3736,5241,5241,3736,5241,3736,5241,5241,1763,1340]
    ratio = [0.8,0.1,0.1]
    datahandler.train_test_dev(total, ratio)
    
    # plot histogram for servo and motor data from train dataset
    datahandler.histogram("data/lists/train.csv", "output/curves/")

#==============================================================================
# Driver Program
#==============================================================================
if __name__ == "__main__":
    main()

#                                                                            
# end of file
# ANI717