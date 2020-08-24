#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Race-car Deep Learning Tool.

This script runs training and testing sessions on Race-car dataset to predict 
speed and steering value from a provided image. 

Revision History:
        2020-05-10 (Animesh): Baseline Software.
        2020-07-25 (Animesh): Updated Docstring.

Example:
        $ python av_train_test.py

"""


#___Import Modules:
import torch
from rc_nn_tools import NNTools


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
TRAIN_DATA = BASE + 'train.csv'
DEV_DATA = BASE + 'dev.csv'
TEST_DATA = BASE + 'test.csv'
SETTINGS = 'settings.json'


#___Main Method:
def main():
    """This is the Main Method.

    This method contains training and testing session for servo and motor data.

    """
    
    # # pass a dummy input to GPU for alloting cache
    # torch.randn(717).cuda()

    # # servo training session:
    # servoTrain = NNTools(settings=SETTINGS, types=['servo','train'])
    # # servoTrain.load_model('models/servo_model.pth')
    # servoTrain.train(TRAIN_DATA, DEV_DATA)

    # # servo testing session:
    # servoTest = NNTools(settings=SETTINGS, types=['servo','test'])
    # # servoTest.test(TEST_DATA, display=True)
    # servoTest.robust_test(TEST_DATA, etype=1)
    
    # servo time count session:
    servoTest = NNTools(settings=SETTINGS, types=['servo','test'])
    servoTest.time_count("data/lists/Debug/time_100.csv")

    # # motor training session:
    # motorTrain = NNTools(settings=SETTINGS, types=['motor','train'])
    # # servoTrain.load_model('models/motor_model.pth')
    # motorTrain.train(TRAIN_DATA, DEV_DATA)

    # # motor testing session:
    # motorTest = NNTools(settings=SETTINGS, types=['motor','test'])
    # # motorTest.test(TEST_DATA, display=True)
    # motorTest.robust_test(TEST_DATA, etype=1)
    
    # # motor time count session:
    # motorTest = NNTools(settings=SETTINGS, types=['motor','test'])
    # motorTest.time_count("data/lists/Debug/time_100.csv")

    return None


#___Driver Program:
if __name__ == "__main__":
    main()


#                                                                              
# end of file
"""ANI717"""