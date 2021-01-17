#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Race-car Deep Learning Tool.

This script runs testing session on Race-car dataset to calculate required 
time. 

Revision History:
        2020-12-25 (Animesh): Baseline Software.

Example:
        $ python train.py

"""


#___Import Modules:
from _train_test import NNTools


#___Global Variables:
TEST_DATA = "data/lists/Debug/time_100.csv"
SETTINGS = 'settings.json'

TYPE = 1 # 0: Motor Control Value, 1: Servo Control Value
ROBUST = 1 # Flag for robust test


#___Main Method:
def main():
    """This is the Main Method.

    This method contains time count session.

    """
    
    if TYPE:
        
        # testing session for servo control value prediction:
        servoTest = NNTools(settings=SETTINGS, types=['servo','test'])
        servoTest.time_count(TEST_DATA)
    
    else:
        
        # testing session for motor control value prediction:
        motorTest = NNTools(settings=SETTINGS, types=['motor','test'])
        motorTest.time_count(TEST_DATA)

    return None


#___Driver Program:
if __name__ == "__main__":
    main()


#                                                                              
# end of file
"""ANI717"""