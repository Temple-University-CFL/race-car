#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Race-car Dataset Refining Tool.

This script helps create dataset for deep learning sessions.

Revision History:
        2020-05-11 (Animesh): Baseline Software
        2020-07-25 (Animesh): Updated Docstring

Example:
        $ python rc_refine_dataset.py

"""


#___Import Modules:
from rc_data_handler import DataHandler


#___Main Method:
def main():
    """This is the Main Method.

    This method performs required operations to create proper dataset.

    Returns:
        None

    """

    datahandler = DataHandler()

    # # merge csv files in a folder
    # datahandler.merge_all("data/lists/refined/0_6Floor/", "data/lists/refined/0_6Floor.csv")

    # # remove data when car is not running
    # datahandler.refine_running("data/lists/refined.csv", "data/lists/running.csv")

    # # plot histogram for servo and motor data from total dataset
    # datahandler.histogram("data/train.csv", "")

    # # devide dataset according to servo values
    # datahandler.devide_data("data/lists/running.csv", "data/lists/")

    # # create train, test, dev dataset
    # # total = [3161,5651,11678,8855,5987,11707,3736,6934,5241,1763,1340]
    # total = [1340,1340,1340,1340,1340,1340,1340,1340,1340,1340,1340]
    # ratio = [0.8,0.1,0.1]
    # datahandler.train_test_dev(total, ratio)

    # plot histogram for servo and motor data from train dataset
    datahandler.histogram("data/lists/train.csv", "output/curves/")

    return None


#___Driver Program:
if __name__ == "__main__":
    main()


#                                                                              
# end of file
"""ANI717"""