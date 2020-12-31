#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Race-car Deep Learning Tool.

This script runs testing session on Race-car dataset to predict servo and 
motor control values from a provided image. 

Revision History:
        2020-12-25 (Animesh): Baseline Software.

Example:
        $ python train.py

"""


#___Import Modules:
from _train_test import NNTools


#___Global Variables:
LIST = ['data/lists/Random/', 
        'data/lists/5 Fold Cross-Val/fold1/',
        'data/lists/5 Fold Cross-Val/fold2/',
        'data/lists/5 Fold Cross-Val/fold3/',
        'data/lists/5 Fold Cross-Val/fold4/',
        'data/lists/5 Fold Cross-Val/fold5/',
        'data/lists/Debug/',
        'data/']

BASE = LIST[7]

TEST_DATA = BASE + 'test.csv'
SETTINGS = 'settings.json'

TYPE = 1 # 0: Motor Control Value, 1: Servo Control Value
ROBUST = 1 # Flag for robust test


#___Main Method:
def main():
    """This is the Main Method.

    This method contains testing session to predict speed and steering value.

    """
    
    if TYPE:
        
        # testing session for servo control value prediction:
        servoTest = NNTools(settings=SETTINGS, types=['servo','test'])
        if ROBUST:
            servoTest.robust_test(TEST_DATA)
        else:
            servoTest.test(TEST_DATA, display=True)
    
    else:
        
        # testing session for motor control value prediction:
        motorTest = NNTools(settings=SETTINGS, types=['motor','test'])
        if ROBUST:
            motorTest.robust_test(TEST_DATA)
        else:
            motorTest.test(TEST_DATA, display=True)

    return None


#___Driver Program:
if __name__ == "__main__":
    main()


#                                                                              
# end of file
"""ANI717"""