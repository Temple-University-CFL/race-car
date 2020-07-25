#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Race-car Deep Learning Tool.

This script runs training and testing sessions on Race-car dataset to predict 
speed and steering value from a provided image. 

Revision history:
        2020-05-10 (Animesh): Base-line Software
        2020-07-25 (Animesh): Updated Docstring

Example:
        $ python av_train_test.py

"""


#___Import Modules:
from rc_nn_tools import NNTools


#___Global Variables:
BASE = 'data/lists/5 Fold Cross-Val/fold5/'
# BASE = 'data/lists/Random/'

TRAIN_DATA = BASE + 'train.csv'
DEV_DATA = BASE + 'dev.csv'
TEST_DATA = BASE + 'test.csv'
SETTINGS = 'settings.json'


#___Main Method:
def main():
    """This is the Main Method.

    This method contains training and testing session for servo and motor data

    Returns:
        None

    """

    # servo training session:
    servoTrain = NNTools(settings=SETTINGS, types=['servo','train'])
    # servoTrain.load_model('models/servo_model.pth')
    servoTrain.train(TRAIN_DATA, DEV_DATA)

    # # servo testing session:
    # servoTest = NNTools(settings=SETTINGS, types=['servo','test'])
    # servoTest.test(TEST_DATA, display=True)

    # # motor training session:
    # motorTrain = NNTools(settings=SETTINGS, types=['motor','train'])
    # servoTrain.load_model('models/motor_model.pth')
    # motorTrain.train(TRAIN_DATA, DEV_DATA)

    # # motor testing session:
    # motorTest = NNTools(settings=SETTINGS, types=['motor','test'])
    # motorTest.test(TEST_DATA, display=True)

    return None


#___Driver Program:
if __name__ == "__main__":
    main()


#                                                                              
# end of file
"""ANI717"""